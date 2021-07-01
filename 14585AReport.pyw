from tkinter.constants import TRUE
import PySimpleGUI as sg      
import matplotlib.pyplot as plt#provide way to generate graph
import os# provid way to interact with the OS
from consume_param import cenario1_2
from trans_param import cenario3
from charge_param import cenario4
import pandas as pd
from charge_param import graph
from discharge_param import cenario5
from discharge_param import graph2
import consume_param
import trans_param
import charge_param
import discharge_param

sg.theme('Reddit')  # please make your creations colorful

layout = [  [sg.Text('Consumo')],
            [sg.Input(key = 'file_in_1'), sg.FileBrowse( file_types=(("CSV Files", ".*csv"),))],
            [sg.Input(key = 'file_out_1'), sg.Text('Output')],
            [sg.Button(button_text='Save', key='consumo')], 

            [sg.Text('Transação')],
            [sg.Input(key="file_in_2"),sg.FileBrowse()], 
            [sg.Input(key = 'file_out_2'), sg.Text('Output')],
            [sg.Button(button_text='Save...', key='trans')],

            [sg.Text('Carregamento:')],
            [sg.Input(key="file_in_3"),sg.FileBrowse()], 
            [sg.Input(key = 'file_out_3'), sg.Text('Output')],
            [sg.Button(button_text='Save...', key='carga')],

            [sg.Text('Descarregamento:')],
            [sg.Input(key="file_in_4"),sg.FileBrowse()], 
            [sg.Input(key = 'file_out_4'), sg.Text('Output')],
            [sg.Button(button_text='Save...', key='descarga')],

            [sg.Cancel(button_text='Close')]
            ]    


window = sg.Window('14585 Report', layout, finalize= TRUE, location=(0,0), size=(550, 550))
if not os.path.exists('Relatórios'):
            os.mkdir(r'Relatórios')#create directory
while TRUE:
    event, values = window.read()
    if (event == sg.WINDOW_CLOSED or event == 'Close') : 
        break
    elif event == 'consumo':
        file_in = values['file_in_1']
        file_out = values['file_out_1']
        t1 = cenario1_2(file_in, file_out)
        consume_param.saveAsPDF1(file_out, t1[0], t1[1], t1[2])
        sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")

    elif event == 'trans':
        sg.theme('Reddit')
        layout = [[sg.Checkbox('Modelo com impressão?', default= False, key= '-IN-')],
            
            [sg.Text('Transação 1')],
            [sg.Input(key = 'ti_0', size=(3, 1)), sg.Text('Início [s]')],
            [sg.Input(key = 'tf_0', size=(3, 1)), sg.Text('Fim [s]' )],
            [sg.Input(key = 'imp1_0', size=(8, 1)), sg.Text('Corrente na 1ª via [mA]')],
            [sg.Input(key = 'imp2_0', size=(8, 1)), sg.Text('Corrente na 2ª via [mA]')],

            [sg.Text('Transação 2')],
            [sg.Input(key = 'ti_1', size=(3, 1)), sg.Text('Início [s]')],
            [sg.Input(key = 'tf_1', size=(3, 1)), sg.Text('Fim [s]')],
            [sg.Input(key = 'imp1_1', size=(8, 1)), sg.Text('Corrente na 1ª via [mA]')],
            [sg.Input(key = 'imp2_1', size=(8, 1)), sg.Text('Corrente na 2ª via [mA]')],

            [sg.Text('Transação 3')],
            [sg.Input(key = 'ti_2', size=(3, 1)), sg.Text('Início [s]')],
            [sg.Input(key = 'tf_2', size=(3, 1)), sg.Text('Fim [s]')],
            [sg.Input(key = 'imp1_2', size=(8, 1)), sg.Text('Corrente na 1ª via [mA]')],
            [sg.Input(key = 'imp2_2', size=(8, 1)), sg.Text('Corrente na 2ª via [mA]')],

            [sg.Text('Transação 4')],
            [sg.Input(key = 'ti_3', size=(3, 1)), sg.Text('Início [s]')],
            [sg.Input(key = 'tf_3', size=(3, 1)), sg.Text('Fim [s]')],
            [sg.Input(key = 'imp1_3', size=(8, 1)), sg.Text('Corrente na 1ª via [mA]')],
            [sg.Input(key = 'imp2_3', size=(8, 1)), sg.Text('Corrente na 2ª via [mA]')],

            [sg.Text('Transação 5')],
            [sg.Input(key = 'ti_4', size=(3, 1)), sg.Text('Início [s]')],
            [sg.Input(key = 'tf_4', size=(3, 1)), sg.Text('Fim [s]')],
            [sg.Input(key = 'imp1_4', size=(8, 1)), sg.Text('Corrente na 1ª via [mA]')],
            [sg.Input(key = 'imp2_4', size=(8, 1)), sg.Text('Corrente na 2ª via [mA]')],

            [sg.Button('Save'), sg.Cancel(button_text='Close')]] 

        window2 = sg.Window('14585 Report C03', layout, finalize= TRUE)

        while TRUE:
            event2, values2 = window2.read()
            if (event2 == sg.WINDOW_CLOSED or event2 == 'Close') : 
                break
            elif event2 == 'Save':
                file_in = values['file_in_2']
                file_out = values['file_out_2']
                t1 = cenario3(file_in, file_out, values2)
                trans_param.saveAsPDF3(file_out,t1[0],t1[1],t1[2],t1[3],t1[4],t1[5],t1[6],t1[7],t1[8],t1[9])
                sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")
        window2.close()    

    elif event == 'carga':
        sg.theme('Reddit')
        layout = [[sg.Checkbox('É possível obter a carga pelo header?', key= '-IN-')],
            [sg.Text('Comentário')],
            [sg.Multiline(key= 'comment', size=(50,5), default_text='Comente caso não seja possível.')],
            
            [sg.Input(key= 'barras', size=(1,1)),sg.Text('Quantidade de barras no header:')],
            
            [sg.Input(key= 't_header_0', size=(8,1)), sg.Text('Tempo para atingir 1 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_1', size=(8,1)), sg.Text('Tempo para atingir 2 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_2', size=(8,1)), sg.Text('Tempo para atingir 3 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_3', size=(8,1)), sg.Text('Tempo para atingir 4 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_4', size=(8,1)), sg.Text('Tempo para atingir 5 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_5', size=(8,1)), sg.Text('Tempo para atingir 6 Barras [hh:mm:ss]')],  
            [sg.Button('Save'), sg.Cancel(button_text='Close')],
            ]    

        window3 = sg.Window('14585 Report C04', layout, finalize= TRUE)

        while TRUE:
            event3, values3 = window3.read()
            if (event3 == sg.WINDOW_CLOSED or event3 == 'Close') : 
                break
            elif event3 == 'Save':
                file_in = values['file_in_3']
                file_out = values['file_out_3']
                t1 = cenario4(file_in,file_out,values3)                             
                layout = [[sg.Input(key= 'zerar'), sg.Text('Truncar gráfico a partir de quantos segundos')],
                [sg.Button('Truncar'), sg.Cancel('Não truncar')]]
                window4 = sg.Window("Graph", layout, modal=True)
                while True:
                    event4, values4 = window4.read()
                    if (event4 == sg.WIN_CLOSED or event4 == 'Não truncar'):
                        break
                    elif event4 == 'Truncar':
                        s = False
                        zerar = int(values4['zerar'])   
                        break
                graph(file_out,t1[0], zerar, s)    
                charge_param.saveAsPDF4(file_out, t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7], t1[8], t1[9],t1[10])
                sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")
                window4.close()  
        window3.close()

    elif event == 'descarga':
        sg.theme('Reddit')
        layout = [[sg.Checkbox('É possível obter a carga pelo header?', key= '-IN-')],
            [sg.Text('Comentário')],
            [sg.Multiline(key= 'comment', size=(50,5), default_text='Comente caso não seja possível.')],
            
            [sg.Input(key= 'barras', size=(1,1)),sg.Text('Quantidade de barras no header:')],
            
            [sg.Input(key= 't_header_5', size=(8,1)), sg.Text('Tempo para atingir 5 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_4', size=(8,1)), sg.Text('Tempo para atingir 4 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_3', size=(8,1)), sg.Text('Tempo para atingir 3 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_2', size=(8,1)), sg.Text('Tempo para atingir 2 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_1', size=(8,1)), sg.Text('Tempo para atingir 1 Barras [hh:mm:ss]')],
            [sg.Input(key= 't_header_0', size=(8,1)), sg.Text('Tempo para atingir 0 Barras [hh:mm:ss]')],  
            [sg.Button('Save'), sg.Cancel(button_text='Close')],
            ]    
        window5 = sg.Window('14585 Report C04', layout, finalize= TRUE)
        while TRUE:
            event5, values5 = window5.read()
            if (event5 == sg.WINDOW_CLOSED or event5 == 'Close') : 
                break
            elif event5 == 'Save':
                file_in = values['file_in_4']
                file_out = values['file_out_4']
                t1 = cenario5(file_in,file_out,values5)                             
                layout = [[sg.Input(key= 'zerar'), sg.Text('Truncar gráfico a partir de quantos segundos')],
                [sg.Button('Truncar'), sg.Cancel('Não truncar')]]
                window6 = sg.Window("Graph", layout, modal=True)
                while True:
                    event6, values6 = window6.read()
                    if (event6 == sg.WIN_CLOSED or event6 == 'Não truncar'):
                        break
                    elif event6 == 'Truncar':
                        s = False
                        zerar = int(values6['zerar'])  
                        break
                graph2(file_out,t1[0], zerar, s)    
                discharge_param.saveAsPDF5(file_out, t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7], t1[8], t1[9],t1[10])        
                sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")
                window6.close()  
        window5.close()

window.close()        