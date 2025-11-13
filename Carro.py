class Veiculo:

    def __init__(self, cor, modelo):
        self.ligar = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
    
    def ligar_carro(self):
        ligo = input("Deseja ligar o carro: s/n: ")
        if ligo == "s":
            self.ligar = True
            resultado = print("O carro está ligado")
        if ligo == "n":
            self.ligar = False
            resultado = print("O carro se mantem desligado")
        print(self.ligar) 

    def movimentos(self):
        acelerar = input("Aperte W para andar com o carro")
        while acelerar == 'w':
            if acelerar == 'w':
                self.velocidade += 20
                print(f"Velocidade atual é de {self.velocidade}")
                acelerar = input("Para aumentar mais a velocidade aperte W novamente, diminuir aperte S: ")
            if acelerar == "s":
                self.velocidade -= 20
                print(f"Velocidade atual é de {self.velocidade}")
                if self.velocidade == 0:
                    print("Velocidade igual a 0")
            if self.velocidade <= 0:
                print("Veiculo parado")
    
        
    


carro = Veiculo(cor="", modelo="")
carro.ligar_carro()
carro.movimentos()