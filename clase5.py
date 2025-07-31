class numero:
    def __init__(self, numero):
        self.numero = numero

    def evaluarNumero(self):
        if self.numero & 1:
            print("impar")
            if self.numero == 7:
                print("\nEl numero ingresado es un comodin")
        else:
            print("Par")
            if self.numero == 10:
                print("\nEl numero ingresado es 10")
            
    def sumar(self,numeroasumar):
        return self.numero + numeroasumar
    
if __name__ == "__main__":
    numeroaevaluar = numero(7)
    numeroaevaluar.evaluarNumero()
    
    
   

    

         
