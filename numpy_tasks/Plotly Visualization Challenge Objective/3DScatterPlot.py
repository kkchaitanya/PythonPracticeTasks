import plotly.express as px
import pandas as pd
import numpy as np

# 1. Create a dummy dataset simulating the relationship
np.random.seed(42)
n_samples = 150

experience = np.random.uniform(0, 20, n_samples)
# Age generally correlates with experience
age = 22 + experience + np.random.normal(0, 2, n_samples) 
# Salary tends to scale with experience and age, plus some variance
salary = 45000 + (experience * 4500) + (age * 500) + np.random.normal(0, 12000, n_samples)
# Ensure data stays within realistic limits
age = np.clip(age, 21, 65)
salary = np.clip(salary, 30000, 200000)

df = pd.DataFrame({
    'Age': age.astype(int),
    'Years of Experience': experience.round(1),
    'Salary ($)': salary.astype(int)
})

# 2. Build the interactive 3D Scatter Plot
fig = px.scatter_3d(
    df, 
    x='Age', 
    y='Years of Experience', 
    z='Salary ($)',
    color='Salary ($)',          # Color gradient scales with income
    color_continuous_scale='Viridis',
    opacity=0.8,
    title="Employee Demographics: Age vs. Experience vs. Salary"
)

# 3. Enhance formatting
fig.update_layout(margin=dict(l=0, r=0, b=0, t=40))
fig.show(renderer="browser")
