import tkinter as tk
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi 
from bson.objectid import ObjectId
from datetime import datetime
import bson

# Connect to MongoDB
uri = "mongodb+srv://priyankaparisa1998:Priyankanti@cluster0.7qp5tys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db =  client['fitness_tracking']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def insert_new_user():
    try:
        # Retrieve user input
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        name = name_entry.get()
        age = int(age_entry.get())
        height = int(height_entry.get())
        weight = int(weight_entry.get())
        fitness_goal = fitness_goal_entry.get()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values for age, height, and weight.")
        return

    # Insert new user
    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "profile": {
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "fitness_goal": fitness_goal
        }
    }
    db.users.insert_one(user_data)
    messagebox.showinfo("Success", "New user inserted successfully.")

def log_workout():
    try:
        # Retrieve user input
        user_id = ObjectId(user_id_entry.get())
        date = datetime.strptime(date_entry.get(), '%Y-%m-%d')
        workout_type = workout_type_entry.get()
        duration = int(duration_entry.get())
        calories_burned = int(calories_burned_entry.get())
        distance = float(distance_entry.get())
        notes = notes_entry.get()
    except (ValueError, bson.errors.InvalidId):
        messagebox.showerror("Error", "Invalid input. Please enter valid values.")
        return

    # Log workout
    workout_data = {
        "user_id": user_id,
        "date": date,
        "type": workout_type,
        "duration": duration,
        "calories_burned": calories_burned,
        "distance": distance,
        "notes": notes
    }
    db.workouts.insert_one(workout_data)
    messagebox.showinfo("Success", "Workout logged successfully.")

def set_fitness_goal():
    try:
        # Retrieve user input
        user_id = ObjectId(user_id_goal_entry.get())
        goal_type = goal_type_entry.get()
        target_value = int(target_value_entry.get())
        start_date = datetime.strptime(start_date_entry.get(), '%Y-%m-%d')
        end_date = datetime.strptime(end_date_entry.get(), '%Y-%m-%d')
    except (ValueError, bson.errors.InvalidId):
        messagebox.showerror("Error", "Invalid input. Please enter valid values.")
        return

    # Set fitness goal
    goal_data = {
        "user_id": user_id,
        "goal_type": goal_type,
        "target_value": target_value,
        "start_date": start_date,
        "end_date": end_date
    }
    db.goals.insert_one(goal_data)
    messagebox.showinfo("Success", "Fitness goal set successfully.")

def retrieve_workouts():
    try:
        user_id = ObjectId(user_id_workout_entry_op.get())
        workouts = db.workouts.find({"user_id": user_id})
        workout_info = ""
        for workout in workouts:
            workout_info += f"Date: {workout['date']}, Type: {workout['type']}, Duration: {workout['duration']} minutes, Calories Burned: {workout['calories_burned']}, Distance: {workout['distance']} km, Notes: {workout['notes']}\n"
        if workout_info:
            messagebox.showinfo("Workouts", workout_info)
        else:
            messagebox.showinfo("Workouts", "No workouts found for the user.")
    except bson.errors.InvalidId:
        messagebox.showerror("Error", "Invalid user ID.")

def delete_workouts():
    try:
        user_id = ObjectId(user_id_workout_entry_op.get())
        db.workouts.delete_many({"user_id": user_id})
        messagebox.showinfo("Success", "Workouts deleted successfully.")
    except bson.errors.InvalidId:
        messagebox.showerror("Error", "Invalid user ID.")

def retrieve_goals():
    try:
        user_id = ObjectId(user_id_goal_entry_op.get())
        goals = db.goals.find({"user_id": user_id})
        goal_info = ""
        for goal in goals:
            goal_info += f"Goal Type: {goal['goal_type']}, Target Value: {goal['target_value']}, Start Date: {goal['start_date']}, End Date: {goal['end_date']}\n"
        if goal_info:
            messagebox.showinfo("Goals", goal_info)
        else:
            messagebox.showinfo("Goals", "No goals found for the user.")
    except bson.errors.InvalidId:
        messagebox.showerror("Error", "Invalid user ID.")

def delete_goals():
    try:
        user_id = ObjectId(user_id_goal_entry_op.get())
        db.goals.delete_many({"user_id": user_id})
        messagebox.showinfo("Success", "Goals deleted successfully.")
    except bson.errors.InvalidId:
        messagebox.showerror("Error", "Invalid user ID.")

root = tk.Tk()
root.title("Fitness Tracking Application")

user_frame = tk.LabelFrame(root, text="Insert New User")
user_frame.grid(row=0, column=0, padx=10, pady=5)

username_label = tk.Label(user_frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")
username_entry = tk.Entry(user_frame)
username_entry.grid(row=0, column=1, padx=5, pady=2)

email_label = tk.Label(user_frame, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=2, sticky="e")
email_entry = tk.Entry(user_frame)
email_entry.grid(row=1, column=1, padx=5, pady=2)

password_label = tk.Label(user_frame, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=2, sticky="e")
password_entry = tk.Entry(user_frame, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=2)

name_label = tk.Label(user_frame, text="Name:")
name_label.grid(row=3, column=0, padx=5, pady=2, sticky="e")
name_entry = tk.Entry(user_frame)
name_entry.grid(row=3, column=1, padx=5, pady=2)

age_label = tk.Label(user_frame, text="Age:")
age_label.grid(row=4, column=0, padx=5, pady=2, sticky="e")
age_entry = tk.Entry(user_frame)
age_entry.grid(row=4, column=1, padx=5, pady=2)

height_label = tk.Label(user_frame, text="Height:")
height_label.grid(row=5, column=0, padx=5, pady=2, sticky="e")
height_entry = tk.Entry(user_frame)
height_entry.grid(row=5, column=1, padx=5, pady=2)

weight_label = tk.Label(user_frame, text="Weight:")
weight_label.grid(row=6, column=0, padx=5, pady=2, sticky="e")
weight_entry = tk.Entry(user_frame)
weight_entry.grid(row=6, column=1, padx=5, pady=2)

fitness_goal_label = tk.Label(user_frame, text="Fitness Goal:")
fitness_goal_label.grid(row=7, column=0, padx=5, pady=2, sticky="e")
fitness_goal_entry = tk.Entry(user_frame)
fitness_goal_entry.grid(row=7, column=1, padx=5, pady=2)

insert_user_button = tk.Button(user_frame, text="Insert User", command=insert_new_user)
insert_user_button.grid(row=8, columnspan=2, pady=5)

workout_frame = tk.LabelFrame(root, text="Log Workout")
workout_frame.grid(row=1, column=0, padx=10, pady=5)

user_id_label = tk.Label(workout_frame, text="User ID:")
user_id_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")
user_id_entry = tk.Entry(workout_frame)
user_id_entry.grid(row=0, column=1, padx=5, pady=2)

date_label = tk.Label(workout_frame, text="Date (YYYY-MM-DD):")
date_label.grid(row=1, column=0, padx=5, pady=2, sticky="e")
date_entry = tk.Entry(workout_frame)
date_entry.grid(row=1, column=1, padx=5, pady=2)

workout_type_label = tk.Label(workout_frame, text="Workout Type:")
workout_type_label.grid(row=2, column=0, padx=5, pady=2, sticky="e")
workout_type_entry = tk.Entry(workout_frame)
workout_type_entry.grid(row=2, column=1, padx=5, pady=2)

duration_label = tk.Label(workout_frame, text="Duration (minutes):")
duration_label.grid(row=3, column=0, padx=5, pady=2, sticky="e")
duration_entry = tk.Entry(workout_frame)
duration_entry.grid(row=3, column=1, padx=5, pady=2)

calories_burned_label = tk.Label(workout_frame, text="Calories Burned:")
calories_burned_label.grid(row=4, column=0, padx=5, pady=2, sticky="e")
calories_burned_entry = tk.Entry(workout_frame)
calories_burned_entry.grid(row=4, column=1, padx=5, pady=2)

distance_label = tk.Label(workout_frame, text="Distance (kilometers):")
distance_label.grid(row=5, column=0, padx=5, pady=2, sticky="e")
distance_entry = tk.Entry(workout_frame)
distance_entry.grid(row=5, column=1, padx=5, pady=2)

notes_label = tk.Label(workout_frame, text="Notes:")
notes_label.grid(row=6, column=0, padx=5, pady=2, sticky="e")
notes_entry = tk.Entry(workout_frame)
notes_entry.grid(row=6, column=1, padx=5, pady=2)

workout_button = tk.Button(workout_frame, text="Log Workout", command=log_workout)
workout_button.grid(row=7, columnspan=2, padx=5, pady=5)

goal_frame = tk.LabelFrame(root, text="Set Fitness Goal")
goal_frame.grid(row=0, column=1, padx=10, pady=5, rowspan=2)

user_id_goal_label = tk.Label(goal_frame, text="User ID:")
user_id_goal_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")
user_id_goal_entry = tk.Entry(goal_frame)
user_id_goal_entry.grid(row=0, column=1, padx=5, pady=2)

goal_type_label = tk.Label(goal_frame, text="Goal Type:")
goal_type_label.grid(row=1, column=0, padx=5, pady=2, sticky="e")
goal_type_entry = tk.Entry(goal_frame)
goal_type_entry.grid(row=1, column=1, padx=5, pady=2)

target_value_label = tk.Label(goal_frame, text="Target Value:")
target_value_label.grid(row=2, column=0, padx=5, pady=2, sticky="e")
target_value_entry = tk.Entry(goal_frame)
target_value_entry.grid(row=2, column=1, padx=5, pady=2)

start_date_label = tk.Label(goal_frame, text="Start Date (YYYY-MM-DD):")
start_date_label.grid(row=3, column=0, padx=5, pady=2, sticky="e")
start_date_entry = tk.Entry(goal_frame)
start_date_entry.grid(row=3, column=1, padx=5, pady=2)

end_date_label = tk.Label(goal_frame, text="End Date (YYYY-MM-DD):")
end_date_label.grid(row=4, column=0, padx=5, pady=2, sticky="e")
end_date_entry = tk.Entry(goal_frame)
end_date_entry.grid(row=4, column=1, padx=5, pady=2)

goal_button = tk.Button(goal_frame, text="Set Goal", command=set_fitness_goal)
goal_button.grid(row=5, columnspan=2, padx=5, pady=5)

workout_ops_frame = tk.LabelFrame(root, text="Workout Operations")
workout_ops_frame.grid(row=2, column=1, padx=10, pady=5)

user_id_workout_op_label = tk.Label(workout_ops_frame, text="User ID:")
user_id_workout_op_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")
user_id_workout_entry_op = tk.Entry(workout_ops_frame)
user_id_workout_entry_op.grid(row=0, column=1, padx=5, pady=2)

retrieve_workouts_button = tk.Button(workout_ops_frame, text="Retrieve Workouts", command=retrieve_workouts)
retrieve_workouts_button.grid(row=1, column=0, padx=5, pady=2)

delete_workouts_button = tk.Button(workout_ops_frame, text="Delete Workouts", command=delete_workouts)
delete_workouts_button.grid(row=1, column=1, padx=5, pady=2)

goal_ops_frame = tk.LabelFrame(root, text="Goal Operations")
goal_ops_frame.grid(row=3, column=0, padx=10, pady=5)

# Workout Operations Section
workout_ops_frame = tk.LabelFrame(root, text="Workout Operations")
workout_ops_frame.grid(row=2, column=1, padx=10, pady=5)

user_id_workout_op_label = tk.Label(workout_ops_frame, text="User ID:")
user_id_workout_op_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")
user_id_workout_entry_op = tk.Entry(workout_ops_frame)
user_id_workout_entry_op.grid(row=0, column=1, padx=5, pady=2)

retrieve_workouts_button = tk.Button(workout_ops_frame, text="Retrieve Workouts", command=retrieve_workouts)
retrieve_workouts_button.grid(row=1, column=0, padx=5, pady=2)

delete_workouts_button = tk.Button(workout_ops_frame, text="Delete Workouts", command=delete_workouts)
delete_workouts_button.grid(row=1, column=1, padx=5, pady=2)

# Main loop
root.mainloop()
