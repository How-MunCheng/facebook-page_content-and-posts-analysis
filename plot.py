import os
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")
os.makedirs("figures", exist_ok=True)

df = pd.read_csv("facebook_post.csv")

# ---- TIMESTAMP HANDLING ----
if "Timestamptimestamp" in df.columns:
    # UNIX seconds (NOT ms in your sample)
    df["dt"] = pd.to_datetime(df["Timestamptimestamp"], unit="s", errors="coerce")
elif "Timetime" in df.columns:
    df["dt"] = pd.to_datetime(df["Timetime"], errors="coerce")
else:
    raise ValueError("No timestamp column found")

df = df.dropna(subset=["dt"])

# ---- WEEKLY AGGREGATION ----
weekly = df.set_index("dt").resample("W").size()

# ---- PLOT ----
plt.figure(figsize=(14,6))
weekly.plot(kind="bar")

plt.xlabel("Week")
plt.ylabel("Number of Posts")
plt.title("Weekly Posting Activity")

# FIX: rotate labels vertically
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig("figures/weekly_posting_activity.png", dpi=200)
plt.show()
