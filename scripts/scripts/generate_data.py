import pandas as pd
import random

cities = ["Delhi", "Mumbai", "Pune", "Bangalore", "Hyderabad"]
categories = ["Hospital", "Cafe", "School", "Gym", "Restaurant"]
sources = ["Google", "Justdial", "Sulekha"]

data = []

for i in range(1, 501):
    data.append({
        "business_name": f"Business_{i}",
        "category": random.choice(categories),
        "city": random.choice(cities),
        "address": f"Address {i}",
        "phone": f"98{random.randint(10000000,99999999)}",
        "source": random.choice(sources)
    })

df = pd.DataFrame(data)

df.to_csv("business_data.csv", index=False)

print("CSV Created Successfully!")