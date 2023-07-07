import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuração de Visualização da Animação

fig = plt.figure(figsize=(8, 8))
#slink, = plt.plot([], [], 'r-', linewidth=4)
#joints, = plt.plot([], [], marker='o', ls="", markersize=10)
#velo1, = plt.plot([], [], 'y', linewidth=2)
#velo2, = plt.plot([], [], 'c', linewidth=2)
#velo3, = plt.plot([], [], 'g', linewidth=2)
veloc_angular_st, = plt.plot([],[],'ro')
veloc_angular, = plt.plot([],[],'c')
#plt.fill([0,0.1,0.2],[0.1,0.3,0.4])
plt.axis([0, 20, -10, 50])
plt.axis('square')

# Gerando Delta2 e Theta2

#theta2 = np.arange(0, 2*np.pi, 0.01)

theta2i = np.deg2rad(0)
W2 = 0.3
time = np.arange(0,6*np.pi/W2,0.1)
theta2 = theta2i + W2*time
s1 = 12
p1 = 15
u1 = 10

delta2 = np.deg2rad(15)
delta3 = np.deg2rad(30)
delta4 = np.deg2rad(-10)

# Calculando os Valores de Theta3 , Theta4,02,04,A1 e B1


def calculate(delta2, delta3, delta4, theta2):

    a = 10
    b = 13
    c = 15
    d = 17

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

    #VELOCIDADE ANGULARES

    W3 = (a/b) * W2 * (np.sin(theta4 - theta2)/ np.sin(theta3 - theta4))
    W4 = (a/c) * W2 * (np.sin(theta2 - theta3)/ np.sin(theta4 - theta3))

    #VELOCIDADE LINEARES

    VA = []
    VBA= []
    VB = []
    W2i = [-np.sin(theta2),np.cos(theta2)]
    W3i = [-np.sin(theta3),np.cos(theta3)]
    W4i = [-np.sin(theta4), np.cos(theta4)]
    for i in range(2):

        VA.append( a * W2 * W2i[i])
        VBA.append( b * W3 * W3i[i])
        VB.append( c * W4 * W4i[i])

    #VELOCIDADE DOS PONTOS DE INTERESSE

    VS = []
    VU= []
    VPA = []
    W2i2 = [-np.sin(theta2 +delta2), np.cos(theta2 + delta2)]
    W3i2 = [-np.sin(theta4 +delta4), np.cos(theta4 + delta4)]
    W4i2 = [-np.sin(theta3 +delta3), np.cos(theta3 + delta3)]
    for i in range(2):

        VS.append( s1 * W2 * W2i2[i])
        VU.append( u1 * W4 * W3i2[i])
        VPA.append( p1 * W3 * W4i2[i])


    VP = VA +  VPA

    return O2, A1, B1, O4, RS, PS, US,VS,VU,VP,W3,W4

# 02 A
# 04 D
# A1 B
# B1 C


def animate(theta2):

    A, B, C, D, RS, PS, US,VS,VU,VP = calculate(delta2, delta3, delta4, theta2)
  

    x = [A[0], B[0], C[0], D[0]]
    y = [A[1], B[1], C[1], D[1]]
    x1 = [RS[0],RS[0]+ VS[0]]
    y1 = [RS[1],RS[1]+ VS[1]]
    x2 = [US[0],US[0]+ VU[0]]
    y2 = [US[1],US[1]+ VU[1]]
    x3 = [PS[0],PS[0]+ VP[0]]
    y3 = [PS[1],PS[1]+ VP[1]]

    #slink.set_data(x, y)
    #joints.set_data(x, y)
    #velo1.set_data(x1,y1)
    #velo2.set_data(x2,y2)
    #velo3.set_data(x3,y3)
    # fill1.set_data(x1,y1)
    # fill2.set_data(x2,y2)
    # fill3.set_data(x3,y3)

#    return slink, joints,velo1,velo2,velo3


def calculate_w3_w4(time):

    theta2i = np.deg2rad(0)
    W2 = 0.3
    theta2 = theta2i + W2*time
    a = 10
    b = 13
    c = 15
    d = 17

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

    By = (-Q + np.sqrt(Q**2 - 4 * P * R))/(2*P)
    Bx = S - (Ay * By) / (Ax - d)

    B1 = [Bx, By]

    # CALCULO DE THETA 3 E THETA 4
    theta3 = np.arctan2(By-Ay, Bx-Ax)
    theta4 = np.arctan2(By, Bx-d)

    #VELOCIDADE ANGULARES

    W3 = (a/b) * W2 * (np.sin(theta4 - theta2)/ np.sin(theta3 - theta4))
    W4 = (a/c) * W2 * (np.sin(theta2 - theta3)/ np.sin(theta4 - theta3))
      #VELOCIDADE LINEARES

    VA = []
    VBA= []
    VB = []
    W2i = [-np.sin(theta2),np.cos(theta2)]
    W3i = [-np.sin(theta3),np.cos(theta3)]
    W4i = [-np.sin(theta4), np.cos(theta4)]
    for i in range(2):

        VA.append( a * W2 * W2i[i])
        VBA.append( b * W3 * W3i[i])
        VB.append( c * W4 * W4i[i])

    #VELOCIDADE DOS PONTOS DE INTERESSE

    VS = []
    VU= []
    VPA = []
    W2i2 = [-np.sin(theta2 +delta2), np.cos(theta2 + delta2)]
    W3i2 = [-np.sin(theta4 +delta4), np.cos(theta4 + delta4)]
    W4i2 = [-np.sin(theta3 +delta3), np.cos(theta3 + delta3)]
    for i in range(2):

        VS.append( s1 * W2 * W2i2[i])
        VU.append( u1 * W4 * W3i2[i])
        VPA.append( p1 * W3 * W4i2[i])


    VP = VA +  VPA

    return VS,VU,VP
VS,VU,VP = calculate_w3_w4(time)
l = plt.plot(time,VP[0])
def animate_velocidade(time):
     VS,VU,VP = calculate_w3_w4(time)
     veloc_angular.set_data(time,VP[0])
     veloc_angular_st.set_data(time,VP[0])
     return veloc_angular ,veloc_angular_st
    

my_animation_velocida = animation.FuncAnimation(fig,animate_velocidade,np.arange(0,6*np.pi/W2,0.1),interval = 10,blit=True, repeat = True)
#ani = animation.FuncAnimation(
#    fig, animate, np.arange(0, 2*np.pi, 0.01), interval=10, blit=True)

plt.ylabel("Velocidade")
plt.xlabel("Tempo")
plt.show()
