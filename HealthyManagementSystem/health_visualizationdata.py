import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------- LOAD DATASET --------------------
data = pd.read_csv("health_dataset.csv")

# -------------------- USER INPUT --------------------
name = input("Enter candidate name: ")
age = int(input("Enter age: "))
height = float(input("Enter height (cm): "))
weight = float(input("Enter weight (kg): "))

# -------------------- BMI CALCULATION --------------------
bmi = weight / ((height / 100) ** 2)

# Exercise recommendation
if bmi < 18.5:
    user_ex = 20
elif bmi < 25:
    user_ex = 35
else:
    user_ex = 50

# -------------------- 1. COMPARISON (BAR CHART) --------------------
plt.figure(figsize=(6,4))
plt.bar(["Age", "Height", "Weight"], [age, height, weight])
plt.title(f"Comparison for {name}")
plt.show()

# -------------------- 2. COMPOSITION (PIE CHART) --------------------
plt.figure(figsize=(5,5))
plt.pie(
    [age, height, weight],
    labels=["Age", "Height", "Weight"],
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Body Composition")
plt.show()

# -------------------- 3. TREND (LINE CHART) --------------------
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
activity = np.random.randint(20, 60, size=5)

plt.figure(figsize=(6,4))
plt.plot(days, activity, marker='o')
plt.title("Weekly Activity Trend")
plt.ylabel("Minutes")
plt.show()

# -------------------- 4. DISTRIBUTION (HISTOGRAM) --------------------
plt.figure(figsize=(6,4))
plt.hist(activity, bins=5)
plt.title("Activity Distribution")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.show()

# -------------------- 5. RELATIONSHIP (SCATTER using DATASET) --------------------
plt.figure(figsize=(6,4))
plt.scatter(data["Age"], data["Weight_kg"])
plt.title("Age vs Weight (Dataset)")
plt.xlabel("Age")
plt.ylabel("Weight (kg)")
plt.show()

# -------------------- FINAL EXERCISE VIEW --------------------
# Choose font color
if user_ex >= 45:
    text_color = "red"
elif user_ex >= 30:
    text_color = "orange"
else:
    text_color = "green"

plt.figure(figsize=(6,3))
plt.text(
    0.5, 0.5,
    "🏃 RUNNING\n45+ mins/day and Do Yoga for 10 mins\n Drink more water\n Recommending to eat early morning banana, peanuts and milk\n Before and after exercise" if user_ex >= 45 else
    "🚶 WALKING\n30–40 mins/day\n Drink water and eat dal rice\n Recommending intake more food\n Sleep well at least 8 hours" if user_ex >= 30 else
    "🧍 LIGHT ACTIVITY\n20 mins/day\n Sleep well",
    fontsize=24,
    ha='center',
    va='center',
    color=text_color   # 👈 dynamic color
)
plt.axis('off')
plt.title(f"Exercise Recommendation for {name}")
plt.show()


