import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# --- 1. SET UP THE FICTIONAL CORPORATION DATA ---
np.random.seed(88)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Revenue: Upward trend with a holiday surge
revenue = [120000, 135000, 140000, 155000, 150000, 165000, 170000, 168000, 180000, 195000, 210000, 245000]

# Expenses: Scaled growth with typical operational overhead
expenses = [95000, 102000, 105000, 110000, 108000, 115000, 118000, 120000, 122000, 130000, 135000, 150000]
expense_categories = ['R&D', 'Sales & Marketing', 'Operations', 'HR & Admin', 'Cloud Infrastructure']
expense_shares = [35, 25, 20, 12, 8] # Percentage split of the total budget

# Customers: Cumulative active subscribers vs new signups
new_customers = [450, 520, 490, 610, 580, 670, 710, 690, 800, 850, 920, 1100]
total_subscribers = np.cumsum(new_customers) - np.array([50, 120, 200, 310, 450, 580, 700, 850, 990, 1150, 1320, 1500]) # factoring churn

# Employees: Departmental headcount distribution
departments = ['Engineering', 'Product & Design', 'Sales', 'Customer Success', 'G&A']
headcount = [45, 18, 32, 25, 12]


# --- 2. CREATE A 2x2 METRICS GRID DASHBOARD ---
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "📈 Financial Trajectory (Revenue vs Expenses)",
        "🍰 Operational Expenses Breakdown",
        "👥 Customer Base Scale",
        "📊 Staff Allocation by Department"
    ),
    specs=[[{"type": "xy"}, {"type": "domain"}],
           [{"type": "xy"}, {"type": "xy"}]],
    vertical_spacing=0.15,
    horizontal_spacing=0.12
)

# Chart 1: Revenue vs Expenses (Line + Area Combination)
fig.add_trace(
    go.Scatter(x=months, y=revenue, name="Revenue", mode='lines+markers', line=dict(color='#00CC96', width=3)),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=months, y=expenses, name="Expenses", mode='lines', fill='tozeroy', line=dict(color='#EF553B', width=2)),
    row=1, col=1
)

# Chart 2: Expenses Structure (Donut Chart)
fig.add_trace(
    go.Pie(labels=expense_categories, values=expense_shares, name="Expenses Type", hole=0.4,
           marker=dict(colors=['#636EFA', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692'])),
    row=1, col=2
)

# Chart 3: Customer Growth Metrics (Dual Axis Bar + Line)
fig.add_trace(
    go.Bar(x=months, y=new_customers, name="New Signups", marker_color='#17BECF', opacity=0.7),
    row=2, col=1
)
# Overlaid trace using a secondary tracking logic mapped on standard subplots
fig.add_trace(
    go.Scatter(x=months, y=total_subscribers, name="Total Active Base", mode='lines', line=dict(color='#19D3F3', dash='dot')),
    row=2, col=1
)

# Chart 4: Employee Demographics (Horizontal Bar Chart)
fig.add_trace(
    go.Bar(x=headcount, y=departments, name="Headcount", orientation='h', marker_color='#333F48'),
    row=2, col=2
)


# --- 3. UNIFIED STYLING AND WINDOW RESOLUTION ---
fig.update_layout(
    title_text="Fictional Corp: Annual Executive Dashboard",
    title_font_size=22,
    title_x=0.5,
    height=800,
    width=1000,
    template="plotly_white",
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.12, xanchor="center", x=0.5)
)

# Clean up axes system specifics
fig.update_xaxes(title_text="Timeline", row=1, col=1)
fig.update_yaxes(title_text="Amount ($)", row=1, col=1)
fig.update_xaxes(title_text="Timeline", row=2, col=1)
fig.update_yaxes(title_text="User Count", row=2, col=1)
fig.update_xaxes(title_text="Employee Count", row=2, col=2)

fig.show(renderer="browser")
