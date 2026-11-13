import pandas as pd
import numpy as np

# Set seed for reproducibility in class
np.random.seed(42)
n_days = 100

# Generate predictor variables
new_snow_in = np.random.exponential(scale=3, size=n_days).round(1)
is_weekend = np.random.choice([0, 1], size=n_days, p=[5/7, 2/7])
promo_sent = np.random.choice([0, 1], size=n_days, p=[0.6, 0.4])
temp_f = np.random.normal(loc=25, scale=8, size=n_days).round(1)

# Underlying true model: 
# Base: 500 tickets
# + 45 per inch of snow
# + 350 for weekends
# + 120 for promo emails
# - 3 per degree F (colder is slightly better for snow conditions/perception)
error = np.random.normal(0, 60, n_days)
tickets_sold = 500 + (45 * new_snow_in) + (350 * is_weekend) + (120 * promo_sent) - (3 * temp_f) + error

df = pd.DataFrame({
    'tickets_sold': tickets_sold.astype(int),
    'new_snow_in': new_snow_in,
    'is_weekend': is_weekend,
    'promo_sent': promo_sent,
    'temp_f': temp_f
})

# Save to CSV for students
df.to_csv("ski_resort_demand.csv", index=False)