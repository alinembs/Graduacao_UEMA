import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cmath

# Codigo Feito por Aline Mariana - UEMA/ENG COMP

def Sistema(L, S, P, Q):

    if (L) > (S + P + Q):
        print("Sistema : Montagem Pré Carregada")
    elif (L == (S + P + Q)):
        print("Sistema: Montagem Estrutura ")
    elif (L < (S + P + Q)):
        print("Sistema : Montagem Mecanismo")


def Grashof(L, S, P, Q, a, b, c, d):

    if(S + L < P + Q):
        print("CLASSE I")
        if ((S == a) or (S == c)):
            print("Tipo : Manivela Seguidor")
        elif(S == b):
            print("Tipo: Duplo Seguidor de Grashof")
        else:
            print("Tipo : Dupla Manivela")
    if(S + L > P + Q):
        print("CLASSE II")
        print("Tipo : Triplo Seguidores")
    if(S + L == P + Q):
        print("CLASSE III")
        if ((S == a) or (S == c)):
            print("Tipo : Caso Especial Manivela Seguidor")
        elif(S == b):
            print("Tipo: Caso Especial Duplo Seguidor ")
        else:
            print("Tipo : Caso Especial Dupla Manivela")


def Gruebler(E, J, G):

    return ((3*E)-(2*J)-(3*G))


def analise_posicoes(theta2i, a, b, c, d, i,p1,W2,delta3):

    
    delta2 = np.deg2rad(15)
    delta4 = np.deg2rad(-10)
    s1 = 12
    u1 = 10

    if i == 0:
        theta2 = np.deg2rad(theta2i)
       
    elif i == 1:
        theta2 = theta2i
        W2 = W2 + theta2
    O2 = [0, 0]
    O4 = [d, 0]

    # Ponto A
    Ax = a * np.cos(theta2)
    Ay = a * np.sin(theta2)

    A1 = [Ax, Ay]

    # Ponto B

    S = (a**2-b**2+c**2-d**2)/(2*(Ax - d))
    P = (Ay**2) / ((Ax - d)**2) + 1
    Q = 2 * Ay * (d - S) / (Ax - d)
    R = (d - S)**2 - c**2

    #raiz = cmath.sqrt(Q**2 - 4 * P * R)
    raiz = np.sqrt(Q**2 - 4 * P * R)
    Bya = (-Q + raiz)/(2*P)
    Byc = (-Q - raiz)/(2*P)

    Bxa = S - (Ay * Bya) / (Ax - d)

    Bxc = S - (Ay * Byc) / (Ax - d)

    B1a = [Bxa, Bya]
    B1c = [Bxc, Byc]



    # CALCULO DE THETA 3 E THETA 4

    theta3 = np.arctan2(Bya-Ay, Bxa-Ax)
    theta4 = np.arctan2(Bya, Bxa-d)

    theta3c = np.arctan2(Byc-Ay, Bxc-Ax)
    theta4c = np.arctan2(Byc, Bxc-d)


     # Localização dos Pontos de Interesse

    ps1 = [np.cos(theta2 + delta2), np.sin(theta2 + delta2)]
    pp1 = [np.cos(theta3 + delta3), np.sin(theta3 + delta3)]
    pu1 = [np.cos(theta4+delta4), np.sin(theta4+delta4)]
    RS = []
    PS = []
    US = []
    for i in range(2):
        RS.append(s1*ps1[i])
        PS.append(A1 + p1 * pp1[i])
        US.append(O4 + u1 *pu1[i])
    # VELOCIDADE ANGULARES

    W3 = (a/b) * W2 * (np.sin(theta4 - theta2) / np.sin(theta3 - theta4))
    W4 = (a/c) * W2 * (np.sin(theta2 - theta3) / np.sin(theta4 - theta3))

    # VELOCIDADE LINEARES

    VA = []
    VBA = []
    VB = []
    W2i = [-np.sin(theta2), np.cos(theta2)]
    W3i = [-np.sin(theta3), np.cos(theta3)]
    W4i = [-np.sin(theta4), np.cos(theta4)]

    for i in range(2):

        VA.append(a * W2 * W2i[i])
        VBA.append(b * W3 * W3i[i])
        VB.append(c * W4 * W4i[i])

    # VELOCIDADE DOS PONTOS DE INTERESSE

    VS = []
    VU = []
    VPA = []
    W2i2 = [-np.sin(theta2 + delta2), np.cos(theta2 + delta2)]
    W3i2 = [-np.sin(theta4 + delta4), np.cos(theta4 + delta4)]
    W4i2 = [-np.sin(theta3 + delta3), np.cos(theta3 + delta3)]

    for i in range(2):

        VS.append(s1 * W2 * W2i2[i])
        VU.append(u1 * W4 * W3i2[i])
        VPA.append(p1 * W3 * W4i2[i])

    VP = VA + VPA

    return VP,W3,W4


print("\n Cinemtatica dos Mecanismo - Analise de Velocidade ")
print("\n Comprimento dos Elos:  ")
a = float(input("Elo 2 - Manivela: "))
b = float(input("Elo 3 - Acoplador: "))
c = float(input("ELo 4 - Seguidor: "))
d = float(input("ELo 1 - Terra : "))
theta2incial = int(input("Theta 2 em Graus:"))
w22incial = int(input("Velocidade angular 2 em Graus:"))
delta3 = int(input("Delta 3 em Graus:"))
Rpa = float(input("Valor de RPA:"))

#theta2 = int(input("Valor de Theta2: "))
print("\n Analisando a Montagem e Condições de Grashoff e Fazendo a Analise de Velocidade......")
elos = [a, b, c, d]
elos = sorted(elos)  # Ordenar os elos pelo Comprimento
S = float(elos[0])
L = float(elos[3])
P = float(elos[1])
Q = float(elos[2])
Sistema(L, S, P, Q)

Grashof(L, S, P, Q, a, b, c, d)

escolha = int(input("Gerar Grafico - 1 ou Resultado - 2:"))

matriz = {'W3':[],'W4':[]}



if escolha == 2:
    

    for time in np.arange(0, 2*np.pi, 0.1):
        VP,W3,W4 = analise_posicoes(time, a, b, c, d, 0,Rpa,w22incial,delta3)
        matriz["W3"].append(W3)
        matriz["W4"].append(W4)


    t = np.arange(0, 2*np.pi, 0.1)
    plt.plot(t,matriz['W3'],'g-', label = 'W3')
    plt.plot(t,matriz['W4'],'y-', label = 'W4')
    plt.ylabel('VELOCIDADE ANGULAR')
    plt.xlabel("Tempo")
    plt.title("Cinematica dos Mecanismo - 4 Barras")
    plt.legend()
    plt.show()
    
if escolha == 1:
    VP,W3,W4 = analise_posicoes(theta2incial, a, b, c, d, 0,Rpa,w22incial,delta3)

    print("W3: ",W3)
    print("W4:", W4)
    print("VP: ",np.linalg.norm(VP))

print("Programa Finalizado")





