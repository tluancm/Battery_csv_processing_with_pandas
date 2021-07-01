from tkinter.constants import TRUE
import pandas as pd
import matplotlib.pyplot as plt
import sys
from fpdf import FPDF
import PySimpleGUI as sg      
import os
import statistics as sts#can operate easily on lists

def saveAsPDF3(file_out, ti,tf,dt,mean2,dt_mean,mean_t,imp1,imp2,mean_imp1,mean_imp2):#print output as pdf file
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
    pdf.image(f'Relatórios\\{file_out}.jpg',x = -10, y = 125, w =225, h = 150)
    pdf.output(f'Relatórios\\{file_out}.pdf','F')

def saveAstxt3(file_out, text):#open a txt file and write the results
    sys.stdout = open(f"Relatórios\\{file_out}.txt", 'wt')#open file to write
    print(text)
    sys.stdout.close()


def cenario3(file_in, file_out,values2):
    ti =[]
    tf = []
    dt = []
    imp1 = []
    imp2 = []
    for k in range (0,5):
        ti.append(int(values2[f'ti_{k}']))
        tf.append(int(values2[f'tf_{k}']))

        if (values2['-IN-'] == True):

            imp1.append(float(values2[f'imp1_{k}']))
            imp2.append(float(values2[f'imp2_{k}']))
                    
        else:    
            imp1.append('-')
            imp2.append('-')

    for k in range(0,5):    
        dt.append(tf[k] - ti[k])
    if (values2['-IN-'] == True):#Calculate the terminal print mean
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
    df2 = df.rename(columns = {df.columns[1]: "Corrente"}, inplace= False)#rename the column "Corrente"
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
    plt.savefig(f'Relatórios\\{file_out}.jpg', dpi = 600)

    df4["Corrente"] = df4["Corrente"].multiply(1/1000)#variables will be presented as Ampere unity
    media = (round(df4["Corrente"].mean(), 5))
    minimo = (round(df4["Corrente"].min(), 5))
    maximo = (round(df4["Corrente"].max(), 5))

    # saveAsPDF3(ti,tf,dt,mean2,dt_mean,mean_t,imp1,imp2,mean_imp1,mean_imp2,file_out )       
    text = {'Corrente média': media, 'Corrente minima': minimo, 'Corrente máxima': maximo, 
            'Duração transação 1':dt[0], 'Duração transação 2':dt[1], 'Duração transação 3':dt[2], 'Duração transação 4':dt[3], 'Duração transação 5':dt[4],
            'Corrente media transação 1': mean2[0], 'Corrente media transação 2': mean2[1],'Corrente media transação 3': mean2[2],
            'Corrente media transação 4': mean2[3],'Corrente media transação 5': mean2[4], 'Média das correntes de transação': mean_t, 
            'Corrente 1ª via #1': imp1[0], 'Corrente 1ª via #2': imp1[1], 'Corrente 1ª via #3': imp1[2], 'Corrente 1ª via #4': imp1[3],
            'Corrente 1ª via #5': imp1[4], 'Média da corrente de 1ª via': mean_imp1, 'Corrente 2ª via 1': imp2[0], 'Corrente 2ª via #2': imp2[1],  
            'Corrente 2ª via #3': imp2[2],'Corrente 2ª via #4': imp2[3],  'Corrente 2ª via #5': imp2[4], 'Média da corrente de 2ª via': mean_imp2
            }
    saveAstxt3(file_out, text)
    return ti,tf,dt,mean2,dt_mean,mean_t,imp1,imp2,mean_imp1,mean_imp2,file_out    