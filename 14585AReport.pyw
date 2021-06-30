from tkinter.constants import TRUE
import PySimpleGUI as sg      
import matplotlib.pyplot as plt#provide way to generate graph
import os# provid way to interact with the OS
from consume_param import cenario1_2
from trans_param import cenario3

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

            [sg.Cancel(button_text='Cancel')]
            ]    


window = sg.Window('14585 Report C01-02', layout, finalize= TRUE, location=(0,0), size=(550, 550))
if not os.path.exists('Relatórios'):
            os.mkdir(r'Relatórios')#create directory
while TRUE:
    event, values = window.read()
    if (event == sg.WINDOW_CLOSED or event == 'Cancel') : 
        break
    elif event == 'consumo':
        file_in = values['file_in_1']
        file_out = values['file_out_1']
        cenario1_2(file_in, file_out) 
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
                cenario3(file_in, file_out, values2)
        window2.close()    
    # elif event == 'carga':
    #     charge_param()
    # elif event == 'descarga':
    #     discharge_param()
window.close()        