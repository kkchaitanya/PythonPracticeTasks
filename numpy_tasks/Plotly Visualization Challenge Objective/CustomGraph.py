import plotly.express as px
import pandas as pd
import numpy as np

# 1. Generate a realistic multi-variable EV dataset
np.random.seed(101)
n_vehicles = 100

# Battery sizes ranging from compact commuter cars to long-haul trucks
battery_kwh = np.random.uniform(40, 120, n_vehicles) 
# Vehicle driving range relies on battery scale multiplied by fluctuating efficiency rates
range_km = battery_kwh * np.random.uniform(4.5, 6.5, n_vehicles) 
# Base price determined by hardware costs, premium tech tiers, and a variance factor
base_price = 22000 + (battery_kwh * 550) + (range_km * 60) + np.random.normal(0, 7500, n_vehicles)
base_price = np.clip(base_price, 28000, 150000)
# Common drivetrain configurations
drivetrain = np.random.choice(['FWD (Front-Wheel Drive)', 'RWD (Rear-Wheel Drive)', 'AWD (All-Wheel Drive)'], 
                              n_vehicles, p=[0.2, 0.3, 0.5])

# Assemble our DataFrame
df_ev = pd.DataFrame({
    'Battery Capacity (kWh)': battery_kwh.round(1),
    'Driving Range (km)': range_km.round(0).astype(int),
    'Base Price ($)': base_price.round(-2).astype(int),
    'Drivetrain': drivetrain
})

# 2. Generate a highly expressive visual representation
fig = px.scatter(
    df_ev,
    x='Battery Capacity (kWh)',
    y='Driving Range (km)',
    size='Base Price ($)',          # Extra dimension: Larger bubbles = More expensive cars
    color='Drivetrain',            # Extra dimension: Easily separates layout distributions
    color_discrete_sequence=px.colors.qualitative.Bold,
    hover_name='Drivetrain',
    title='EV Market Matrix: Battery Capacity vs. Range vs. Base MSRP',
    labels={'Battery Capacity (kWh)': 'Battery Pack Size (kWh)', 'Driving Range (km)': 'Max Range (Kilometers)'}
)

# Improve overall layout formatting
fig.update_layout(
    legend_title_text='Drivetrain Type',
    plot_bgcolor='white',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray')
)

fig.show(renderer="browser")
