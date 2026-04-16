age = 25
has_license = True
drunk = True

# AND - both must be true
can_drive = age >= 16 and has_license and not drunk
print(can_drive)  # True

name= "Jayanthi"
string = f"Hi there, My name is {name}"

name.lower()
name.upper()

sentence = "hi my name is Dave"
sentence.title()

temperature = 32
if temperature > 30:
    print("Its very hot!")
elif temperature > 25:
    print("Its hot!")
else:
    print("Its nice weather!")



score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")


for i in range (5):
    print(i)

