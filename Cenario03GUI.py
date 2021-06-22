from tkinter.constants import TRUE
import PySimpleGUI as sg  
import pandas as pd#provide way to process a csv file
import matplotlib.pyplot as plt#provide way to generate graph
from fpdf import FPDF# print output as pdf file
import sys#provide access to variable wich interact with the phyon interpreter
import os# provid way to interact with the OS
import statistics as sts#can operate easily on lists

def saveAsPDF():#print output as pdf file
    pdf = FPDF()
    pdf.add_page()
    epw = pdf.w -2*pdf.l_margin#widht of page minus 2x the margin, make possible to create cells with wide from margin to margin
    col_widht = epw/5 -3#adjusting the columns width size to fit on page
    col_widht2 = epw/3
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    pdf.set_font('Times', 'B', 12)

    pdf.cell(w = col_widht, h =6, border = 1, align = 'C',  txt = "Transação #" )
    pdf.cell(w = col_widht, h =6, border =1, align = 'C', txt = "Início [s]")
    pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = "Fim [s]")
    pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = "Duração [s]")
    pdf.cell(w = col_widht+12, h =6, border =1,ln =1, align = 'C', txt = "Corrente média [mA]")
    for k in range(0,5):
        i = k+1
        pdf.cell(w = col_widht, h =6, border = 1, align = 'C',  txt = f"{i}" )
        pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = f"{ti[k]}")
        pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = f"{tf[k]}")
        pdf.cell(w = col_widht, h =6, border =1, align = 'C', txt = f"{dt[k]}")
        pdf.cell(w = col_widht+12, h =6, border =1,ln =1, align = 'C', txt = f"{mean2[k]}")
    pdf.cell(w =  3*col_widht, h = 6, border = 1, align = 'C', txt = "Média")
    pdf.cell(w = col_widht, h = 6, border = 1, align= 'C', txt = f"{dt_mean}" )
    pdf.cell(w = col_widht+12, h = 6, border= 1,ln= 1, align= 'C', txt=f"{mean_t}" )

    pdf.cell(w = 0, h= 6,border= 0, ln= 1, txt='' )

    pdf.cell(w = col_widht2,h= 6, border= 1,align= 'C', txt= "Transação #" )
    pdf.cell(w = col_widht2,h= 6, border= 1,align= 'C', txt= "Corrente 1ª via [mA]" )
    pdf.cell(w = col_widht2,h= 6, border= 1, ln=1, align= 'C', txt= "Corrente 2ª via [mA]" )
    for k in range(0,5):
        i = k+1
        pdf.cell(w = col_widht2, h =6, border = 1, align = 'C',  txt = f"{i}" )
        pdf.cell(w = col_widht2, h =6, border =1, align = 'C',  txt = f"{imp1[k]}")
        pdf.cell(w = col_widht2, h =6, border =1,ln= 1,  align = 'C',  txt = f"{imp2[k]}")
    pdf.cell(w = col_widht2, h= 6, border = 1, align= 'C', txt= 'Média')    
    pdf.cell(w = col_widht2, h= 6,border= 1, align= 'C', txt= f'{mean_imp1}' )
    pdf.cell(w = col_widht2, h= 6,border= 1, align= 'C', txt= f'{mean_imp2}' )
    pdf.image(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg',x = -10, y = 125, w =225, h = 150)
    pdf.output(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\pdf\\{file_out}.pdf','F')

def saveAstxt():#open a txt file and write the results
    os.chdir(r'C:\Users\VNTTAMA\Desktop\Relatorios\txt')#create directory
    sys.stdout = open(f"{file_out}.txt", 'wt')#open file to write
    print(text)
    sys.stdout.close()

    sg.theme('Reddit')  # please make your creations colorful

sg.theme('Reddit')

layout = [  [sg.Text('CSV File')],
            [sg.Input(key = 'file_in'), sg.FileBrowse(initial_folder= 'C:\\Users\\VNTTAMA\\Desktop\\logs-csv', file_types=(("CSV Files", ".*csv"),))], 
            [sg.Input(key = 'file_out'), sg.Text('File out')],
            [sg.Checkbox('Modelo com impressão?', default= False, key= '-IN-')],
            
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


window = sg.Window('14585 Report C03', layout, finalize= TRUE)

while TRUE:
    event, values = window.read()
    if (event == sg.WINDOW_CLOSED or event == 'Close') : 
        break
    elif event == 'Save':
        file_in = values['file_in']
        file_out = values['file_out']
        ti =[]
        tf = []
        dt = []
        imp1 = []
        imp2 = []
        for k in range (0,5):
            ti.append(int(values[f'ti_{k}']))
            tf.append(int(values[f'tf_{k}']))

            if (values['-IN-'] == True):

                imp1.append(float(values[f'imp1_{k}']))
                imp2.append(float(values[f'imp2_{k}']))
                
            else:    
                imp1.append('-')
                imp2.append('-')

        for k in range(0,5):    
            dt.append(tf[k] - ti[k])
        if (values['-IN-'] == True):#Calculate the terminal print mean
            mean_imp1 = round(sts.mean(imp1), 3)
            mean_imp2 = round(sts.mean(imp2), 3)
            
        else:
            mean_imp1 = '-'#if not a printer terminal print "-" on pdf
            mean_imp2 = '-' 

        dt_mean = sts.mean(dt)#calculate the mean of transaction time
        ti_m = [c*2 for c in ti]#convert the time inputs to represent your associated index   
        tf_m = [c*2 for c in tf]

        df = pd.read_csv(file_in,skiprows=(3))#convert csv to dataframe
        df['Time'] = df['Time'].round(decimals = 1)
        df2 = df.rename(columns = {'Active Instrument A Channel 3 Current Avg': "Corrente"}, inplace= False)#rename the column "Corrente"
        df3 = df2.set_index('Time')#create df3 with index seted as "Time" column from df2
        df3["Corrente"] = df3["Corrente"].multiply(1000)
        df4 = pd.DataFrame(df3, columns = ["Corrente"])#create a subdataframe df4 with column "Corrente" from df3

        mean = []

        for k in range(0, 5):#localize the transaction times based on time index
            mean.append(df4.iloc[ti_m[k]:tf_m[k]+1,0].mean())
        mean2 = [round(n, 3) for n in mean ] #create a list with rounded values from variable mean
        mean_t = round(sts.mean(mean), 3)#create a variable with the currente mean on transaction

        df4.plot( grid = True, legend = False, figsize = (19.20,10.80))
        plt.xlabel('tempo [s]', fontsize=22)
        plt.ylabel('Corrente [mA]', fontsize=22)
        plt.suptitle(f'{file_out}'+" gráfico", fontsize= 26)
        plt.savefig(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg', dpi = 600)

        df4["Corrente"] = df4["Corrente"].multiply(1/1000)#variables will be presented as Ampere unity
        media = (round(df4["Corrente"].mean(), 5))
        minimo = (round(df4["Corrente"].min(), 5))
        maximo = (round(df4["Corrente"].max(), 5))

        saveAsPDF()

        sg.popup(f"{file_out}.png foi salvo em Relatorios\imagens\n{file_out}.pdf foi salvo em Relatorios\pdf\n{file_out}.txt foi salvo em Relatorios"+'\\txt')       
        text = {'Corrente média': media, 'Corrente minima': minimo, 'Corrente máxima': maximo, 
        'Duração transação 1':dt[0], 'Duração transação 2':dt[1], 'Duração transação 3':dt[2], 'Duração transação 4':dt[3], 'Duração transação 5':dt[4],
        'Corrente media transação 1': mean2[0], 'Corrente media transação 2': mean2[1],'Corrente media transação 3': mean2[2],
        'Corrente media transação 4': mean2[3],'Corrente media transação 5': mean2[4], 'Média das correntes de transação': mean_t, 
        'Corrente 1ª via #1': imp1[0], 'Corrente 1ª via #2': imp1[1], 'Corrente 1ª via #3': imp1[2], 'Corrente 1ª via #4': imp1[3],
        'Corrente 1ª via #5': imp1[4], 'Média da corrente de 1ª via': mean_imp1, 'Corrente 2ª via 1': imp2[0], 'Corrente 2ª via #2': imp2[1],  
        'Corrente 2ª via #3': imp2[2],'Corrente 2ª via #4': imp2[3],  'Corrente 2ª via #5': imp2[4], 'Média da corrente de 2ª via': mean_imp2
        }
        saveAstxt()
window.close()    
