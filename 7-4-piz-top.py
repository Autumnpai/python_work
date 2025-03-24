prompt = "Enter a pizza topping."
prompt += "\n(Enter 'quit' when you are finished.): "
msg = ""
while msg != "quit":
    msg = input(prompt)
    if msg != "quit":
        print("I will add " + msg + " to your pizza.")