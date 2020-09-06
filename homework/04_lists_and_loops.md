# lists and loops homework
## quadratic_lists.py
Refactor the `quadratic.py` file you previously created.
- Define a function `get_quadratic`, which prompts the user to input three variables and returns a list.
- Modify `solve_quadratic` to take a list as its only parameter and use that list.
- Modify your code so it no longer imports the math library.

## login_welcome.py
Make a list of five or more usernames, including the name `'admin'`. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
- If the username is `'admin'`, print a special greeting, such as *Hello admin, would you like to see a status report?*
- Otherwise, print a generic greeting, such as *Hello Eric, thank you for logging in again.*
- Add an `if` test to make sure the list of users is not empty.
- If the list is empty, print the message *We need to find some users!*

## username_check.py
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
- Make a list of five or more usernames called `current_users`.
- Make another list of five usernames called `new_users`. Make sure one or two of the new usernames are also in the `current_users` list.
- Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
- Make sure your comparison is case insensitive. If `'John'` has been used, `'JOHN'` should not be accepted

## favorite_fruits.py
Make a list of your favorite fruits, and then write a series of independent `if` statements that check for certain fruits in your list.
- Make a list of your three favorite fruits and call it `favorite_fruits`.
- Write five `if` statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the `if` block should print a statement, such as *You really like bananas!*

## days_of_week.py
Create a looping function that will populate a list to match the contents of an existing list of the days of the week (Monday to Sunday). For example output, see page 33 in the student book.

The function will:
- Ask the user for a day of the week.
- If correct, it will be added to the list.
- If the user adds an element twice, the user will be notified.
- If the inputted data does not match the existing list, the user will be notified.
- Run until the new list is correctly populated.
