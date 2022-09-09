name = input("Qual seu nome? ")

if name == "João":
    status = input(f"Olá {name}, tudo bem com você? ")
    if status == "Sim":
        print("Ainda bem!")
    else:
        print("Que pena, espero que melhore...")
else:
    print(f"Olá {name}, é a sua primeira vez acessando esta máquina?")