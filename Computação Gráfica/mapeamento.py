# UNIVERSIDADE ESTADUAL DO MARANHÃO - UEMA
# CENTRO DE CIÊNCIAS TECNOLÓGICAS - CCT 
# ENGENHARIA DA COMPUTAÇÃO
# ASL092N724 - COMPUTAÇÃO GRÁFICA
# PROFESSORA:  YONARA COSTA MAGALHAES
# PERIODO 2022 - 4 / CADEIRA DE FÉRIAS

# PARTICIPANTES DO GRUPO :
#1- ALINE MARIANA BARROS SILVA 
#2- JADE MOREIRA DE SOUSA 
#3- LUIZ FELIPE FREITAS FERREIRA
#4- NILSON LUCAS PEREIRA ABRANTES
#5- WESLESON SOUZA SILVA





#IMPORTAÇÃO DA BIBLIOTECA DE INTERFACE GŔAFICA USADA NO TRABALHO

from PySimpleGUI import PySimpleGUI as sg


#DEFINIÇÃO DAS FUNÇÕES USADAS NO TRABALHO 

def SRU(xmin, xmax, ymin, ymax):
    return{'Minimo': (xmin, ymin), 'Maximo': (xmax, ymax)}

 
def SRD(xmin, xmax, ymin, ymax):
    return{'Minimo': (xmin, ymin), 'Maximo': (xmax, ymax)}




def Validacao(numero):
    if (numero < 0):
        return False
    return True



def Mapeamento(tipo, SRU, SRD, Ponto):

    erro = False


    try:
       
        if tipo == 1:

            xd = (Ponto[0]*SRD['Maximo'][0])/SRU['Maximo'][0]
            yd = ((Ponto[1]*(-SRD['Maximo'][1])) /
                SRU['Maximo'][1]) + SRD['Maximo'][1]
            


        if tipo == 2:

            xd = (((Ponto[0]-SRU['Minimo'][0])*(SRD['Maximo'][0]) - SRD['Minimo']
                [0])/(SRU['Maximo'][0] - SRU['Minimo'][0])) + SRD['Minimo'][0]
            yd = (((Ponto[1]-SRU['Minimo'][1])*(SRD['Maximo'][1]) - SRD['Minimo']
                [1])/(SRU['Maximo'][1] - SRU['Minimo'][1])) + SRD['Minimo'][1]
        print('\n ----Executando----')  

    except ZeroDivisionError:

        sg.popup('Erro',' O Mapeamento não foi Possivel! Valores Incorretos! ') 
        print('\n --- TENTE NOVAMENTE ---')
        xd = 0
        yd = 0
        erro = True
        return xd,yd
   
    if ( (xd < 0) | (yd < 0 ) | (xd > SRD['Maximo'][0]) | (yd > SRD['Maximo'][1]) ):
       
        sg.popup('Erro',' O Mapeamento não foi Possivel! Valores Incorretos! ') 
        print('\n --- TENTE NOVAMENTE ---')
        xd = 0
        yd = 0
        erro = True

    return xd, yd,erro



def tipo_mapeamento(SRU, SRD):

    if ((SRU['Minimo'][0] == 0) & (SRU['Minimo'][1] == 0) & (SRD['Minimo'][0] == 0) & (SRD['Minimo'][1] == 0)):
        return 1
    return 2



  
#INTERFACE GRÁFICA 

class Interface_Mapeamento():


    def __init__(self):


        sg.theme('GreenTan')
       

        col1 = sg.Column([[sg.Frame('SRU:',
                            [[sg.Column([[sg.Text('Mínimo'), sg.Input('X_min',size=(10,0),key= '-INPUT1-',do_not_clear=True),sg.Input('Y_min',size=(10,0),key= '-INPUT2-',do_not_clear=True) ],[sg.Text('Máximo'), sg.Input('X_max',size=(10,0),key= '-INPUT3-',do_not_clear=True),sg.Input('Y_max',size=(10,0),key= '-INPUT4-',do_not_clear=True) ]],
                         size=(250,45), pad=(0,0))]])]], pad=(0,0), element_justification='c')
        col2 = sg.Column([[sg.Frame('SRD:',
                            [[sg.Column([[sg.Text('Mínimo'), sg.Input('X_min',size=(10,0),key= '-INPUT5-',do_not_clear=True),sg.Input('Y_min',size=(10,0),key= '-INPUT6-',do_not_clear=True) ],[sg.Text('Máximo'), sg.Input('X_max',size=(10,0),key= '-INPUT7-',do_not_clear=True),sg.Input('Y_max',size=(10,0),key= '-INPUT8-',do_not_clear=True) ]],
                         size=(250,45), pad=(0,0))]])]], pad=(0,0), element_justification='c')
        col3 = sg.Column([[sg.Frame('Ponto U:',
                            [[sg.Column([[sg.Text('Ponto_x'), sg.Input('',size=(10,0),key= '-INPUT9-',do_not_clear=True)],[sg.Text('Ponto_y'), sg.Input('',size=(10,0),key= '-INPUT10-',do_not_clear=True)]],
                         size=(250,45), pad=(75,0))]])]], pad=(75,0), element_justification='c')


       
        menu_layout = [['&Options', ['&Help', '&About']],['&Informações', ['&Para que?', '&Como?']]]

        layout = [
        [sg.Menu(menu_layout, tearoff=True, font='_ 12', key='-MENUBAR-')],
        [sg.Text('MAPEAMENTO DE SISTEMAS DE COORDENADAS', size=(35, 3),pad=(150,5))],[col1,col2],[col3],
        [sg.Button('Converter',pad=(210,5), key='-CONVERTER-')],
        [sg.Output(size=(50,50),pad=(75,0))]
        
                 ]
                

        self.janela = sg.Window(' MAPEAMENTO ',layout=layout,size = (550,500))
 


    def Iniciar(self):
 
        while True: 

            self.button ,self.values = self.janela.Read()
        
            if self.button in (sg.WIN_CLOSED, 'Exit'):
                break
       
            if self.button == 'About':
    
                self.janela.disappear()
                sg.popup('About this program', 'Version 1.0', 'PySimpleGUI Version', sg.get_versions())
                self.janela.reappear()
            
            if self.button == 'Help':
 
                self.janela.disappear()
                sg.popup('Help','Para Qualquer Problema Envie um mensagem para o Grupo')
                self.janela.reappear()

            if self.button == 'Para que?':
    
                self.janela.disappear()
                sg.popup('Por que fazer Transformações entre Sistemas de coordenadas?', ''' ◉ Aplicações gráficas frequentemente requerem a transformação de descrições de objetos de um sistema de coordenadas para outro.''',''' ◉  O objeto às vezes é descrito em um sistema de coordenadas não-cartesiano como as coordenadas polares ou elípticas), e precisa ser convertido para o sistema de coordenadas Cartesianas.''',''' ◉ Em aplicações de animação e modelagem, objetos individuais são definidos em seu próprio sistema de coordenadas, e as coordenadas locais devem ser transformadas para posicionar os objetos no sistema de coordenadas global da cena. ''',''' ◉ Quando se cria um modelo as informações gráficas geométricas dizem respeito à aplicação e não ao dispositivo.''','''◉ Para visualizar dados em um dispositivo gráfico qualquer, é necessário que se efetue algumas transformações entre os sistemas de referência apresentados.Para tal é preciso definir as razões e proporções entre cada um dos sistemas.''','''◉ Para permitir a visualização do modelo faz-se necessário realizar uma conversão dos valores do modelo ou do seu universo para valores compatíveiscom as dimensões da tela (SRU → SRD).''',''' ◉ A este processo de conversão é dá-se o nome de Mapeamento e é uma das etapas do processo de visualização de imagens 2D e 3D.''')
                self.janela.reappear()

            if self.button == 'Como?':
    
                self.janela.disappear()
                sg.popup('Como funciona o Mapeamento?', '''◉ A forma mais simples para representar cada sistema de coordenadas a se fazer a correspondência é sempre fazer isto apenas por 2 pontos: o ponto mínimo e o ponto máximo''','''TIPO 1 - COM MÍNIMOS IGUAIS A ZERO TEMOS: XD = XU * XDMAX/XUMAX  E YD = (YU*(-YDMAX)/ YUMAX ) + YDMAX  ''','''TIPO 2- SE OS MÍNIMOS NÃO FOREM ZERO TEMOS : XD=[(Xu-Xumin) (XDMAX-XDmin)/(XuMAX-Xumin)]+XDmin) e YD=[(Yu-Yumin) (YDMAX-YDmin)/(YuMAX-Yumin)]+YDmin)''')
                self.janela.reappear()

            if self.button == '-CONVERTER-':
               
    
                    try:
                
                        xminU = int(self.values['-INPUT1-'])
                        xmaxU = int(self.values['-INPUT3-'])
                        yminU = int(self.values['-INPUT2-'])
                        ymaxU = int(self.values['-INPUT4-'])

                        xminD = int(self.values['-INPUT5-'])
                        xmaxD = int(self.values['-INPUT7-'])
                        yminD = int(self.values['-INPUT6-'])
                        ymaxD = int(self.values['-INPUT8-'])


                        xu = int(self.values['-INPUT9-'])
                        yu = int(self.values['-INPUT10-'])
                  
                           
                        if (Validacao(int(xminU)) & Validacao(int(xmaxU)) & Validacao(int(yminU)) & Validacao(int(ymaxU)) &Validacao(int(xminD)) & Validacao(int(xmaxD)) & Validacao(int(yminD)) & Validacao(int(ymaxD)) & Validacao(int(xu)) & Validacao(int(yu))) == True:
                            
                            SRUs = SRU(int(xminU), int(xmaxU), int(yminU),int(ymaxU))
                            SRDs = SRD(int(xminD), int(xmaxD), int(yminD),int(ymaxD))
                            Ponto = (int(xu), int(yu))  

        

                            xd, yd,erro = Mapeamento(tipo_mapeamento(SRUs,SRDs), SRUs,SRDs,Ponto)
                            Pontod = (int(xd), int(yd))

                            if( erro == False ):
                                
                                print("\n --- MAPEAMENTO CONCLUIDO COM SUCESSO!---")
                                print('\n ---SRU---')
                                print('\n SRU - Xmin:',xminU)
                                print('\n SRU - Xmax:',xmaxU)
                                print('\n SRU - Ymin:',yminU)
                                print('\n SRU - Ymax:',ymaxU)
                                print('\n ---SRD---')
                                print('\n SRD - Xmin:',xminD)
                                print('\n SRD - Xmax:',xmaxD)
                                print('\n SRD - Ymin:',yminD)
                                print('\n SRD - Ymax:',ymaxD)

                                print('\n Ponto Dado:',Ponto)
                                print('\n Ponto no novo SC: ', Pontod)
                      
                        else:
                                
                            sg.popup('Erro',' Algum Valor foi  Digitado no Formato Errado! ')      

                    except ValueError:
                                
                        sg.popup('Erro',' Algum Valor foi Valor Digitado no Formato Errado! ')  
                                
                

        

tela = Interface_Mapeamento()

tela.Iniciar()




