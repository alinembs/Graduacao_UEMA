import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuração de Visualização da Animação

fig = plt.figure(figsize=(10, 6))
slink, = plt.plot([], [], 'r-', linewidth=4)
joints, = plt.plot([], [], marker='o', ls="", markersize=10)

plt.axis([-20, 40, -20, 40])
plt.axis('square')

# Gerando Delta2 ou Theta2

theta2 = np.arange(0, 2*np.pi, 0.01)
s1 = 12
p1 = 15
u1 = 10

delta2 = np.deg2rad(15)
delta3 = np.deg2rad(30)
delta4 = np.deg2rad(-10)

# Calculando os Valores de Theta3 , Theta4,02,04,A1 e B1


def calculate(delta2,delta3,delta4,theta2):

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

    return O2, A1, B1, O4

# 02 A
# 04 D
# A1 B
# B1 C

def animate(theta2):
    A, B, C, D, = calculate(delta2,delta3,delta4,theta2)
    x = [A[0], B[0], C[0], D[0]]
    y = [A[1], B[1], C[1], D[1]]
    
    slink.set_data(x, y)
    joints.set_data(x, y)
    

    return slink, joints

ani = animation.FuncAnimation(
    fig, animate, np.arange(0, 2*np.pi, 0.01), interval=10, blit=True)
plt.show()
