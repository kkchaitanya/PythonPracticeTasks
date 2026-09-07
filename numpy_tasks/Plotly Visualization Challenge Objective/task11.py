# NumPy + Plotly
# Generate 100 random numbers using NumPy and visualize them with Plotly.

import plotly.express as px
import numpy as np

# 1. Generate 100 random numbers from a standard normal distribution
np.random.seed(42)
random_data = np.random.standard_normal(100)

# 2. Visualize the distribution with a Plotly Histogram
fig = px.histogram(
    x=random_data,
    nbins=15,
    title="Distribution of 100 Random Numbers (NumPy + Plotly)",
    labels={'x': 'Generated Value'},
    color_discrete_sequence=['#636EFA']
)

# 3. Clean up layout styling
fig.update_layout(
    yaxis_title="Count",
    plot_bgcolor='white',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray')
)

fig.show(renderer="browser")
