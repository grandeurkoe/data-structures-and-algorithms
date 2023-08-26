def scream():
    """Prints Ahhhhhhhh!!!! on the console."""
    print("Ahhhhhhhh!!!!")


user = {"Name": "Meowya", "Age": 54, "Magic": True, "Scream": scream, "Spell": "Avada Kedavra"}

# Time Complexity - O(1)
print(user)
# Time Complexity - O(1)
user["Scream"]()
