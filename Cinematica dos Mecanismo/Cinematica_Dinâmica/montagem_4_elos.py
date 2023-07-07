#Aline Mariana - 
class GLD:
    def __init__(self, elos):

        self.elos = sorted(elos) #Ordenar os elos pelo Comprimento

    ######################################

        self.a = int(elos[0])  # manivela
        self.b = int(elos[1])  # acoplador
        self.c = int(elos[2]) # seguidor
        self.d = int(elos[3])  # elo terra

     #########################################

        self.S = int(self.elos[0])
        self.L = int(self.elos[3])
        self.P = int(self.elos[1])
        self.Q = int(self.elos[2])

    def Sistema(self):
        if (self.L) > (self.S + self.P + self.Q):
            print("Sistema : Montagem Pré Carregada")
        elif (self.L == (self.S + self.P + self.Q)):
            print("Sistema: Montagem Estrutura ")
        elif (self.L < (self.S + self.P + self.Q)):
            print("Sistema : Montagem Mecanismo")

    def Grashof(self):
        if((int(self.S) + int(self.L)) < (int(self.P) + int(self.Q))):
            print("CLASSE I")
            if ((self.S == self.a) or (self.S == self.c)):
                print("Tipo : Manivela Seguidor")
            elif(self.S == self.b):
                print("Tipo: Duplo Seguidor de Grashof")
            else:
                print("Tipo : Dupla Manivela")
        if((int(self.S) + int(self.L)) > (int(self.P) + int(self.Q))):
            print("CLASSE II")
            print("Tipo : Triplo Seguidores")
        if((int(self.S) + int(self.L)) == (int(self.P) + int(self.Q))):
            print("CLASSE III")
            if ((self.S == self.a) or (self.S == self.c)):
                print("Tipo : Caso Especial Manivela Seguidor")
            elif(self.S == self.b):
                print("Tipo: Caso Especial Duplo Seguidor ")
            else:
                print("Tipo : Caso Especial Dupla Manivela")

    def Gruebler(self, E, J, G):
        return ((3*E)-(2*J)-(3*G))
    
    def Verificar(self):
        print("S: ",self.S )
        print("L: ",self.L )
        print("P: ",self.P )
        print("Q: ",self.Q )


    def Analise(self):
      print("Analise: ")
      self.Sistema()
      self.Grashof()
      self.Verificar()


i = 1
while i == 1:
    print("\n Comprimento dos Elos:  ")
    a = input("C-Elo1: ")
    b = input("C-Elo2: ")
    c = input("C-Elo3: ")
    d = input("C-Elo4: ")
    print("\n Analisando a Montagem......")
    teste = GLD([a, b, c, d])
    teste.Analise()

    i = int(input("\n Fazer uma nova Analise? S-1/ N - 0: "))

print("Programa Finalizado")