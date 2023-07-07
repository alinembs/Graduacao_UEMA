import numpy as np
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


def analise_posicoes(theta2i, a, b, c, d, i):

    if i == 0:
        theta2 = np.deg2rad(theta2i)
    elif i == 1:
        theta2 = theta2i

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

    theta3a = np.arctan2(Bya-Ay, Bxa-Ax)
    theta4a = np.arctan2(Bya, Bxa-d)

    theta3c = np.arctan2(Byc-Ay, Bxc-Ax)
    theta4c = np.arctan2(Byc, Bxc-d)

    return O2, A1, B1a, O4, theta3a, theta4a,theta3c,theta4c


