import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("cookie_performance.csv")

# roll_df = df.rolling(window=3).mean()  # Smoothing

x = df["Time Between Buys"].tolist()
plt.figure(figsize=(8, 6))

for column in df.columns[1:]:
    y = df[column].tolist()
    plt.plot(x, y, marker='o', linestyle='-', label=column)

# Labels and title
plt.xlabel("Time Between Buys (seconds)")
plt.ylabel("Cookies per Second")
plt.title("Cookie Clicker Performance Over Time")
plt.legend()
plt.grid(True)
plt.show()