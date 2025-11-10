
nathan_og = {
    "id":"1234",
    "username":"nicartan",
    "kills":200,
    "death":500,
    "matches":700

}

print(nathan_og)
print(f"The id for nathan og is {nathan_og['id']}")
print(f"The username for nathan og is {nathan_og['username']}")
print(f"The username for nathan og is {nathan_og.get("username")}")

print("Changing the username")
nathan_og["username"] = "yolo"
print(nathan_og)

print("Add another key")
nathan_og["spawn"] = 20
print(nathan_og)