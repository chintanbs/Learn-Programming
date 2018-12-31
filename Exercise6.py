#This line declares a variable types_of_people and assigns it a numeric value.
types_of_people = 10
#This line declares a variable x, and assigns it a value in the form of a formatted string, with the prior variable "types_of_people" embedded in it.
x = f"There are {types_of_people} types of people."

#The lines below declare three variables, i.e. "binary", "do_not" and "y", and assigns them values either in the form of a string,
#or in the form of a formatted string, with the first two variables "binary" and "do_not"embedded in it.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#The lines below print variables declared in the previous lines, i.e. "x" & "y". They will print the strings taking into considerations the formatting that
#has been programmed in the earlier variables.
print(x)
print(y)

#The lines below print variables declared in the previous lines, i.e. "x" & "y". They will print the strings taking into considerations the formatting that
#has been programmed in the earlier variables, along with the formatting written in the print statements on these lines themselves.
print(f"I said: {x}")
print(f"I also said: '{y}'")

#This line declares a variable hilarious and assigns it a boolean value.
hilarious = False

#This line declares a variable joke_evaluation and assigns it a value in the form of a string.
joke_evaluation = "Isn't that joke so funny?! {}"

#This line prints the string, based on the formatting assigned in the variables hilarious and joke_evaluation, as well print the boolean value assigned
#to the variable hilarious.
print(joke_evaluation.format(hilarious))

#The lines declare two variables, i.e. w and e, and assign them values in the form of a string.
w = "This is left side of..."
e = "a string with a right side."

#This line prints the strings that are assigned to variables w & e, along with concatenating the two strings assigned to the two variables,
#using the operator "+".
print(w + e)



