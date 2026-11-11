users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]

print("Total users:", len(users))
print("First user:", users[0])

users.append("visual_user")
print("Total users now:", len(users))


for user in users:
    if user == "locked_out_user":
        print(user, "→ should be BLOCKED")
    else:
        print(user, "→ should LOGIN")