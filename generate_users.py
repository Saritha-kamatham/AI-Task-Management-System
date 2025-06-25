import random
import pandas as pd
from faker import Faker

fake = Faker()

skill_levels = [1, 2, 3, 4, 5]
preferred_task_types = ["Technical", "Research", "Admin", "Support"]

def generate_user_data(num_users):
    users = []
    for user_id in range(1, num_users + 1):
        avg_completion = round(random.uniform(1, 5), 2)
        current_workload = round(random.uniform(1, 5), 2)
        user = {
            "User_ID": f"U{user_id:02d}",
            "Skill_Level": random.choice(skill_levels),
            "Avg_Completion_Time": f"{avg_completion} hrs",
            "Tasks_Completed": random.randint(50, 100),
            "Current_Workload": f"{current_workload} hrs",
            "Preferred_Task_Type": random.choice(preferred_task_types),
            "Performance_Score": round(random.uniform(0.5, 1), 2)
        }
        users.append(user)
    return pd.DataFrame(users)

# Generate and save
df = generate_user_data(10)
df.to_csv("user_behavior_profile.csv", index=False)
print("✅ user_behavior_profile.csv created.")
