name = "Chintan Sandesara"
age = 34  # I am getting old
height = round(76.8)  # Using round() function to round off height in inches.
weight = 197
eyes = "Brown"
teeth = "white"
hair = "black"
# Using the round() function, with calculations within it (yet to understand details), to round off height in cms.
height_cm = round(height / 0.39370)
# Using the round() function, with calculations within it (yet to understand details), to round off weight in kgs.
weight_kg = round(weight / 2.2046)


print(f"Let's talk about {name}.")
print(f"He's {height} inches, or {height_cm} centimeters tall.")
print(f"He's {weight} pounds, or {weight_kg} kilograms heavy.")
print("Actually that is not too heavy.")
print(f"He's got {eyes} eyes, and {hair} hair.")
print(f"He's teeth are usually {teeth} color, depending on the coffee.")

#This line is tricky, so hopefully I got it right.

total = age + height_cm + weight_kg
print(f"If I add {age}, {height} and {weight}, I get {total}.")
