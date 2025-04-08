"""This is a simple project meant to display simple string and input manipulations. 
Nothing crazy, just a simple user input based string project.
    Concepts used here include: 
        1. Concatenation
        2. New lines
        3. Simple string variable usage

    Future additions to consider:
        1. Potentially use a DB file to upload a selection of words for the user to pick from a menu.
        2. Implement a switch case to allow users to select what type of name they want to generate. 
        3. Add a front-end to the code to display the project with proper HTML objects such as buttons and drop downs.
 """

print("Welcome, this is a simple brand name generator tool.")
town = input("What is the name of the city you grew up in?\n")
pet = input("What is your pets name?\n")
print("Congratulations your brand shall be called: " + town + " " + pet + "!")