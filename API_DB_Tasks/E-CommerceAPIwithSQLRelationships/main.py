
from decimal import Decimal

from fastapi import FastAPI, Depends, HTTPException, status
from models import *
from database import *
# ---------------------------------------------------------
# 4. FASTAPI APP & WRITE OPERATIONS
# ---------------------------------------------------------
from fastapi import FastAPI

from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from order_status import *
app = FastAPI(title="E-Commerce API with SQL Relationships")

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_users(userCreate: UserCreate, db: AsyncSession = Depends(get_db)):
    user_create= User(name=userCreate.name,email=userCreate.email)
    try:
        db.add(user_create)
        await db.flush()
        return {"message": "User created successfully", "user_id": user_create.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Database operational failure: {str(e)}")

@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    try:
         user_result = await db.execute(select(User)
                                        .order_by(User.name)
                                       )
         return user_result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Details{ex}")
@app.get("/users/{user_name}")
async def get_users(user_name:str,db: AsyncSession = Depends(get_db)):
    try:
         user_result = await db.execute(select(User).where(User.name==user_name)
                                        .order_by(User.name)
                                    )
         return user_result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Details{ex}")
    
@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_product(productCreat:ProductCreate,db: AsyncSession = Depends(get_db)):
    product_create= Product(name=productCreat.name,
                             price=productCreat.price,
                             inventory_count=productCreat.inventory_count)
    try:
        db.add(product_create)
        await db.flush()
        return {"message": "Product created successfully", "product_id": product_create.id}
    except Exception as e:
            await db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Database operational failure: {str(e)}")

@app.get("/products/{product_name}")
async def get_users(product_name:str=None,db: AsyncSession = Depends(get_db)):
    try:
         query = select(Product)
         if product_name:
             query = query.where(Product.name==product_name)
         query = query.order_by(Product.name)
         user_result = await db.execute(query)
         return user_result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Details{ex}")
    
@app.post("/orders/", status_code=status.HTTP_201_CREATED)
async def create_orders(orderCreate: OrderCreate, db: AsyncSession = Depends(get_db)):
    # 1. Fetch user asynchronously using select()
    user_result = await db.execute(select(User).filter(User.id == orderCreate.user_id))
    user = user_result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
        
    try:
        # Initialize order total variable
        order_total = Decimal("0.00")
        
        order = Order(
            id=uuid4(),
            user_id=orderCreate.user_id,
            status=OrderStatus.PENDING.value,
            total_amount=order_total
        )
        db.add(order)
        await db.flush()  # Flush asynchronously to generate IDs if needed

        for prd in orderCreate.items:
            # 2. Fetch product asynchronously using select()
            product_result = await db.execute(select(Product).filter(Product.id == prd.product_id))
            product = product_result.scalars().first()
            
            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Product with ID {prd.product_id} not found"
                )
                
            if product.inventory_count < prd.quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Insufficient stock for product {product.id}"
                )
            
            unit_price = Decimal(str(product.price))
            item_total = unit_price * prd.quantity
            
            order_item = OrderItem(
                id=uuid4(),
                order_id=order.id,
                product_id=product.id,
                quantity=prd.quantity,
                unit_price=unit_price,
                item_total=item_total
            )
            db.add(order_item)
            
            # Deduct inventory and accumulate totals
            product.inventory_count -= prd.quantity
            order_total += item_total

        # 3. Update order final values after processing all loop items
        order.total_amount = order_total
        order.status = OrderStatus.CONFIRMED.value
        
        # 4. Commit and refresh asynchronously
        await db.commit()
        await db.refresh(order)
        
        return {
            "message": "Order placed successfully",
            "order_id": str(order.id),
            "order_total": float(order.total_amount)
        }
        
    except HTTPException:
        # Re-raise HTTPExceptions so FastAPI handles them properly instead of catching them as general exceptions
        await db.rollback()
        raise
    except Exception as ex:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )

@app.patch("/orders/{order_id}/cancel")
async def create_orders(order_id:str, db: AsyncSession = Depends(get_db)):   
    try:
          order_results = await db.execute(select(Order).filter(Order.id == order_id))
          order = order_results.scalars().first()
          order.status=OrderStatus.CANCELLED
          db.commit()
          db.flush()
          return {
              "message": "Order Cacnelled",
              "order_id": str(order.id),
          }
    except Exception as ex:
        raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=str(ex)
                )
@app.patch("/product/")
async def update_product_inventory(product_id:str,
                        inventory_count:int,
                        db: AsyncSession = Depends(get_db)):   
    try:
              produt_result = await db.execute(select(Product).filter(Product.id == product_id))
              product = produt_result.scalars().first()
              product.inventory_count = inventory_count
              db.commit()
              db.flush()
              return {
                  "message": "Product Invetory Updated",
                  "order_id": product,
              }
    except Exception as ex:
        raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=str(ex)
                )
