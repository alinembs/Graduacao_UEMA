import numpy as np
import matplotlib.pyplot as plt

# Entradas

a = 10
b = 13
c = 15
d = 17

O2 = [0, 0]
O4 = [d, 0]

s1 = 12
p1 = 15
u1 = 10


delta2 = np.deg2rad(15)
delta3 = np.deg2rad(30)
delta4 = np.deg2rad(-10)

# Definição de Velocidade e Aceleração Angular W2 E ALPHA2

theta2i = np.deg2rad(0)
W2ii = 5
alpha2 = 0.1
t = np.arange(0, 6*np.pi/W2ii, 0.1)

# Armazenar os Dados

matriz_posicao = {'PA': [], 'PB': [], 'RS': [], 'US': [], 'PS': []}
matriz_velocidade = {'VA': [], 'VB': [], 'VS': [], 'VP': [], 'VU': []}
matriz_aceleracao = {'ALA': [], 'ALB': [], 'AS': [], 'AP': [], 'AU': []}
matriz_velocidade_angular = {'W2': [], 'W3': [], 'W4': []}
matriz_aceleracao_angular = {'ALPHA2': [], 'ALPHA3': [], 'ALPHA4': []}

for time in np.arange(0, 6*np.pi/W2ii, 0.1):

    theta2 = theta2i + W2ii*time + (0.5 * alpha2 * (time**2))
    W2 = W2ii + alpha2 * time

    # Ponto A
    Ax = a * np.cos(delta2)
    Ay = a * np.sin(delta2)

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

    # Localização dos Pontos de Interesse

    RS = s1 * [np.cos(theta2 + delta2), np.sin(theta2 + delta2)]
    PS = A1 + p1 * [np.cos(theta3 + delta3), np.sin(theta3 + delta3)]
    US = O4 + u1 * [np.cos(theta4+delta4), np.sin(theta4+delta4)]

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

    # ACELERAÇÃO NO PONTOS DE INTERESSES

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

    AP = np.array(ALA) - np.array(APA)
    AP = list(AP)

    # ARMAZERNAR AS INFORMAÇÕES

    matriz_velocidade_angular['W2'].append(W2)
    matriz_velocidade_angular['W3'].append(W3)
    matriz_velocidade_angular['W4'].append(W4)

    matriz_aceleracao_angular['ALPHA2'].append(alpha2)
    matriz_aceleracao_angular['ALPHA3'].append(alpha3)
    matriz_aceleracao_angular['ALPHA4'].append(alpha4)

    matriz_posicao['PA'].append(A1)
    matriz_posicao['PB'].append(B1)
    matriz_posicao['RS'].append(RS)
    matriz_posicao['US'].append(US)
    matriz_posicao['PS'].append(PS)

    matriz_velocidade['VA'].append(np.linalg.norm(VA))
    matriz_velocidade['VB'].append(np.linalg.norm(VB))
    matriz_velocidade['VP'].append(np.linalg.norm(VP))
    matriz_velocidade['VS'].append(np.linalg.norm(VS))
    matriz_velocidade['VU'].append(np.linalg.norm(VU))

    matriz_aceleracao['ALA'].append(np.linalg.norm(ALA))
    matriz_aceleracao['ALB'].append(np.linalg.norm(ALB))
    matriz_aceleracao['AP'].append(np.linalg.norm(AP))
    matriz_aceleracao['AS'].append(np.linalg.norm(AS))
    matriz_aceleracao['AU'].append(np.linalg.norm(AU))

print("\n ---- CINEMATICA DOS MECANISMO ----")
print("\n 1- GRAFICO DE VELOCIDADE ANGULAR")
print("\n 2- GRAFICO DE ACELERACAO ANGULAR")
print("\n 3- GRAFICO DE VELOCIDADE ")
print("\n 4- GRAFICO DE ACELERACAO")
print("\n 0 - SAIR ")

a = int(input('\n ESCOLHA O TIPO DE GRAFICO GERADO!'))

if a == 0:

    print("PROGRAMA FINALIZADO")

if a == 1:

    plt.plot(t,matriz_velocidade_angular['W2'],'r-', label = 'W2')
    plt.plot(t,matriz_velocidade_angular['W3'],'g-', label = 'W3')
    plt.plot(t,matriz_velocidade_angular['W4'],'y-', label = 'W4')
    plt.ylabel('VELOCIDADE ANGULAR')
    plt.xlabel("Tempo")
    plt.title("Cinematica dos Mecanismo - 4 Barras")
    plt.legend()
    plt.show()

if a == 2:

    plt.plot(t,matriz_aceleracao_angular['ALPHA2'],'r-', label = 'Alpha2')
    plt.plot(t,matriz_aceleracao_angular['ALPHA3'],'g-', label = 'Alpha3')
    plt.plot(t,matriz_aceleracao_angular['ALPHA4'],'y-', label = 'Alpha4')
    plt.ylabel('ACELERACAO ANGULAR')
    plt.xlabel("Tempo")
    plt.title("Cinematica dos Mecanismo - 4 Barras")
    plt.legend()
    plt.show()

if a == 3:

    plt.plot(t,matriz_velocidade['VA'],'r-',label="VA")
    plt.plot(t,matriz_velocidade['VB'],'g-',label="VB")
    plt.plot(t,matriz_velocidade['VP'],'y-',label="VP")
    plt.plot(t,matriz_velocidade['VS'],'b-',label="VS")
    plt.plot(t,matriz_velocidade['VU'],'c-',label="VU")
    plt.ylabel('VELOCIDADE')
    plt.xlabel("Tempo")
    plt.title("Cinematica dos Mecanismo - 4 Barras")
    plt.legend()
    plt.show()

if a == 4:

    plt.plot(t,matriz_aceleracao['ALA'],'r-', label='ALA')
    plt.plot(t,matriz_aceleracao['ALB'],'g-', label='ALB')
    plt.plot(t,matriz_aceleracao['AP'],'y-', label='AP')
    plt.plot(t,matriz_aceleracao['AS'],'b-', label='AS')
    plt.plot(t,matriz_aceleracao['AU'],'c-', label='AU')
    plt.ylabel('ACELERACAO')
    plt.xlabel("Tempo")
    plt.title("Cinematica dos Mecanismo - 4 Barras")
    plt.legend()
    plt.show()

else:
    print("PROGRAMA FINALIZADO")