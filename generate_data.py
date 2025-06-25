import random
import pandas as pd
from faker import Faker
from datetime import timedelta

# Initialize Faker
fake = Faker()

categories = ["Feature", "Bug", "Improvement"]
priorities = ["Low", "Medium", "High"]
classes = ["Research", "Admin", "Technical", "Support"]

def generate_task_data(num_tasks):
    tasks = []
    for task_id in range(1, num_tasks + 1):
        created_date = fake.date_this_year(before_today=True, after_today=False)
        deadline = pd.to_datetime(created_date) + timedelta(days=random.randint(1, 10))
        est_hours = round(random.uniform(1, 10), 2)
        task = {
            "Task_ID": task_id,
            "Task_Description": fake.sentence(nb_words=6),
            "Created_Date": created_date,
            "Deadline": deadline,
            "Est. Hours": est_hours,
            "Category": random.choice(categories),
            "Priority": random.choice(priorities),
            "Class": random.choice(classes),
            "Assigned_To": f"U{random.randint(1, 10):02d}"
        }
        tasks.append(task)
    return pd.DataFrame(tasks)

# Generate and save
df = generate_task_data(20000)
df.to_csv("synthetic_task_data.csv", index=False)
print("✅ synthetic_task_data.csv created.")
