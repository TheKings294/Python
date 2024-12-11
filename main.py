def PrintHello(hello):
    if hello == "bonjour":
        print("bonjour c'est du francais")
    elif hello == "hello":
        print("hello c'est de l anglais")
    else:
        print("je ne connais pas")


bonjour = input("Tapper bonjour dans une langue")
PrintHello(bonjour)