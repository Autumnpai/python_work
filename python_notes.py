# "cwd": "${fileDirname}"  // put this line into the .vscode/launch.json to set the working directory to the script's directory

# python automaticly create a variable "__name__", its value is __main__ if running it directly, or the file name without .py if imported.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
# The super() function 4 is a special function that allows you to call a method from the parent class. This line tells 
# Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that 
# method. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.