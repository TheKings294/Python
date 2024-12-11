def StartConvertisseur():
    print("Bienvenido sur le convertisseur")
    print("\n")
    print("Option 1 : € -> $ (1)\nOption 2 : °C -> °F (2)\nOption 3 : Km -> M (3)\n")
    print("Que choisiez vous : ")

def Convertisseur(Input, InputValue):
    if Input == 1 and isinstance(InputValue, int):
        print(InputValue * 1.0494)
        return InputValue * 1.0494
    elif Input == 2 and isinstance(InputValue, float):
        return (InputValue * 9 / 5) + 32
    elif Input == 3 and isinstance(InputValue, float):
        return InputValue * 0,621371
    else:
        return "Cette opération n'existe pas"

StartConvertisseur()
UserInput = int(input())
if UserInput == 1:
    UserInputValue = int(input("Quelle est la valeur : "))
elif UserInput == 2:
    UserInputValue = float(input("Quelle est la valeur : "))
elif UserInput == 3:
    UserInputValue = float(input("Quelle est la valeur : "))

print(Convertisseur(UserInput, UserInputValue))

