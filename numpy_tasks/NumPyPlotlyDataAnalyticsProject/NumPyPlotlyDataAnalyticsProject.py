import numpy as np
import pandas as pd
import plotly.express as px
months =  np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
revenue = np.random.randint(500000, 2000000, 12) # Revenue in ₹
orders = np.random.randint(1000, 10000, 12) # Number of orders
customers = np.random.randint(800, 8000, 12) # Number of customers
expenses = np.random.randint(300000, 1200000, 12) # Expenses in ₹


revenue_df= pd.DataFrame({
            "Month": months,
            "Orders": orders,
            "Revenue": revenue,
            "Customers":customers,
            "Expenses":expenses
            })

print(revenue_df)

### Calculate total annual revenue.###
print("total annual revenue",revenue_df["Revenue"].sum())
### Calculate average monthly revenue. ###
print("average monthly revenue.",revenue_df["Revenue"].mean())
### Find the best-performing month. ###
print("best-performing month")
#print(revenue_df[revenue_df["Revenue"]==revenue_df["Revenue"].max()]["Month"])
print(revenue_df.loc[revenue_df["Revenue"].idxmax(), "Month"])
#print(revenue_df.loc[revenue_df["Revenue"].idxmax()])
### Find the lowest-performing month. ###
print("Find the lowest-performing month.")
print(revenue_df.loc[revenue_df["Revenue"].idxmin(), "Month"])
## Calculate month-to-month revenue differences. ##
revenue_df["Revenue_Difference"] = revenue_df["Revenue"].diff()
print(revenue_df)
## Create a line chart showing revenue trends. ##
line_chart = px.line(
                revenue_df,
                x="Month",
                y="Revenue",
                title="Monthly Revenue Trend",
                markers=True)
line_chart.show()
## Create a bar chart showing monthly orders
bar_chart = px.bar(revenue_df,
                   x="Month",
                   y="Orders",
                   title="monthly orders"
                   )
bar_chart.show()


fig = px.line(
    revenue_df,
    x="Month",
    y=["Revenue", "Expenses"],
    markers=True,
    title="Monthly Revenue vs Expenses"
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Amount",
    legend_title="Metrics",
    template="plotly_white"
)

fig.show()
import plotly.express as px

fig = px.bar(
    revenue_df,
    x="Month",
    y=["Revenue", "Expenses"],
    barmode="group",
    title="Monthly Revenue vs Expenses",
    labels={
        "value": "Amount",
        "variable": "Metric"
    }
)

fig.show()

## Create customer-growth visualization.##
line_chart = px.line(
                revenue_df,
                x="Month",
                y="Customers",
                title="Customers growth",
                markers=True)
line_chart.show()
# Calculate profit
# Profit = Revenue - Expenses
# and visualize monthly profit.

revenue_df["Profit"]= revenue_df["Revenue"]-revenue_df["Expenses"]
# print(revenue_df)
line_chart = px.line(
                revenue_df,
                x="Month",
                y="Profit",
                title="Profit profit",
                markers=True)
line_chart.show(renderer="browser")

bar_chart = px.bar(
                revenue_df,
                x="Month",
                y="Profit",
                title="Profit profit",
               )
bar_chart.show(renderer="browser")
import plotly.graph_objects as go
fig = go.Figure()

# Revenue
fig.add_trace(
    go.Scatter(
        x=revenue_df["Month"],
        y=revenue_df["Revenue"],
        mode="lines+markers",
        name="Revenue",
        line=dict(color="blue", width=3)
    )
)

# Expenses
fig.add_trace(
    go.Scatter(
        x=revenue_df["Month"],
        y=revenue_df["Expenses"],
        mode="lines+markers",
        name="Expenses",
        line=dict(color="red", width=3)
    )
)

# Profit
fig.add_trace(
    go.Bar(
        x=revenue_df["Month"],
        y=revenue_df["Profit"],
        name="Profit",
        marker_color="green"
    )
)

fig.update_layout(
    title="E-Commerce Performance Dashboard",
    xaxis_title="Month",
    yaxis_title="Amount (₹)",
    template="plotly_white",
    hovermode="x unified"
)

fig.show(renderer="browser")