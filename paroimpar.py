def evalucacionNumero(numero):
    if numero == 10:
        print("el numero ingresado es 10") 
    elif numero == 7:
        print("se ha ingresado un comodin")
    elif numero % 2 == 0:
        print("el numero ingresado es par")
    else:
        print("el numero ingresado es impar")
    
def main():
    numero = int(input("ingrese un numero"))
    evalucacionNumero(numero)
    
if __name__ == "__main__":
    main()
    