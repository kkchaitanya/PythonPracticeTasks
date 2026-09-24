
from fastapi import FastAPI, Depends, HTTPException, status
from models import *
from database import *
# ---------------------------------------------------------
# 4. FASTAPI APP & WRITE OPERATIONS
# ---------------------------------------------------------
from fastapi import FastAPI

from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

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
