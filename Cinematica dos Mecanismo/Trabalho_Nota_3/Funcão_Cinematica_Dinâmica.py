import numpy as np
import cmath
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# Codigo Feito por Aline Mariana - UEMA/ENG COMP

def Sistema(L, S, P, Q):

    if (L) > (S + P + Q):
         return("Sistema : Montagem Pré Carregada"),0
    elif (L == (S + P + Q)):
        return("Sistema: Montagem Estrutura "),0
    elif (L < (S + P + Q)):
        return("Sistema : Montagem Mecanismo"),1


def Grashof(L, S, P, Q, a, b, c, d):

    if(S + L < P + Q):
        #print("CLASSE I")
        if ((S == a) or (S == c)):
            return("CLASSE I -> Tipo : Manivela Seguidor")
        elif(S == b):
            return("CLASSE I -> Tipo: Duplo Seguidor de Grashof")
        else:
            return("CLASSE I -> Tipo : Dupla Manivela")
    if(S + L > P + Q):
        #print("CLASSE II")
        return("CLASSE II -> Tipo : Triplo Seguidores")
    if(S + L == P + Q):
        return("CLASSE III")
        #if ((S == a) or (S == c)):
            #print("Tipo : Caso Especial Manivela Seguidor")
        #elif(S == b):
            #print("Tipo: Caso Especial Duplo Seguidor ")
        #else:
            #print("Tipo : Caso Especial Dupla Manivela")


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


    #Adicionar theta d usando a equação Freuedensteim

  
    # CALCULO DE THETA 3 E THETA 4

    theta3a = np.arctan2(Bya-Ay, Bxa-Ax)
    theta4a = np.arctan2(Bya, Bxa-d)
    gammaa = theta3a-theta4a
    theta3c = np.arctan2(Byc-Ay, Bxc-Ax)
    theta4c = np.arctan2(Byc, Bxc-d)
    gammac = theta3c-theta4c
    return O2, A1, B1a, O4, theta3a, theta4a,theta3c,theta4c,gammaa,gammac



def analise_ponto_p(a, b, c, d,delta3,e):

    ar = delta3*np.pi/180         # Radianos do ângulo de extensão do acoplador
    theta = np.arange(50, 411, 1)  # Ângulo inicial com limite de rotação 
    T = theta*np.pi/180          # Radianos do ângulo inicial
    #T = np.arange(0,2*np.pi,0.01)
    f = np.sqrt(a*a + d*d - 2*a*d*np.cos(T))

    # Seção 2: Cálculos
    #--------------------------------------------------------------------------
    # Ângulos e coordenadas da curva do acoplador
    G = np.arctan((a*np.sin(T))/(d - a*np.cos(T)))
    Bita = np.arccos((f*f + b*b - c*c)/(2*b*f)) - G

    # Coordenadas
    X = a*np.cos(T) + e*np.cos(ar + Bita)
    Y = a*np.sin(T) + e*np.sin(ar + Bita)
    return X,Y

def analise_velocidades(theta2i, a, b, c, d, i,p1,W2,delta3):

    
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

    W3c = (a/b) * W2 * (np.sin(theta4c - theta2) / np.sin(theta3c - theta4c))
    W4c = (a/c) * W2 * (np.sin(theta2 - theta3c) / np.sin(theta4c - theta3c))

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
    VPAc = []
    W2i2 = [-np.sin(theta2 + delta2), np.cos(theta2 + delta2)]
    W3i2 = [-np.sin(theta4 + delta4), np.cos(theta4 + delta4)]
    W4i2 = [-np.sin(theta3 + delta3), np.cos(theta3 + delta3)]
    W4i3 = [-np.sin(theta3c + delta3), np.cos(theta3c + delta3)]

    for i in range(2):

        VS.append(s1 * W2 * W2i2[i])
        VU.append(u1 * W4 * W3i2[i])
        VPA.append(p1 * W3 * W4i2[i])
        VPAc.append(p1 *W3c*W4i3[i])

    VP = VA + VPA
    Vpc = VA + VPAc
    return VP,W3,W4,W3c,W4c,Vpc



def analise_de_aceleracao(theta2i, a, b, c, d, i,p1,W2,delta3,alpha2):

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

    W3c = (a/b) * W2 * (np.sin(theta4c - theta2) / np.sin(theta3c - theta4c))
    W4c = (a/c) * W2 * (np.sin(theta2 - theta3c) / np.sin(theta4c - theta3c))
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
    VPAc = []
    W2i2 = [-np.sin(theta2 + delta2), np.cos(theta2 + delta2)]
    W3i2 = [-np.sin(theta4 + delta4), np.cos(theta4 + delta4)]
    W4i2 = [-np.sin(theta3 + delta3), np.cos(theta3 + delta3)]
    W4i3 = [-np.sin(theta3c + delta3), np.cos(theta3c + delta3)]

    for i in range(2):

        VS.append(s1 * W2 * W2i2[i])
        VU.append(u1 * W4 * W3i2[i])
        VPA.append(p1 * W3 * W4i2[i])
        VPAc.append(p1 *W3c*W4i3[i])

    VP = VA + VPA
    Vpc = VA + VPAc

    # Acelerações Angulares - ABERTO

    AA = c * np.sin(theta4)
    BB = b * np.sin(theta3)
    CC = a * alpha2 * np.sin(theta2)+a*(W2**2) * np.cos(theta2) + \
        b * (W3**2) * np.cos(theta3) - c * (W4**2) * np.cos(theta4)
    DD = c * np.cos(theta4)
    EE = b * np.cos(theta3)
    FF = a * alpha2 * np.cos(theta2)-a*(W2**2) * np.sin(theta2) - \
        b * (W3**2) * np.sin(theta3) + c * (W4**2) * np.sin(theta4)

    alpha3 = (CC * DD - AA * FF)/(AA * EE - BB * DD)
    alpha4 = (CC * EE - BB * FF)/(AA * EE - BB * DD)

     # Acelerações Angulares - CRUZADO

    AAc = c * np.sin(theta4c)
    BBc = b * np.sin(theta3c)
    CCc = a * alpha2 * np.sin(theta2)+a*(W2**2) * np.cos(theta2) + \
        b * (W3c**2) * np.cos(theta3c) - c * (W4c**2) * np.cos(theta4c)
    DDc = c * np.cos(theta4c)
    EEc = b * np.cos(theta3c)
    FFc = a * alpha2 * np.cos(theta2)-a*(W2**2) * np.sin(theta2) - \
        b * (W3c**2) * np.sin(theta3c) + c * (W4c**2) * np.sin(theta4c)

    alpha3c = (CCc * DDc - AAc * FFc)/(AAc * EEc - BBc * DDc)
    alpha4c = (CCc * EEc - BBc * FFc)/(AAc * EEc - BBc * DDc)


    # Acelerações Lineares - ABERTO

    ALA = [- a * alpha2*np.sin(theta2) - a * (W2**2)*np.cos(theta2),
           a * alpha2*np.cos(theta2) - a * (W2**2)*np.sin(theta2)]
    ALB = [c * alpha4 * np.sin(theta4) + c * (W4**2) * np.cos(theta4), -
           c * alpha4 * np.cos(theta4) + c * (W4**2) * np.sin(theta4)]

    ALBA = np.array(ALB) + np.array(ALA)
    ALBA = list(ALBA)

     # Acelerações Lineares - CRUZADO

    ALAc = [- a * alpha2*np.sin(theta2) - a * (W2**2)*np.cos(theta2),
           a * alpha2*np.cos(theta2) - a * (W2**2)*np.sin(theta2)]
    ALBc = [c * alpha4 * np.sin(theta4c) + c * (W4c**2) * np.cos(theta4c), -
           c * alpha4 * np.cos(theta4c) + c * (W4c**2) * np.sin(theta4c)]

    ALBAc = np.array(ALBc) - np.array(ALAc)
    ALBAc = list(ALBAc)

    # ACELERAÇÃO NO PONTOS DE INTERESSES - ABERTO

    AS = []
    AU = []
    APA = []

    pr1 = [np.sin(theta2 + delta2), np.cos(theta2+delta2)]
    pi1 = [np.cos(theta2+delta2), np.sin(theta2+delta2)]
    pr2 = [-np.sin(theta4 + delta4), np.cos(theta4+delta4)]
    pi2 = [np.cos(theta4+delta4), np.sin(theta4+delta4)]
    pr3 = [-np.sin(theta3 + delta3), np.cos(theta3+delta3)]
    pi3 = [np.cos(theta3+delta3), np.sin(theta3+delta3)]

    for i in range(2):

        AS.append(s1*alpha2*pr1[i] - s1*(W2**2)*pi1[i])
        AU.append(u1*alpha4*pr2[i] - u1*(W4**2)*pi2[i])
        APA.append(p1*alpha3*pr3[i] - p1*(W3**2)*pi3[i])

    AP = np.array(ALA) + np.array(APA)
    AP = list(AP)

     # ACELERAÇÃO NO PONTOS DE INTERESSES - CRUZADO

    ASs = []
    AUs = []
    APAs = []

    pr1c = [np.sin(theta2 + delta2), np.cos(theta2+delta2)]
    pi1c = [np.cos(theta2+delta2), np.sin(theta2+delta2)]
    pr2c = [-np.sin(theta4c + delta4), np.cos(theta4c+delta4)]
    pi2c = [np.cos(theta4c+delta4), np.sin(theta4c+delta4)]
    pr3c = [-np.sin(theta3c + delta3), np.cos(theta3c+delta3)]
    pi3c = [np.cos(theta3c+delta3), np.sin(theta3c+delta3)]

    for i in range(2):

        ASs.append(s1*alpha2*pr1c[i] - s1*(W2**2)*pi1c[i])
        AUs.append(u1*alpha4*pr2c[i] - u1*(W4c**2)*pi2c[i])
        APAs.append(p1*alpha3*pr3c[i] - p1*(W3c**2)*pi3c[i])

    APc = np.array(ALAc) - np.array(APAs)
    APc = list(APc)

    return AP,alpha3,alpha4,alpha3c,alpha4c,APc

def analise_cinematica_mecanismo_4_barras(a,b,c,d,W2,alpha2):
    
    matriz_posicao = {'THETA3': [], 'THETA4': []}
    matriz_velocidade_angular = {'W3': [], 'W4': []}
    matriz_aceleracao_angular = {'ALPHA3': [], 'ALPHA4': []}

    for theta2 in np.arange(0, 2*np.pi, 0.01):
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
        matriz_posicao["THETA3"].append(theta3)
        matriz_posicao["THETA4"].append(theta4)
        #theta3c = np.arctan2(Byc-Ay, Bxc-Ax)
        #theta4c = np.arctan2(Byc, Bxc-d)

        # VELOCIDADE ANGULARES

        W3 = (a/b) * W2 * (np.sin(theta4 - theta2) / np.sin(theta3 - theta4))
        W4 = (a/c) * W2 * (np.sin(theta2 - theta3) / np.sin(theta4 - theta3))

       # W3c = (a/b) * W2 * (np.sin(theta4c - theta2) / np.sin(theta3c - theta4c))
        #W4c = (a/c) * W2 * (np.sin(theta2 - theta3c) / np.sin(theta4c - theta3c))
        matriz_velocidade_angular["W3"].append(W3)
        matriz_velocidade_angular["W4"].append(W4)

        # Acelerações Angulares - ABERTO

        AA = c * np.sin(theta4)
        BB = b * np.sin(theta3)
        CC = a * alpha2 * np.sin(theta2)+a*(W2**2) * np.cos(theta2) + \
            b * (W3**2) * np.cos(theta3) - c * (W4**2) * np.cos(theta4)
        DD = c * np.cos(theta4)
        EE = b * np.cos(theta3)
        FF = a * alpha2 * np.cos(theta2)-a*(W2**2) * np.sin(theta2) - \
            b * (W3**2) * np.sin(theta3) + c * (W4**2) * np.sin(theta4)

        alpha3 = (CC * DD - AA * FF)/(AA * EE - BB * DD)
        alpha4 = (CC * EE - BB * FF)/(AA * EE - BB * DD)

        matriz_aceleracao_angular["ALPHA3"].append(alpha3)
        matriz_aceleracao_angular["ALPHA4"].append(alpha4)
        # Acelerações Angulares - CRUZADO
       
       # alpha3c = (CCc * DDc - AAc * FFc)/(AAc * EEc - BBc * DDc)
        #alpha4c = (CCc * EEc - BBc * FFc)/(AAc * EEc - BBc * DDc)
    return matriz_posicao,matriz_velocidade_angular,matriz_aceleracao_angular


def analise_dinâmica(theta2i,W2ii,alpha2,T4,FP,deltaFP,ponto_p,deltapp,CG2,CG3,CG4,deltaCG2,deltaCG3,deltaCG4,a,b,c,d,massa2,massa3,massa4,ig2,ig3,ig4):
    '''
     Função que faz a analise dinâmica de Mecanismo de 4 barras
    '''
    

    O2 = [0, 0]
    O4 = [d, 0]

    deltaCG2 = np.deg2rad(deltaCG2)
    deltaCG3 = np.deg2rad(deltaCG3)
    deltaCG4 = np.deg2rad(deltaCG4)

    deltapp = np.deg2rad(deltapp)

    deltaFP = np.deg2rad(deltaFP)
    xddp = [np.cos(deltaFP), np.sin(deltaFP)]
    FPP = []
    for i in range(2):
        FPP.append(FP * xddp[i])

    t = np.arange(0, 1*np.pi/W2ii, 0.1)

    # Armazenar os Dados

    Dinamica = {'Torque': [],'F12x':[],'F12y':[],'F32x':[],'F32y':[],'F43x':[],'F43y':[],'F14x':[],'F14y':[]}
    contator = 0
    eixo_x = np.arange(0, 1*np.pi/W2ii, 0.1)
    for time in np.arange(0, 1*np.pi/W2ii, 0.1):

        theta2 = theta2i + W2ii*time + (0.5 * alpha2 * (time**2))
        W2 = W2ii + alpha2 * time

        # Ponto A
        Ax = a * np.cos(deltaCG2)
        Ay = a * np.sin(deltaCG2)

        A1 = [Ax, Ay]

        # Ponto B

        S = (a**2-b**2+c**2-d**2)/(2*(Ax - d))
        P = (Ay**2) / ((Ax - d)**2) + 1
        Q = 2 * Ay * (d - S) / (Ax - d)
        R = (d - S)**2 - c**2

        By = (-Q + np.sqrt(Q**2 - 4 * P * R))/(2*P)
        Bx = S - (Ay * By) / (Ax - d)

        B1 = [Bx, By]

        # CALCULO DE THETA 3 E THETA 4

        theta3 = np.arctan2(By-Ay, Bx-Ax)
        theta4 = np.arctan2(By, Bx-d)

        # Localização dos (CENTRO DE GRAVIDADE)

        RCG2 = []
        xrcg2 = [np.cos(theta2 + deltaCG2), np.sin(theta2 + deltaCG2)]
        for i in range(2):
            RCG2.append(CG2*xrcg2[i])

        RCG3 = []
        xrcg3 = [np.cos(theta3 + deltaCG3), np.sin(theta3 + deltaCG3)]
        for i in range(2):
            RCG3.append(A1[i]*CG3 * xrcg3[i])
        
        RCG4 = []
        xrcg4 = [np.cos(theta4+deltaCG4), np.sin(theta4+deltaCG4)]
        for i in range(2):
            RCG4.append(O4[i]+CG4*xrcg4[i])

        RP = []
        rpi = [np.cos(deltapp), np.sin(deltapp)]
        for i in range(2):
            RP.append(RCG3[i] + ponto_p * rpi[i])

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

        # VELOCIDADE DOS (CENTRO DE GRAVIDADE)

        VCG2 = []
        VCG4 = []
        VCG3A = []
        W2i2 = [-np.sin(theta2 + deltaCG2), np.cos(theta2 + deltaCG2)]
        W3i2 = [-np.sin(theta4 + deltaCG4), np.cos(theta4 + deltaCG4)]
        W4i2 = [-np.sin(theta3 + deltaCG3), np.cos(theta3 + deltaCG3)]

        for i in range(2):

            VCG2.append(CG2 * W2 * W2i2[i])
            VCG4.append(CG4 * W4 * W3i2[i])
            VCG3A.append(CG3 * W3 * W4i2[i])

        VCG3 = VA + VCG3A

        # Acelerações Angulares

        AA = c * np.sin(theta4)
        BB = b * np.sin(theta3)
        CC = a * alpha2 * np.sin(theta2)+a*(W2**2) * np.cos(theta2) + \
            b * (W3**2) * np.cos(theta3) - c * (W4**2) * np.cos(theta4)
        DD = c * np.cos(theta4)
        EE = b * np.cos(theta3)
        FF = a * alpha2 * np.cos(theta2)-a*(W2**2) * np.sin(theta2) - \
            b * (W3**2) * np.sin(theta3) + c * (W4**2) * np.sin(theta4)

        alpha3 = (CC * DD - AA * FF)/(AA * EE - BB * DD)
        alpha4 = (CC * EE - BB * FF)/(AA * EE - BB * DD)

        # Acelerações Lineares

        ALA = [- a * alpha2*np.sin(theta2) - a * (W2**2)*np.cos(theta2),
            a * alpha2*np.cos(theta2) - a * (W2**2)*np.sin(theta2)]
        ALB = [c * alpha4 * np.sin(theta4) + c * (W4**2) * np.cos(theta4), -
            c * alpha4 * np.cos(theta4) + c * (W4**2) * np.sin(theta4)]

        ALBA = np.array(ALB) - np.array(ALA)
        ALBA = list(ALBA)

        # ACELERAÇÃO NO (CENTRO DE GRAVIDADE)

        ACG2 = []
        ACG4 = []
        ACG3A = []

        pr1 = [np.sin(theta2 + deltaCG2), np.cos(theta2+deltaCG2)]
        pi1 = [np.cos(theta2+deltaCG2), np.sin(theta2+deltaCG2)]
        pr2 = [-np.sin(theta4 + deltaCG4), np.cos(theta4+deltaCG4)]
        pi2 = [np.cos(theta4+deltaCG4), np.sin(theta4+deltaCG4)]
        pr3 = [-np.sin(theta3 + deltaCG3), np.cos(theta3+deltaCG3)]
        pi3 = [np.cos(theta3+deltaCG3), np.sin(theta3+deltaCG3)]

        for i in range(2):

            ACG2.append(CG2*alpha2*pr1[i] - CG2*(W2**2)*pi1[i])
            ACG4.append(CG4*alpha4*pr2[i] - CG4*(W4**2)*pi2[i])
            ACG3A.append(CG3*alpha3*pr3[i] - CG3*(W3**2)*pi3[i])

        ACG3 = np.array(ALA) - np.array(ACG3A)
        ACG3 = list(ACG3)

        # VETORES DE POSICAO DAS REAÇOES

        R12 = []
        R32 = []
        R23 = []
        R43 = []
        R34 = []
        R14 = []

        for i in range(2):

            R12.append(O2[i]-RCG2[i])
            R32.append(A1[i]-RCG2[i])
            R23.append(A1[i]-RCG3[i])
            R43.append(B1[i]-RCG3[i])
            R34.append(B1[i]-RCG4[i])
            R14.append(O4[i]-RCG4[i])

            #R12 = O2 - RCG2
            #R32 = A1 - RCG2
            #R23 = A1 - RCG3
            #R43 = B1 - RCG3
            #R34 = B1 - RCG4
            #R14 = O4 - RCG4

        # DINAMICA INVERSA

        matrizA = np.array([[1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0], [-R12[1], R12[0], -R32[1], R32[0], 0, 0, 0, 0, 1], [0, 0, -1, 0, 1, 0, 0, 0, 0], [0, 0, 0, -1, 0,
                        1, 0, 0, 0], [0, 0, R23[1], -R23[0], -R43[1], R43[0], 0, 0, 0], [0, 0, 0, 0, -1, 0, 1, 0, 0], [0, 0, 0, 0, 0, -1, 0, 1, 0], [0, 0, 0, 0, R34[1], -R34[0], - R14[1], R14[0], 0]])

        matrizC = np.array([[massa2*ACG2[0]], [massa2 * ACG2[1]], [ig2*alpha2], [massa3*ACG3[0]-FPP[0]], [massa3*ACG3[1] - FPP[1]],
                        [ig3 * alpha3 - RP[0] * FPP[1] + RP[1]*FPP[0]], [massa4 * ACG4[0]], [massa4 * ACG4[1]], [ig4 * alpha4 - T4]])

        matriB = np.linalg.inv(matrizA) @ matrizC
        
        #F12 = matriB[0:2]
        #F32 = matriB[2:3]
        #F43 = matriB[4:5]
        #F14 = matriB[6:7]
        #T12 = matriB[8]
        #print('MBTA',matriB)

        
        # ARMAZERNAR AS INFORMAÇÕES
        Dinamica['F12x'].append(matriB[0])
        Dinamica['F12y'].append(matriB[1])
        Dinamica['F32x'].append(matriB[2])
        Dinamica['F32y'].append(matriB[3])
        Dinamica['F43x'].append(matriB[4])
        Dinamica['F43y'].append(matriB[5])
        Dinamica['F14x'].append(matriB[6])
        Dinamica['F14y'].append(matriB[7])
        Dinamica['Torque'].append(matriB[8])

    return Dinamica,eixo_x


def calc_th_b(a,b,c,d,th_a,mode='open',show_angle=False):
    '''
    Calculates theta b using Freuedenstein equations
    '''
    K1 = d/a
    K4 = d/b
    K5 = (-a**2-b**2+c**2-d**2)/(2*a*b)
    D = np.cos(th_a) - K1 + K4*np.cos(th_a) + K5
    E = -2*np.sin(th_a)
    F = K1 + (K4-1)*np.cos(th_a) + K5
    disc = (E**2)-4*D*F
    #Checks if non-grashoff, and extracts the valid angles
    if not(np.greater_equal(disc,0).all()):
        #This extracts the th_a elements with discriminants > 0 and reruns the function.
        condition = np.greater_equal(disc,0)
        th_a = np.extract(condition, th_a)
        condition = np.less_equal(th_a, np.pi)
        th_a= np.extract(condition,th_a)
        th_a=np.append(th_a,th_a[-2::-1])
        _,th_b=calc_th_d(a,b,c,d,th_a)
    else:
        th_b=2*np.arctan((-E - np.sqrt(disc) )/(2*D)) if mode=='open' else 2*np.arctan((-E + np.sqrt(disc) )/(2*D))
    return th_a,th_b

def calc_th_d(a,b,c,d,th_a,mode='open',show_angle=False):
    '''
    Calculates theta d using Freuedenstein equations
    '''
    K1 = d/a
    K2 = d/c
    K3 = (a**2-b**2+c**2+d**2)/(2*a*c)
    A = np.cos(th_a) - K1 - K2*np.cos(th_a) + K3
    B = -2*np.sin(th_a)
    C = K1 - (K2+1)*np.cos(th_a) + K3
    #Grashoff condition
    disc = (B**2)-4*A*C
#    print(disc)
    #Checks if non-grashoff, and extracts the valid angles
    if not(np.greater_equal(disc,0).all()):#Checks grashoff?
        #This extracts the th_a elements with discriminants > 0 and reruns the function.
        condition = np.greater_equal(disc,0)
        th_a = np.extract(condition, th_a)
#        condition = np.less_equal(th_a, np.pi)
#        th_a= np.extract(condition,th_a)
        th_a=np.append(th_a,th_a[-2::-1])#Full range of non-grashoff motion
        _,th_d=calc_th_d(a,b,c,d,th_a,show_angle=True)
    else:
        th_d=2*np.arctan((-B - np.sqrt(disc) )/(2*A)) if mode=='open' else 2*np.arctan((-B + np.sqrt(disc) )/(2*A))#Final formula for other fixed angle

    return th_a,th_d

def generate_th_a(rotation='cw',step=0.1):
    return np.arange(np.pi,-np.pi,-step*np.pi) if rotation=='cw' else np.arange(-np.pi,np.pi+0.0001,step*np.pi)
def calc_joint_position(a,b,c,d,th_a):
    '''
    Calculates the position of the joints
    '''
    if a==c and b==d:
        print('Special GRashoff')
        th_d=th_a
    else:
        th_a,th_d=calc_th_d(a,b,c,d,th_a,show_angle=True)
#    print(th_a)
#    print(th_d)
    if th_a[0]==-np.pi and th_a[-1]==np.pi:
        pass
    else:
        th_a=full_rotation(th_a)
        th_d=full_rotation(th_d)
    x1,x4 = 0,d
    y1,y4 = 0,0
    x2,x3 = a*np.cos(th_a), d + c*np.cos(th_d)
    y2,y3 = a*np.sin(th_a), c*np.sin(th_d)
    return x1,x2,x3,x4,y1,y2,y3,y4

'''
NUMERICAL SOLUTION USING MULTIDIMENSIONAL NR METHOD
'''
def generate_th2(a,b,c,d,nth=100):
    #input_config defines the input linkage configuration type
    input_config={(-1,-1,1):'C',
                  (1,1,1):'C',
                  (1,-1,-1):'R',
                  (-1,1,-1):'R',
                  (-1,-1,-1):'O',
                  (-1,1,1):'P',
                  (1,-1,1):'P',
                  (1,1,-1):'O'
     }
    T1=np.sign(b+d-a-c)
    T2=np.sign(c+d-a-b)
    T3=np.sign(b+c-a-d)

    conf=input_config[(T1,T2,T3)]
    tog1=np.arccos((a**2+d**2-b**2-c**2)/(2*a*d)-(b*c)/(a*d))
    tog2=np.arccos((a**2+d**2-b**2-c**2)/(2*a*d)+(b*c)/(a*d))
    tog=tog1 if np.isnan(tog2) else tog2
    if conf in ['O','P']:
        tog=abs(tog)
        if conf in ['O']:
            th2=np.linspace(-tog,tog,nth)
        else:
            th2=np.linspace(tog,2*np.pi-tog,nth)
    elif conf in ['C']:
        th2=np.linspace(-np.pi,np.pi,nth)
    elif conf in ['R']:
        th2=np.linspace(tog1,tog2,nth)
        pass
    else:
        Exception
    return th2


    th2=generate_th2(a,b,c,d,nth)
#    th2=np.append(th2,th2[-2::-1])
    th3=np.zeros_like(th2)
    th4=np.zeros_like(th2)
#    print(th2)
    th3[0]=np.arcsin(a*np.sin(abs(th2[0]))/(b+c))
    th4[0]=-(np.pi-th3[0])
#    print(th3[0],th4[0])
    #Initalise
#    f=[lambda thb,thc: a*np.cos(th2[0])+b*cos(thb)-c*cos(thc)-d,
#       lambda thb,thc: a*np.sin(th2[0])+b*sin(thb)-c*sin(thc)]
#    x=findroot(f,(th3[0]*(1-eps),th4[0]*(1-eps)),tol=1E-8,solver='mnewton')
#    th3[0]=np.array(x,dtype=float)[0]
#    th4[0]=np.array(x,dtype=float)[1]
#    print(th3[0],th4[0])
    #Solve angles theta_3 and theta_4 using mpmath multidimensional Newton's method
    for i in range(1,nth):
        f=[lambda thb,thc: a*np.cos(th2[i])+b*cos(thb)-c*cos(thc)-d,
           lambda thb,thc: a*np.sin(th2[i])+b*sin(thb)-c*sin(thc)]
#        x=findroot(f,(th3[i-1]*(1-eps),th4[i-1]*(1-eps)),tol=1E-8,verify=False,verbose=True,solver='mnewton')
        x=findroot(f,(th3[i-1]*(1-eps),th4[i-1]*(1-eps)),verify=False,verbose=False,solver='anewton')
        
        th3[i]=np.array(x,dtype=float)[0]
        th4[i]=np.array(x,dtype=float)[1]
    th3=principal_angle(th3)
    th4=principal_angle(th4)
    return th2,th3,th4

def full_rotation(x):
    return np.append(x,x[-2::-1])


def principal_angle(t):
    return t-np.round(t/(2*np.pi))*2*np.pi

def animate_linkage_motion(fig,x1,x2,x3,x4,y1,y2,y3,y4):
    def animate(i,x1,x2,x3,x4,y1,y2,y3,y4):
        #This uses global angles in degrees
#        global th_a_d,patch1
#        global th_b_d,patch2
#        global th_d_d,patch4
#
#        global arrow1,arrow2,arrow3,len_arrow
        #This draws the linkages
        thisx = [x1, x2[i],x3[i],x4]
        thisy = [y1, y2[i],y3[i],y4]
        line.set_data(thisx, thisy)
        '''
        #This draws the angles
        ax.patches.remove(patch1)
        patch1= patches.Arc((x1,y1),100,100,0,0,th_a_d[i],color='r')
        ax.add_patch(patch1)

        ax.patches.remove(patch2)
        patch2= patches.Arc((x2[i],y2[i]),100,100,0,0,th_b_d[i],color='g')
        ax.add_patch(patch2)

        ax.patches.remove(patch4)
        patch4 = patches.Arc((x4,y4),100,100,0,0,th_d_d[i],color = 'b')
        ax.add_patch(patch4)

        #Draws tangential component
    #    ax.patches.remove(arrow1)
    #    arrow1 = patches.Arrow(x3[i],y3[i]
    #                           ,len_arrow*v_b[i]*(np.cos(th_d[i]-th_b[i])*
    #np.cos(np.pi + th_b[i] - th_d[i]) + np.sin(th_d[i]-th_b[i])*np.sin(np.pi + th_b[i] - th_d[i]))
    #                           ,len_arrow*v_b[i]*(np.sin(th_d[i]-th_b[i])*
    #np.cos(np.pi + th_b[i] - th_d[i]) - np.cos(th_d[i]-th_b[i])*np.sin(np.pi + th_b[i] -
    #th_d[i]))
    #                           ,width = 20,color = 'y')
    #    ax.add_patch(arrow1)
        #Draws radial component

        ax.patches.remove(arrow3)
        arrow3 = patches.Arrow(x3[i],y3[i],
                               len_arrow*np.cos(th_b[i])*v_b[i]*np.cos(np.pi + th_b[i]- th_d[i])
                               ,len_arrow*np.sin(th_b[i])*v_b[i]*np.cos(np.pi + th_b[i]- th_d[i])
                               ,width = 20,color = 'y')
        ax.add_patch(arrow3)

        #Draws actual component
        ax.patches.remove(arrow2)
        arrow2 = patches.Arrow(x3[i],y3[i],
                               len_arrow*np.cos(th_b[i])*v_b[i]
                               ,len_arrow*np.sin(th_b[i])*v_b[i]
                               ,width = 20,color = 'y')
        ax.add_patch(arrow2)

        #This displays the angles
    #    ax.text(x1,y1)
        text = \
        'Angle1 (red): ' + str(round(th_a_d[i],2)) + '\n' + \
        'Angle2 (green): ' + str(round(th_b_d[i],2)) + '\n' + \
        'Angle4 (blue): ' + str(round(th_d_d[i],2)) + '\n' + \
        'Speed(yellow): ' + str(round(v_b[i],2)) + '\n'
        ang_text.set_text(text)
        '''
        return line,#patch1,patch2,patch4,ang_text,arrow2,#arrow3,arrow1

    #Defining xandylims of the plot
    temp = x1,x2,x3,x4
    xmin = np.amin([np.amin(mini) for mini in temp])
    xmax = np.amax([np.amax(mini) for mini in temp])
    temp = y1,y2,y3,y4
    ymin = np.amin([np.amin(mini) for mini in temp])
    ymax = np.amax([np.amax(mini) for mini in temp])
    #xmin,xmax

    #fig = plt.figure(figsize=(6,6))
#    fig.set_size_inches(6,4.8,True)
    #plt.axis('off')

    #plt.tight_layout()
    bord = 10 #FBL an offset
    ax = fig.add_subplot(111, autoscale_on=True,
                         xlim=(xmin-bord, xmax+bord), ylim=(ymin-bord, ymax+bord))
    #ax.grid()
    #Draw linkages
#    plt.gca().set_aspect('equal',adjustable='box')

    line, = ax.plot([], [], marker = 'o',c = 'y',lw = 6,ms = 10)
    '''
    len_arrow = 300
    #Max and min angles, radians
    a_min = np.amin(th_d)
    a_max = np.amax(th_d)
    #draw arrows
    ax.arrow(x4,y4,
             len_arrow * np.cos(a_min), len_arrow * np.sin(a_min),
             fc='b', ec='b')
    ax.arrow(x4,y4,
             len_arrow * np.cos(a_max), len_arrow * np.sin(a_max)
             ,fc='b', ec='b')
    #Max and min angles, degrees
    a_min = np.amin(th_d_d)
    a_max = np.amax(th_d_d)
    #Draw angle between the arrows
    ang_radius = 200 #for both drawing and writing
    ang_subtended = a_max - a_min #angle subtended
    ang_patch = patches.Arc((x4,y4),ang_radius,ang_radius,a_min,0,ang_subtended)
    ax.add_patch(ang_patch)

    #Write angle
    #x,y = (x4 + ang_radius*np.cos(a_min),y4 + ang_radius*np.sin(a_min))
    #s = str(rou qnd(ang_subtended,2) )
    #ang_text = ax.text(x,y,'')
    #ang_text.set_text(s)

    #Initialize an arc patch
    #patch1 -> angle of point1 etc.
    patch1 = patches.Arc((x1,y1),100,100,0,0,0,color='r')
    patch2 = patches.Arc((x2[0],y2[0]),100,100,0,0,0,color='g')
    patch4 = patches.Arc((x4,y4),100,100,0,0,0,color = 'b')

    #Transmisson angle
    len_arrow = 100
    #arrow direction: use 0[i] - 0[i-1]/dt
    v_b = (np.roll(th_d,1) - np.roll(th_d,-1))*30

    arrow1 = patches.Arrow(x3[0],y3[0],0,0)
    arrow2 = patches.Arrow(x3[0],y3[0],0,0)
    arrow3 = patches.Arrow(x3[0],y3[0],0,0)
    ang_text = ax.text(0.5, 0.1, '', transform=ax.transAxes)
    '''
    #Initialize lines and patches

    #Animate the FBL
    ani = animation.FuncAnimation(fig, animate, frames=len(y2),fargs=(x1,x2,x3,x4,y1,y2,y3,y4),
                              interval=50, blit=True)
    return ani
