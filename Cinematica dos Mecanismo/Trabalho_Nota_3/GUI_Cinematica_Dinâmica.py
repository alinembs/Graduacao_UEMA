# Codigo Feito por Aline Mariana - UEMA/ENG COMP

# Importação das bibiotecas
import warnings
import tkinter as tk
from tkinter import ttk, messagebox

from Funcão_Cinematica_Dinâmica import*

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib
matplotlib.use('TkAgg')

from PIL import ImageTk, Image

# Ignorar apenas RuntimeWarnings relacionados a conversões de floats para inteiros
warnings.filterwarnings(
    "ignore", category=RuntimeWarning, message="converting.*")



#Definição da Interface Gráfica

class Frame_analise_dinamica(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # Elos
        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.E)
        self.input1 = ttk.Entry(self, width=10)
        self.input1.focus()
        self.input1.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.E)
        self.input2 = ttk.Entry(self, width=10)
        self.input2.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.E)
        self.input3 = ttk.Entry(self, width=10)
        self.input3.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.E)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.grid(column=1, row=3, sticky=tk.W)

         #Massa

        ttk.Label(self, text='Massa 2 (kg):').grid(
            column=0, row=4, sticky=tk.E)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.focus()
        self.input5.grid(column=1, row=4, sticky=tk.W)

        ttk.Label(self, text='Massa 3 (kg):').grid(column=0, row=5, sticky=tk.E)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=5, sticky=tk.W)

        ttk.Label(self, text='Massa 4 (kg):').grid(column=0, row=6, sticky=tk.E)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=6, sticky=tk.W)

        #Massa

        ttk.Label(self, text='Ig 2 (kg*m²):').grid(
            column=0, row=7, sticky=tk.E)
        self.input8 = ttk.Entry(self, width=10)
        self.input8.focus()
        self.input8.grid(column=1, row=7, sticky=tk.W)

        ttk.Label(self, text='Ig 3 (kg*m²):').grid(column=0, row=8, sticky=tk.E)
        self.input9 = ttk.Entry(self, width=10)
        self.input9.grid(column=1, row=8, sticky=tk.W)

        ttk.Label(self, text='Ig 4 (kg*m²):').grid(column=0, row=9, sticky=tk.E)
        self.input10 = ttk.Entry(self, width=10)
        self.input10.grid(column=1, row=9, sticky=tk.W)


        ttk.Label(self, text='Theta2-Inicial(radiano):').grid(
            column=0, row=10, sticky=tk.E)
        self.input11 = ttk.Entry(self, width=10)
        self.input11.grid(column=1, row=10, sticky=tk.W)


        ttk.Label(self, text='W2-Inicial(radiano):').grid(
            column=0, row=11, sticky=tk.E)
        self.input12 = ttk.Entry(self, width=10)
        self.input12.grid(column=1, row=11, sticky=tk.W)

        ttk.Label(self, text='Alpha2-Constante(radiano):').grid(
            column=2, row=0, sticky=tk.E)
        self.input13 = ttk.Entry(self, width=10)
        self.input13.grid(column=3, row=0, sticky=tk.W)

        #Forcas Externas


        ttk.Label(self, text='T4:').grid(
            column=2, row=1, sticky=tk.E)
        self.input14 = ttk.Entry(self, width=10)
        self.input14.grid(column=3, row=1, sticky=tk.W)


        ttk.Label(self, text='FP:').grid(
            column=2, row=2, sticky=tk.E)
        self.input15 = ttk.Entry(self, width=10)
        self.input15.grid(column=3, row=2, sticky=tk.W)

        ttk.Label(self, text='Delta FP(radianos):').grid(
            column=2, row=3, sticky=tk.E)
        self.input16 = ttk.Entry(self, width=10)
        self.input16.grid(column=3, row=3, sticky=tk.W)

        ttk.Label(self, text='Ponto P:').grid(
                    column=2, row=4, sticky=tk.E)
        self.input17 = ttk.Entry(self, width=10)
        self.input17.grid(column=3, row=4, sticky=tk.W)

        ttk.Label(self, text=' Delta do Ponto P(radianos):').grid(
                    column=2, row=5, sticky=tk.E)
        self.input18 = ttk.Entry(self, width=10)
        self.input18.grid(column=3, row=5, sticky=tk.W)

        #Centro de Gravidade

        ttk.Label(self, text='CG2:').grid(
            column=2, row=6, sticky=tk.E)
        self.input19 = ttk.Entry(self, width=10)
        self.input19.focus()
        self.input19.grid(column=3, row=6, sticky=tk.W)

        ttk.Label(self, text='CG3:').grid(column=2, row=7, sticky=tk.E)
        self.input20 = ttk.Entry(self, width=10)
        self.input20.grid(column=3, row=7, sticky=tk.W)

        ttk.Label(self, text='CG4:').grid(column=2, row=8, sticky=tk.E)
        self.input21 = ttk.Entry(self, width=10)
        self.input21.grid(column=3, row=8, sticky=tk.W)

        #Delta de Gravidade

        ttk.Label(self, text='Delta CG2(radianos):').grid(
            column=2, row=9, sticky=tk.E)
        self.input22 = ttk.Entry(self, width=10)
        self.input22.focus()
        self.input22.grid(column=3, row=9, sticky=tk.W)

        ttk.Label(self, text='Delta CG3(radianos):').grid(column=2, row=10, sticky=tk.E)
        self.input23 = ttk.Entry(self, width=10)
        self.input23.grid(column=3, row=10, sticky=tk.W)

        ttk.Label(self, text='Delta CG4(radianos):').grid(column=2, row=11, sticky=tk.E)
        self.input24 = ttk.Entry(self, width=10)
        self.input24.grid(column=3, row=11, sticky=tk.W)


    def get_values(self):

        try:

            elo1 = float(self.input1.get())
            elo2 = float(self.input2.get())
            elo3 = float(self.input3.get())
            elo4 = float(self.input4.get())
            massa2 = float(self.input5.get())
            massa3 = float(self.input6.get())
            massa4 = float(self.input7.get())
            ig2 = float(self.input8.get())
            ig3 = float(self.input9.get())
            ig4 = float(self.input10.get())
            theta2 = int(self.input11.get())
            w2 = int(self.input12.get())
            alpha2 = int(self.input13.get())
            t4 = float(self.input14.get())
            ponto_p = float(self.input17.get())
            fp = float(self.input15.get())
            deltafp = int(self.input16.get())
            deltapp = int(self.input18.get())
            cg2 = float(self.input19.get())
            cg3 = float(self.input20.get())
            cg4 = float(self.input21.get())
            deltacg2 = int(self.input22.get())
            deltacg3 = int(self.input23.get())
            deltacg4 = int(self.input24.get())
           

            return elo1,elo2,elo3,elo4,massa2,massa3,massa4,ig2,ig3,ig4,theta2,w2,alpha2,t4,fp,deltafp,ponto_p,deltapp,cg2,cg3,cg4,deltacg2,deltacg3,deltacg4
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None, None, None,None, None, None, None, None, None,None, None, None, None, None, None,None, None, None, None, None, None






class Frame_analise_cinematica(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # Elos
        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.W)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.focus()
        self.input4.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.W)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.W)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.W)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self, text='W2-Constante(radiano):').grid(
            column=2, row=2, sticky=tk.E)
        self.input8 = ttk.Entry(self, width=10)
        self.input8.grid(column=3, row=2, sticky=tk.W)

        ttk.Label(self, text='Alpha2-Constante(radiano):').grid(
            column=2, row=3, sticky=tk.E)
        self.input9 = ttk.Entry(self, width=10)
        self.input9.grid(column=3, row=3, sticky=tk.W)



    def get_values(self):

        try:

            elo1 = float(self.input4.get())
            elo2 = float(self.input5.get())
            elo3 = float(self.input6.get())
            elo4 = float(self.input7.get())
            w2 = int(self.input8.get())
            alpha2 = int(self.input9.get())
    

            return elo1, elo2, elo3, elo4, w2, alpha2
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None, None, None


class Frame_analise_de_posicao(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Elos
        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.W)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.focus()
        self.input4.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.W)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.W)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.W)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self, text='Theta 2:').grid(column=0, row=4, sticky=tk.W)
        self.input8 = ttk.Entry(self, width=10)
        self.input8.grid(column=1, row=4, sticky=tk.W)

    def get_values(self):

        try:

            elo1 = float(self.input4.get())
            elo2 = float(self.input5.get())
            elo3 = float(self.input6.get())
            elo4 = float(self.input7.get())
            theta = int(self.input8.get())
            return elo1, elo2, elo3, elo4, theta
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None, None


class Frame_analise_de_velocidade(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # Elos
        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.W)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.focus()
        self.input4.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.W)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.W)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.W)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self, text='Theta 2:').grid(
            column=2, row=0, sticky=tk.E)
        self.input8 = ttk.Entry(self, width=10)
        self.input8.grid(column=3, row=0, sticky=tk.W)

        ttk.Label(self, text='W2:').grid(
            column=2, row=1, sticky=tk.E)
        self.input9 = ttk.Entry(self, width=10)
        self.input9.grid(column=3, row=1, sticky=tk.W)

        ttk.Label(self, text='Delta 3:').grid(
            column=2, row=2, sticky=tk.E, padx=2)
        self.input10 = ttk.Entry(self, width=10)
        self.input10.grid(column=3, row=2, sticky=tk.W)

        ttk.Label(self, text='RPA:').grid(
            column=2, row=3, sticky=tk.E)
        self.input11 = ttk.Entry(self, width=10)
        self.input11.grid(column=3, row=3, sticky=tk.W)

    def get_values(self):

        try:

            elo1 = float(self.input4.get())
            elo2 = float(self.input5.get())
            elo3 = float(self.input6.get())
            elo4 = float(self.input7.get())
            theta = int(self.input8.get())
            w2 = int(self.input9.get())
            delta3 = int(self.input10.get())
            rpa = float(self.input11.get())

            return elo1, elo2, elo3, elo4, theta, w2, delta3, rpa
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None, None, None, None, None


class Frame_ponto_psr(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # Elos
        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.W)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.focus()
        self.input4.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.W)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.W)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.W)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self, text='Delta 3:').grid(
            column=2, row=0, sticky=tk.E, padx=2)
        self.input8 = ttk.Entry(self, width=10)
        self.input8.grid(column=3, row=0, sticky=tk.W)

        ttk.Label(self, text='RPA:').grid(
            column=2, row=1, sticky=tk.E)
        self.input9 = ttk.Entry(self, width=10)
        self.input9.grid(column=3, row=1, sticky=tk.W)

    def get_values(self):

        try:

            elo1 = float(self.input4.get())
            elo2 = float(self.input5.get())
            elo3 = float(self.input6.get())
            elo4 = float(self.input7.get())
            delta3 = int(self.input8.get())
            rpa = float(self.input9.get())

            return elo1, elo2, elo3, elo4, delta3, rpa
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None, None, None


class Frame_analise_de_aceleracao(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # Elos
        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.W)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.focus()
        self.input4.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.W)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.W)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.W)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self, text='Theta 2:').grid(
            column=2, row=0, sticky=tk.E)
        self.input8 = ttk.Entry(self, width=10)
        self.input8.grid(column=3, row=0, sticky=tk.W)

        ttk.Label(self, text='W2:').grid(
            column=2, row=1, sticky=tk.E)
        self.input9 = ttk.Entry(self, width=10)
        self.input9.grid(column=3, row=1, sticky=tk.W)

        ttk.Label(self, text='Alpha 2:').grid(
            column=2, row=2, sticky=tk.E, padx=2)
        self.input10 = ttk.Entry(self, width=10)
        self.input10.grid(column=3, row=2, sticky=tk.W)

        ttk.Label(self, text='Delta 3:').grid(
            column=2, row=3, sticky=tk.E, padx=2)
        self.input11 = ttk.Entry(self, width=10)
        self.input11.grid(column=3, row=3, sticky=tk.W)
        ttk.Label(self, text='RPA:').grid(
            column=0, row=4, sticky=tk.E)
        self.input12 = ttk.Entry(self, width=10)
        self.input12.grid(column=1, row=4, sticky=tk.W)

    def get_values(self):

        try:

            elo1 = float(self.input4.get())
            elo2 = float(self.input5.get())
            elo3 = float(self.input6.get())
            elo4 = float(self.input7.get())
            theta = int(self.input8.get())
            w2 = int(self.input9.get())
            alpha2 = int(self.input10.get())
            delta3 = int(self.input11.get())
            rpa = float(self.input12.get())

            return elo1, elo2, elo3, elo4, theta, w2, alpha2, delta3, rpa
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None, None, None, None, None, None


class Frame_Elos_animacao_simples(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        ttk.Label(self, text='Elo 1:').grid(
            column=0, row=0, sticky=tk.W)
        self.input4 = ttk.Entry(self, width=10)
        self.input4.focus()
        self.input4.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Elo 2:').grid(column=0, row=1, sticky=tk.W)
        self.input5 = ttk.Entry(self, width=10)
        self.input5.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Elo 3:').grid(column=0, row=2, sticky=tk.W)
        self.input6 = ttk.Entry(self, width=10)
        self.input6.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Elo 4:').grid(column=0, row=3, sticky=tk.W)
        self.input7 = ttk.Entry(self, width=10)
        self.input7.grid(column=1, row=3, sticky=tk.W)

    def get_values(self):

        try:

            elo1 = float(self.input7.get())
            elo2 = float(self.input4.get())
            elo3 = float(self.input5.get())
            elo4 = float(self.input6.get())
            return elo1, elo2, elo3, elo4
        except ValueError:
            messagebox.showwarning(
                "Aviso", "Preencha todos os campos de entrada corretamente!")
            return None, None, None, None


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Cinemática dos Mecanismos')
        self.geometry('600x550')
        self.resizable(0, 0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)

        self.axes1 = plt.plot([], [], 'r-', linewidth=4)
        self.axes2 = plt.plot([], [], marker='o', ls="", markersize=10)

        self.selected_value = tk.StringVar()

        self.languages = ('Selecione', 'Animação', 'Analise de Posição', 'Plotagem da Curva do Acoplador', 'Plotagem do Angulo de Trasmissão',
                          'Analise de Velocidade', 'Analise de Aceleração','Analise Cinematica do Mecanismo', 'Analise Dinâmica do Mecanismo')
        self.selected_value.set('Animação')
        self.label_opt = ttk.Label(self, text='Selecione o modo de uso:').grid(
            column=0, row=3, sticky=tk.E, padx=5, pady=5)
        self.modo_opt = ttk.OptionMenu(
            self, self.selected_value, self.languages[0], *self.languages, command=self.change_frame).grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        #Telas - Frames
        self.frames1 = Frame_Elos_animacao_simples(self)
        self.frames2 = Frame_analise_de_posicao(self)
        self.frames3 = Frame_analise_de_velocidade(self)
        self.frames4 = Frame_analise_de_aceleracao(self)
        self.frames5 = Frame_ponto_psr(self)
        self.frames6 = Frame_analise_cinematica(self)
        self.frames7 = Frame_analise_dinamica(self)

        # Carregar a imagem
        image = Image.open("Cinematica dos Mecanismo/Trabalho_Nota_3/icon_elos1.jpeg")
        image = image.resize((300, 200))  # Redimensionar a imagem, se necessário

        # Converter a imagem para o formato do Tkinter
        self.photo = ImageTk.PhotoImage(image)

        # Exibir a imagem em um rótulo
        self.label = tk.Label(self, image=self.photo)
        self.label.grid(row=0, column=0, padx=10, pady=10,columnspan=2,sticky=tk.NS)
        
        self.btn1 = ttk.Button(self, text='Gerar', command=self.modo_do_graph).grid(
            column=0, row=5, columnspan=2, padx=5, pady=5)
        self.btn2 = ttk.Button(self, text='Exit', command=self.close_program).grid(
            column=0, row=6, columnspan=2, padx=5, pady=5)

    def change_frame(self, *args, event=None):

        selecao = self.selected_value.get()
        if selecao == "Animação":

            self.frames2.grid_forget()
            self.frames3.grid_forget()
            self.frames4.grid_forget()
            self.frames5.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid_forget()
            self.frames1.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        elif selecao == "Analise de Posição":
            self.frames1.grid_forget()
            self.frames3.grid_forget()
            self.frames4.grid_forget()
            self.frames5.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid_forget()
            self.frames2.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        if selecao == "Analise de Velocidade":

            self.frames1.grid_forget()
            self.frames2.grid_forget()
            self.frames4.grid_forget()
            self.frames5.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid_forget()
            self.frames3.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        if selecao == "Analise de Aceleração":

            self.frames1.grid_forget()
            self.frames2.grid_forget()
            self.frames3.grid_forget()
            self.frames5.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid_forget()
            self.frames4.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        if selecao == "Plotagem do Angulo de Trasmissão":

            self.frames2.grid_forget()
            self.frames3.grid_forget()
            self.frames4.grid_forget()
            self.frames5.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid_forget()
            self.frames1.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        if selecao == "Plotagem da Curva do Acoplador":

            self.frames2.grid_forget()
            self.frames3.grid_forget()
            self.frames4.grid_forget()
            self.frames1.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid_forget()
            self.frames5.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        if selecao == "Analise Cinematica do Mecanismo":
            self.frames2.grid_forget()
            self.frames3.grid_forget()
            self.frames4.grid_forget()
            self.frames5.grid_forget()
            self.frames1.grid_forget()
            self.frames7.grid_forget()
            self.frames6.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        if selecao == "Analise Dinâmica do Mecanismo":
            self.frames2.grid_forget()
            self.frames3.grid_forget()
            self.frames4.grid_forget()
            self.frames5.grid_forget()
            self.frames1.grid_forget()
            self.frames6.grid_forget()
            self.frames7.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        
    
    
    
    def modo_do_graph(self, *args, event=None):

        selecao = self.selected_value.get()
        if selecao == "Animação":
            self.open_animate_graph()
        if selecao == "Analise de Posição":
            self.open_posicao_graph()
        if selecao == 'Analise de Velocidade':
            self.open_velo_graph()
        if selecao == "Analise de Aceleração":
            self.open_acele_graph()
        if selecao == 'Plotagem do Angulo de Trasmissão':
            self.open_plotar_angulo_de_transmisao()
        if selecao == "Plotagem da Curva do Acoplador":
            self.open_plotar_ponto_p()
        if selecao == "Analise Cinematica do Mecanismo":
            self.open_cinematica_analysys()
        if selecao == "Analise Dinâmica do Mecanismo":
            self.open_dinamica_analysys()





    def open_dinamica_analysys(self):
       self.a, self.b, self.c, self.d, self.m2,self.m3,self.m4,self.ig2,self.ig3,self.ig4,self.theta2, self.w2, self.alpha2, self.t4,self.fp,self.deltafp,self.pontop,self.deltapp,self.cg2,self.cg3,self.cg4,self.deltacg2,self.deltacg3,self.deltacg4 = self.frames7.get_values()
       
       fourbar = self.Condition_FBL()
       if ((self.a != None) or  (self.w2 != None)) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Analise Dinâmica de um Mecanismo de 4 barras")
            self.graph.geometry("700x500")

            figure = Figure(figsize=(6, 4))
            self.axes = figure.add_subplot()
            self.axes.set_title('Plotagem da Forca Dinâmica')
            self.axes.set_xlabel('Força / Torque')
            self.axes.set_ylabel('Tempo')
            dinamico,x  = analise_dinâmica(self.theta2,self.w2,self.alpha2,self.t4,self.fp,self.deltafp,self.pontop,self.deltapp,self.cg2,self.cg3,self.cg4,self.deltacg2,self.deltacg3,self.deltacg4,self.a,self.b,self.c,self.d,self.m2,self.m3,self.m4,self.ig2,self.m3,self.m4)
            
            self.axes.plot(x, dinamico['Torque'],label='Torque')
            self.axes.plot(x,dinamico['F12x'],label ='F12x')
            self.axes.plot(x,dinamico['F12y'],label ='F12y')
            self.axes.plot(x,dinamico['F32x'],label ='F32x')
            self.axes.plot(x,dinamico['F32y'],label ='F32y')
            self.axes.plot(x,dinamico['F43x'],label ='F43x')
            self.axes.plot(x,dinamico['F43y'],label ='F43y')
            self.axes.plot(x,dinamico['F14x'],label ='F14x')
            self.axes.plot(x,dinamico['F14y'],label ='F14y')
            self.axes.legend()
            canvas = FigureCanvasTkAgg(figure, master=self.graph)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, padx=5, pady=5)




















    def open_cinematica_analysys(self):
        self.a, self.b, self.c, self.d, self.w2,self.alpha2 = self.frames6.get_values()
        fourbar = self.Condition_FBL()
        if (self.a != None) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Cinematica dos Mecanismo")
            self.graph.geometry("1850x410")
            t = np.arange(0,2*np.pi,0.01)
            MP,MV,MA= analise_cinematica_mecanismo_4_barras(self.a,self.b,self.c,self.d,self.w2,self.alpha2)
            figure1 = Figure(figsize=(6, 4))
            self.axes = figure1.add_subplot()
            self.axes.set_title('Cinematica dos Mecanismo - Curvas dos Angulos de Posição ')
            self.axes.set_ylabel('Angulo de Posição(radianos)')
            self.axes.set_xlabel('Tempo(segundos)')
            self.axes.plot(t,MP["THETA3"], 'r', label='theta3')
            self.axes.plot(t,MP["THETA4"], 'g', label='theta4')
            self.axes.legend()
            canvas = FigureCanvasTkAgg(figure1, master=self.graph)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=1, padx=5, pady=5)
            figure2 = Figure(figsize=(6, 4))
            self.axes1 = figure2.add_subplot()
            self.axes1.set_title('Cinematica dos Mecanismo - Curvas dos Angulos de Velocidade ')
            self.axes1.set_ylabel('Angulo de Velocidade(radianos)')
            self.axes1.set_xlabel('Tempo(segundos)')
            self.axes1.plot(t,MV["W3"], 'y', label='omega3')
            self.axes1.plot(t,MV["W4"], 'c', label='omega4')
            self.axes1.legend()
            canvas1 = FigureCanvasTkAgg(figure2, master=self.graph)
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=7, column=2, padx=5, pady=5)
            figure3 = Figure(figsize=(6, 4))
            self.axes2 = figure3.add_subplot()
            self.axes2.set_title('Cinematica dos Mecanismo - Curvas dos Angulos de Aceleração')
            self.axes2.set_ylabel('Angulo de Aceleração(radianos)')
            self.axes2.set_xlabel('Tempo(segundos)')
            self.axes2.plot(t,MA["ALPHA3"], 'b', label='Alpha3')
            self.axes2.plot(t,MA["ALPHA4"], 'r', label='Alpha4')
            self.axes2.legend()
            canvas2 = FigureCanvasTkAgg(figure3, master=self.graph)
            canvas2.draw()
            canvas2.get_tk_widget().grid(row=7, column=3, padx=5, pady=5)

            
            
    def open_posicao_graph(self):

        self.d, self.a, self.b, self.c, self.theta2 = self.frames2.get_values()
        fourbar = self.Condition_FBL()
        if (self.a != None) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Analise de Posição")
            self.graph.geometry("610x630")

            A, B, C, D, self.theta3a, self.theta4a, self.theta3c, self.theta4c, gammaa, gammac = analise_posicoes(
                self.theta2, self.a, self.b, self.c, self.d, 0)
            x = [A[0], B[0], C[0], D[0]]
            y = [A[1], B[1], C[1], D[1]]

            ttk.Label(master=self.graph, text='Theta 3 - Aberto:' + str(
                np.rad2deg(self.theta3a))).grid(column=0, row=0, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Theta 3 - Cruzado:' + str(
                np.rad2deg(self.theta3c))).grid(column=0, row=1, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Theta 4 - Aberto:' + str(
                np.rad2deg(self.theta4a))).grid(column=0, row=3, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Theta 4 - Cruzado:' + str(
                np.rad2deg(self.theta4c))).grid(column=0, row=4, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Angulo de Tramsmissão - Aberto:' +
                      str(np.rad2deg(gammaa))).grid(column=0, row=5, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Angulo de Tramsmissão - Cruzado:' +
                      str(np.rad2deg(gammac))).grid(column=0, row=6, sticky=tk.W, padx=7, pady=7)
            figure = Figure(figsize=(6, 4))
            self.axes = figure.add_subplot()
            self.axes.set_title('Analise dos Elos')
            self.axes.set_xlabel('Posição')
            self.axes.set_ylabel('Posição')
            self.axes.plot(x, y)

            canvas = FigureCanvasTkAgg(figure, master=self.graph)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, padx=5, pady=5)

    def open_velo_graph(self):

        self.d, self.a, self.b, self.c, self.theta2, self.w2, self.delta3, self.p1 = self.frames3.get_values()
        fourbar = self.Condition_FBL()
        if ((self.a != None) or (self.w2 != None) or (self.p1 != None)) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Analise de Velocidade")
            self.graph.geometry("500x350")

            self.VPa, self.w3a, self.w4a, self.w3c, self.w4c, self.VPc = analise_velocidades(
                self.theta2, self.a, self.b, self.c, self.d, 0, self.p1, self.w2, self.delta3)

            ttk.Label(master=self.graph, text='Velocidade Angular - W3- Aberto:' +
                      str(self.w3a)).grid(column=0, row=1, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Velocidade Angular - W4- Aberto:' +
                      str(self.w4a)).grid(column=0, row=2, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Velocidade Angular - W3- Cruzado:' +
                      str(self.w3c)).grid(column=0, row=3, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Velocidade Angular - W4- Cruzado:' +
                      str(self.w4c)).grid(column=0, row=4, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='VP - Aberto:' + str(np.linalg.norm(self.VPa))
                      ).grid(column=0, row=5, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='VP - Cruzado:' + str(np.linalg.norm(self.VPc))
                      ).grid(column=0, row=6, sticky=tk.W, padx=7, pady=7)

    def open_acele_graph(self):

        self.d, self.a, self.b, self.c, self.theta2, self.w2, self.alpha2, self.delta3, self.p1 = self.frames4.get_values()
        fourbar = self.Condition_FBL()
        if ((self.a != None) or (self.w2 != None) or (self.p1 != None)) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Analise de Aceleração")
            self.graph.geometry("500x350")

            self.APa, self.a3a, self.a4a, self.a3c, self.a4c, self.APc = analise_de_aceleracao(
                self.theta2, self.a, self.b, self.c, self.d, 0, self.p1, self.w2, self.delta3, self.alpha2)

            ttk.Label(master=self.graph, text='Aceleraçao Angular - Alpha3- Aberto:' +
                      str(self.a3a)).grid(column=0, row=1, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Aceleração Angular - ALpha4- Aberto:' +
                      str(self.a4a)).grid(column=0, row=2, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Aceleração Angular - Alpha3- Cruzado:' +
                      str(self.a3c)).grid(column=0, row=3, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='Aceleração Angular - Alpha4- Cruzado:' +
                      str(self.a4c)).grid(column=0, row=4, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='AP - Aberto:' + str(np.linalg.norm(self.APa))
                      ).grid(column=0, row=5, sticky=tk.W, padx=7, pady=7)
            ttk.Label(master=self.graph, text='AP - Cruzado:' + str(np.linalg.norm(self.APc))
                      ).grid(column=0, row=6, sticky=tk.W, padx=7, pady=7)

    def open_plotar_angulo_de_transmisao(self):

        self.d, self.a, self.b, self.c = self.frames1.get_values()
        fourbar = self.Condition_FBL()
        if (self.a != None) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Cinemática dos Mecanismo")
            self.graph.geometry("610x630")
            ya = []
            yc = []
            x = np.arange(0, 4*np.pi, 0.01)
            x1 = np.arange(0, 360, 1)
            for theta in x1:
                A, B, C, D, self.theta3a, self.theta4a, self.theta3c, self.theta4c, gammaa, gammac = analise_posicoes(
                    theta, self.a, self.b, self.c, self.d, 0)
                ya.append(gammaa)
                yc.append(gammac)

            figure = Figure(figsize=(6, 4))
            self.axes = figure.add_subplot()
            self.axes.set_title('Analise dos Elos')
            self.axes.set_ylabel('Angulo de Trasmissão(graus)')
            self.axes.set_xlabel('Theta2(graus)')
            self.axes.plot(x1, ya, 'y', label='gamma - a')
            self.axes.plot(x1, yc, 'r', label='gamma - c')
            self.axes.legend()

            canvas = FigureCanvasTkAgg(figure, master=self.graph)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, padx=5, pady=5)

    def open_plotar_ponto_p(self):

        self.a, self.b, self.c, self.d, self.delta3, self.rpa = self.frames5.get_values()
        fourbar = self.Condition_FBL()
        if (self.a != None) and (fourbar == True):

            self.graph = tk.Toplevel(self)
            self.graph.title("Cinemática dos Mecanismo")
            self.graph.geometry("600x400")

            figure = Figure(figsize=(6, 4))
            self.axes = figure.add_subplot()
            self.axes.set_title('Plotagem da Curva do Acoplador')
            self.axes.set_xlabel('Posição')
            self.axes.set_ylabel('Posição')
            x, y = analise_ponto_p(
                self.a, self.b, self.c, self.d, self.delta3, self.rpa)
            self.axes.plot(x, y)

            canvas = FigureCanvasTkAgg(figure, master=self.graph)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, padx=5, pady=5)

    # Função para Animar os Mecanismos de 4 de barras

    def open_animate_graph(self):

        self.d, self.a, self.b, self.c = self.frames1.get_values()
        fourbar = self.Condition_FBL()
        if (self.a != None) and (fourbar == True):
            self.graph = tk.Toplevel(self)
            self.graph.title("Animação do Mecanismo")
            self.graph.geometry("600x400")
            figure = Figure(figsize=(6, 4))
            canvas = FigureCanvasTkAgg(figure, master=self.graph)
            canvas.get_tk_widget().grid(row=0, column=0)
            theta2 = generate_th2(self.a, self.b, self.c, self.d)
            x1, x2, x3, x4, y1, y2, y3, y4 = calc_joint_position(
                self.a, self.b, self.c, self.d, theta2)
            self.animacao = animate_linkage_motion(
                figure, x1, x2, x3, x4, y1, y2, y3, y4)
            canvas.draw()

    def Condition_FBL(self):
        elos = [self.a, self.b, self.c, self.d]
        self.elos = sorted(elos)  # Ordenar os elos pelo Comprimento

    ######################################
        S = int(self.elos[0])
        L = int(self.elos[3])
        P = int(self.elos[1])
        Q = int(self.elos[2])

        sist, cond = Sistema(L, S, P, Q)
        messagebox.showinfo("Tipo do Sistema", sist)
        if cond == 0:
            messagebox.showerror(
                "Erro", "Não é possivel gerar uma animação para esse tipo de Sistema")
            return False
        elif cond == 1:

            tipog = Grashof(L, S, P, Q, self.a, self.b, self.c, self.d)

            if tipog == "CLASSE III":
                messagebox.showerror(
                    "Erro", "Não é possivel gerar uma animação para esse tipo")
                return False
            else:
                messagebox.showinfo("Grashof", tipog)
        return True

    # Função para Fechar o Programa

    def close_program(self):
        self.destroy()


if __name__ == "__main__":

    app = App()

    app.mainloop()
