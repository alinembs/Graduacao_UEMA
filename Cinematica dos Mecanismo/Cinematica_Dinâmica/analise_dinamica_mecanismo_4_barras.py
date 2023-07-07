import numpy as np
import matplotlib.pyplot as plt

# Entradas

a = 12.7  # manivela
b = 38.1  # acoplador
c = 25.4  # seguidor
d = 48.26  # elo terra

massa2 = 0.680
ig2 = 0.006

massa3 = 3.493
ig3 = 0.011

massa4 = 2.631
ig4 = 0.090

O2 = [0, 0]
O4 = [d, 0]

# Pontos de (Centro de Gravidade)

CG2 = 0.762
CG3 = 22.86
CG4 = 12.7

deltaCG2 = np.deg2rad(30)
deltaCG3 = np.deg2rad(45)
deltaCG4 = np.deg2rad(0)

ponto_p = 7.62
deltapp = np.deg2rad(100)

# Indentifcações dos Esforços Externos

T4 = 13.558

FP = 355.84

deltaFP = np.deg2rad(330)

xddp = [np.cos(deltaFP), np.sin(deltaFP)]
FPP = []
for i in range(2):
    FPP.append(FP * xddp[i])


# Definição de Velocidade e Aceleração Angular W2 E ALPHA2

theta2i = np.deg2rad(60)
W2ii = np.deg2rad(1432.39)
alpha2 = np.deg2rad(-2291.93)

t = np.arange(0, 1*np.pi/W2ii, 0.1)

# Armazenar os Dados

matriz_posicao = {'PA': [], 'PB': [], 'RS': [], 'US': [], 'PS': []}
matriz_velocidade = {'VA': [], 'VB': [], 'VS': [], 'VP': [], 'VU': []}
matriz_aceleracao = {'ALA': [], 'ALB': [], 'AS': [], 'AP': [], 'AU': []}
matriz_velocidade_angular = {'W2': [], 'W3': [], 'W4': []}
matriz_aceleracao_angular = {'ALPHA2': [], 'ALPHA3': [], 'ALPHA4': []}
Torque = {'Torque': []}
contator = 0

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

    F12 = matriB[0:2]
    F32 = matriB[2:3]
    F43 = matriB[4:5]
    F14 = matriB[6:7]
    T12 = matriB[8]

    # ARMAZERNAR AS INFORMAÇÕES

    matriz_velocidade_angular['W2'].append(W2)
    matriz_velocidade_angular['W3'].append(W3)
    matriz_velocidade_angular['W4'].append(W4)

    matriz_aceleracao_angular['ALPHA2'].append(alpha2)
    matriz_aceleracao_angular['ALPHA3'].append(alpha3)
    matriz_aceleracao_angular['ALPHA4'].append(alpha4)

    matriz_posicao['PA'].append(A1)
    matriz_posicao['PB'].append(B1)
    matriz_posicao['RS'].append(RCG2)
    matriz_posicao['US'].append(RCG4)
    matriz_posicao['PS'].append(RCG3)

    matriz_velocidade['VA'].append(np.linalg.norm(VA))
    matriz_velocidade['VB'].append(np.linalg.norm(VB))
    matriz_velocidade['VP'].append(np.linalg.norm(VCG3))
    matriz_velocidade['VS'].append(np.linalg.norm(VCG2))
    matriz_velocidade['VU'].append(np.linalg.norm(VCG4))

    matriz_aceleracao['ALA'].append(np.linalg.norm(ALA))
    matriz_aceleracao['ALB'].append(np.linalg.norm(ALB))
    matriz_aceleracao['AP'].append(np.linalg.norm(ACG3))
    matriz_aceleracao['AS'].append(np.linalg.norm(ACG2))
    matriz_aceleracao['AU'].append(np.linalg.norm(ACG4))

    Torque['Torque'].append(T12)

plt.plot(t, Torque['Torque'], 'r-', label='Torque')
plt.ylabel('Torque')
plt.xlabel("Tempo")
plt.title("Cinematica dos Mecanismo - 4 Barras")
plt.legend()
plt.show()
