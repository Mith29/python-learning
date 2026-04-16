def greet():
    print("Hello!")

greet()    


def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()

# parameter----
def greet(first_name = "John", last_name="Doe"):
    print(f"Hello, {first_name} {last_name}")

greet(first_name="Mithra")
greet("venu", "Mithra")


def add_print(a,b):
    return(a+b)

result = add_print(a=5, b=10)



def simple_function():
    numbers = [0,1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number,last_number

f,l = simple_function()
