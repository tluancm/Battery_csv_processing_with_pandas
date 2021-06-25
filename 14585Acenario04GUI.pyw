from tkinter.constants import TRUE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Checkbox, Input 
import pandas as pd#provide way to process a csv file
import matplotlib.pyplot as plt#provide way to generate graph
from fpdf import FPDF# print output as pdf file
import sys#provide access to variable wich interact with the phyon interpreter
import os# provid way to interact with the OS
import time#can read times input as hh:mm:ss

def saveAsPDF():#print output as pdf file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    pdf.set_font('Times', 'B', 12)
    epw = pdf.w -2*pdf.l_margin#widht of page minus 2x the margin, make possible to create cells with wide from margin to margin
    cold_widht = epw/4#adjusting the columns width size to fit on page

    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border =1, txt= 'Tensão média [V]' )
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1, txt= 'Tensão miníma [V]')
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= 'Tensão máxima [V]' )
    pdf.cell(w= cold_widht+18, h= 6,align = 'C', border= 1, ln=1,txt= 'Tempo de carregamento [hh:mm:ss]' )

    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= f'{media}' )
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= f'{minimo}')
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= f'{maximo}' )
    pdf.cell(w= cold_widht+18, h= 6,align = 'C', border= 1, ln=1,txt= f'{t_carga}' )

    pdf.cell(w = 0, h= 6,border= 0,align = 'C', ln= 1, txt='' )
    cold_widht2 = epw/3
    cold_widht3 = epw/4
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= ' ' )
    pdf.cell(w= 2*cold_widht3, h= 6,align = 'C', border= 1,txt= 'Tempo' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C',ln=1, border= 1,txt= ' ' )
    
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= 'Barras #' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= 's' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= 'hh:mm:ss' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C',ln= 1, border= 1,txt= 'Bateria[%]')
    if (flag == TRUE):
        for k in range(0, barras):
            pdf.cell(w = cold_widht3, h= 6,align = 'C', border=1, txt= f'{k+1}' )
            pdf.cell(w = cold_widht3, h=6,align = 'C', border=1, txt= f'{t_conv_list[k]}')
            pdf.cell(w = cold_widht3, h= 6,align = 'C', border=1, txt= f'{t_header[k]}')
            pdf.cell(w = cold_widht3, h=6,align = 'C', border= 1, ln=1, txt= f'{battery[k]}')
    else: 
        pdf.multi_cell(w =0, h=5, border= 1, txt= f'{comment}')        

    pdf.image(f'Relatórios\\{file_out}.jpg',x = -10, y = 100, w =225, h = 150)
    pdf.output(f"Relatórios\\{file_out}.pdf",'F')

def saveAstxt():#open a txt file and write the results
    sys.stdout = open(f"Relatórios\\{file_out}.txt", 'wt')#open file to write
    print(text)
    sys.stdout.close()      

sg.theme('Reddit')
layout = [[sg.Text('CSV File')],
            [sg.Input(key = 'file_in'), sg.FileBrowse(initial_folder= 'C:\\Users\\VNTTAMA\\Desktop\\logs-csv', file_types=(("CSV Files", ".*csv"),))], 
            [sg.Input(key = 'file_out'), sg.Text('File out')],
            [sg.Checkbox('É possível obter a carga pelo header?', key= '-IN-')],
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

window = sg.Window('14585 Report C04', layout, finalize= TRUE)

while TRUE:
    event, values = window.read()
    if (event == sg.WINDOW_CLOSED or event == 'Close') : 
        break
    elif event == 'Save':
        if not os.path.exists('Relatórios'):
            os.mkdir(r'Relatórios')#create directory
        file_in = values['file_in']
        file_out = values['file_out']

        df = pd.read_csv(file_in,skiprows=(3))#convert csv to dataframe
        df['Time'] = df['Time'].round(decimals = 1)
        df2 = df.rename(columns = {'File1 Instrument A Channel 1 Voltage Avg': "Tensão"}, inplace= False)#create df2 with df renamed columns
        df3 = df2.set_index('Time')#create df3 with df2 time columns as index
        df4 = pd.DataFrame(df3, columns = ["Tensão"])#create a df4 subdataframe with df3 columns "Tensão"

        df4['Bateria[%]'] = (df4["Tensão"]-df4["Tensão"].min())*100/(df4["Tensão"].max()-df4["Tensão"].min())#calculate the battery %charge
        df5 = pd.DataFrame(df4, columns = ['Bateria[%]'])#create a subdataframe df5 with df4 "Bateria [%]" column

        df5.plot( grid = True, legend = False, figsize = (19.20,10.80))
        plt.xlabel('tempo [s]', fontsize=22)
        plt.ylabel('Bateria [%]', fontsize=22)
        plt.suptitle(f'{file_out}'+" gráfico", fontsize= 26)
        plt.savefig(f'Relatórios\\{file_out}.jpg', dpi = 600)
        plt.show()

        media = (round(df4["Tensão"].mean(), 5)) 
        minimo = (round(df4["Tensão"].min(), 5))
        maximo = (round(df4["Tensão"].max(), 5))
        max_index = df4.index[df4["Tensão"] == df4["Tensão"].max()]#calculate the max voltage on column "Tensão"
        max_index_list = max_index.tolist()#create a list with every max voltage index
        t_carga = time.strftime('%H:%M:%S', time.gmtime(max_index_list[0]))#take the first time with the lowest voltage and convert to h:m:s format

        flag = False
        if (values['-IN-'] == TRUE):
            t_header =[]
            flag = TRUE
            t_conv_list = []
            battery = []
            barras = int(values['barras'])  
            for k in range(0, barras):
                t_convert = values[f't_header_{k}']#input time to reach a certain header on a hh:mm:ss format 
                t_header.append(t_convert)#convert input to seconds
                h, m, s = t_convert.split(':')
                t_convert2 = int(h)*3600 + int(m)*60 + int(s)
                t_conv_list.append(t_convert2)#will be printed on pdf as seconds and hh:mm:ss 
                battery.append(df5.iloc[t_convert2, 0])#loaclize battery % in dataframe and save in a list    
            battery = [int(round(n, 0)) for n in battery ]#printed as integer
        else:
            comment = values['comment']#if not is possible to read the header battery % the user input a comment    


        layout = [[sg.Input(key= 'zerar'), sg.Text('Truncar gráfico a partir de quantos segundos')],
        [sg.Button('Truncar'), sg.Cancel('Não truncar')]]
        window = sg.Window("Second Window", layout, modal=True)
        while True:
            event, values = window.read()
            if (event == sg.WIN_CLOSED or event == 'Não Truncar'):
                break
            elif event == 'Truncar':
                zerar = int(values['zerar'])
                df5 = df5.drop(range(zerar, int(df5.index[-1])+1))
                df5.plot( grid = True, legend = False, figsize = (19.20,10.80))
                plt.xlabel('tempo [s]', fontsize=22)
                plt.ylabel('Bateria [%]', fontsize=22)
                plt.suptitle(f'{file_out}'+" gráfico", fontsize= 26)
                plt.savefig(f'Relatórios\\{file_out}.jpg', dpi = 600)
                plt.show()            
                break
            window.close()       

        saveAsPDF()
        sg.popup(f"Salvos na pasta Relatórios: \n{file_out}.png\n{file_out}.pdf\n{file_out}.txt")
        text = {'Tensao média': media, 'Tensão miníma': minimo, 'Tensão máxima': maximo, 'Tempo de carregamento': t_carga}
        saveAstxt()