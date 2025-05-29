import pandas as pd
import requests

# Part 1
url = ("https://api.open-meteo.com/v1/forecast?latitude=50.4547"
       "&longitude=30.5238&hourly=temperature_2m,wind_speed_10m&timezone=auto")

response = requests.get(url)
print("Status code:", response.status_code)

data = response.json()
print(data.keys())

# Part 2
df = pd.DataFrame(data['hourly'])
df['time'] = pd.to_datetime(df['time'])
print(df.head())

# Part 3
today = pd.to_datetime('today').normalize()
in_3_days = today + pd.Timedelta(days=3)

df_for_3_days = df[(df['time'] >= today) & (df['time'] < in_3_days)]

min_temp = df_for_3_days['temperature_2m'].min()
max_temp = df_for_3_days['temperature_2m'].max()
avg_temp = df_for_3_days['temperature_2m'].mean()

print(f"Minimum temperature for the next 3 days: {min_temp}°C")
print(f"Maximum temperature for the next 3 days: {max_temp}°C")
print(f"Average temperature for the next 3 days: {avg_temp}°C")

# Part 4
avg_wind_speed = df['wind_speed_10m'].mean()
df_check_wind_speed = df[df['wind_speed_10m'] > avg_wind_speed]
number_of_hours = df_check_wind_speed.shape[0]
print(f"Number of hours with wind speed above average: {number_of_hours}")