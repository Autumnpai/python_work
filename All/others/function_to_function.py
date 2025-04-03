def greet():
    return "Hello!"

def execute_function(x=greet):
    print(greet())  # Call the passed function

execute_function()  # Pass the function object
# print(result)  # Output: Hello!