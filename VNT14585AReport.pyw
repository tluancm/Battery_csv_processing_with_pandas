from tkinter.constants import TRUE
import PySimpleGUI as sg      
import matplotlib.pyplot as plt#provide way to generate graph
import os# provid way to interact with the OS
from consume_param import cenario1_2
from trans_param import cenario3
from charge_param import cenario4
from charge_param import graph
from discharge_param import cenario5
from discharge_param import graph2
import consume_param
import trans_param
import charge_param
import discharge_param

sg.theme('LightPurple')  # please make your creations colorful

layout = [  [sg.Text('Parâmetros de Consumo:')],
            [sg.Input(key = 'file_in_1', size=(60,1)), sg.FileBrowse( file_types=(("CSV Files", ".*csv"),), size=(8,1))],
            [sg.Input(key = 'file_out_1', size=(60,1)), sg.Text('Output')],
            [sg.Button(button_text='Save', key='consumo', size=(8,1))], 

            [sg.Text('Parâmetros de Transação:')],
            [sg.Input(key="file_in_2", size=(60,1)),sg.FileBrowse(file_types=(("CSV Files", ".*csv"),), size=(8,1))], 
            [sg.Input(key = 'file_out_2', size=(60,1)), sg.Text('Output')],
            [sg.Button(button_text='Save...', key='trans', size=(8,1))],

            [sg.Text('Parâmetros de Carregamento:')],
            [sg.Input(key="file_in_3", size=(60,1)),sg.FileBrowse(file_types=(("CSV Files", ".*csv"),), size=(8,1))], 
            [sg.Input(key = 'file_out_3', size=(60,1)), sg.Text('Output')],
            [sg.Button(button_text='Save...', key='carga', size=(8,1))],

            [sg.Text('Parâmetros de Descarregamento:')],
            [sg.Input(key="file_in_4", size=(60,1)),sg.FileBrowse(file_types=(("CSV Files", ".*csv"),), size=(8,1))], 
            [sg.Input(key = 'file_out_4', size=(60,1)), sg.Text('Output')],
            [sg.Button(button_text='Save...', key='descarga', size=(8,1))],

            [sg.Cancel(button_text='Close', size=(8,1))]
            ]    


window = sg.Window('VNT 14585A Report', layout, finalize= TRUE, location=(500,150), size=(550, 530), icon="dist\\Assets\\vnt_icone.ico")
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
        sg.theme('DarkBlue7')
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

        window2 = sg.Window('VNT 14585A Report Transaction Parameters', layout, finalize= TRUE, modal=True)

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
        sg.theme('DarkBlue7')
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

        window3 = sg.Window('VNT 14585A Report Charge Parameters', layout, finalize= TRUE, modal=True)

        while TRUE:
            event3, values3 = window3.read()
            if (event3 == sg.WINDOW_CLOSED or event3 == 'Close') : 
                break
            elif event3 == 'Save':
                file_in = values['file_in_3']
                file_out = values['file_out_3']
                t1 = cenario4(file_in,file_out,values3)                             
                layout = [[sg.Input(key= 'zerar'), sg.Text('Cut graph from how many seconds?')],
                [sg.Button('Apply', key= 'apply'), sg.Cancel('Cancel', key= 'cancel')]]
                window4 = sg.Window("Graph", layout, modal=True)
                while True:
                    event4, values4 = window4.read()
                    if (event4 == sg.WIN_CLOSED or event4 == 'cancel'):
                        break
                    elif event4 == 'apply':
                        zerar = int(values4['zerar'])   
                        graph(file_out,t1[0], zerar)  
                        break  
                charge_param.saveAsPDF4(file_out, t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7], t1[8], t1[9],t1[10])
                sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")
                window4.close()  
        window3.close()

    elif event == 'descarga':
        sg.theme('DarkBlue7')
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
        window5 = sg.Window('VNT 14585A Report Discharge Parameters', layout, finalize= TRUE, modal=True)
        while TRUE:
            event5, values5 = window5.read()
            if (event5 == sg.WINDOW_CLOSED or event5 == 'Close') : 
                break
            elif event5 == 'Save':
                file_in = values['file_in_4']
                file_out = values['file_out_4']
                t1 = cenario5(file_in,file_out,values5)                             
                layout = [[sg.Input(key= 'zerar'), sg.Text('Cut graph from how many seconds?')],
                [sg.Button('Apply', key= 'apply'), sg.Cancel('Cancel', key= 'cancel')]]
                window6 = sg.Window("Graph", layout, modal=True)
                while True:
                    event6, values6 = window6.read()
                    if (event6 == sg.WIN_CLOSED or event6 == 'cancel'):
                        break
                    elif event6 == 'apply':
                        s = False
                        zerar = int(values6['zerar'])  
                        graph2(file_out,t1[0], zerar) 
                        break   
                discharge_param.saveAsPDF5(file_out, t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7], t1[8], t1[9],t1[10])        
                sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")
                window6.close()  
        window5.close()

window.close()        