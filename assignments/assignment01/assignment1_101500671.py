"""
Author: <Lucas Tavares Criscuolo>
Student ID: 101500671
Assignment: #1
"""

# Basic details about a gym member
gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5  # float
highest_reps = 25  # integer
membership_active = True  # boolean

# Dictionary storing workout stats (yoga, running, weightlifting) for different friends
workout_stats = {
    "Lucas": (30, 45, 50),  # Lucas did 30 mins yoga, 45 mins running, 50 mins weightlifting
    "Matheus": (40, 30, 25),
    "Davi": (20, 35, 20),
    "Giovanna": (25, 25, 25),
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 25),
    "Taylor": (20, 35, 50)
}

# Calculate total minutes spent working out for each friend
total_minutes = {name: sum(times) for name, times in workout_stats.items()}

# Convert the workout data into a simple list format for easy processing
workout_list = list(workout_stats.values())

# Get only the yoga & running minutes for all friends
yoga_running_minutes = [times[:2] for times in workout_list]
print("Yoga & Running Minutes:", yoga_running_minutes)

# Get only the weightlifting minutes for the last two friends in the list
weightlifting_last_two = [times[2] for times in workout_list[-2:]]
print("Weightlifting Minutes (Last Two):", weightlifting_last_two)

# Let the user enter a friend's name to check their workout details
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    yoga, running, weightlifting = workout_stats[friend_name]
    print(
        f"{friend_name}'s Workout: Yoga: {yoga} min, Running: {running} min, Weightlifting: {weightlifting} min, Total: {total_minutes[friend_name]} min")

    # Check how much this friend worked out and encourage them
    if total_minutes[friend_name] >= 120:
        print(f"Great job staying active, {friend_name}!")
    else:
        print(f"Keep pushing, {friend_name}! You logged {total_minutes[friend_name]} minutes. Keep it up!")
else:
    print(f"Friend {friend_name} not found in the records.")

# Find the friend who worked out the most and the least
max_friend = max(total_minutes, key=total_minutes.get)
min_friend = min(total_minutes, key=total_minutes.get)

print(f"Friend with the highest workout minutes: {max_friend}")
print(f"Friend with the lowest workout minutes: {min_friend}")

