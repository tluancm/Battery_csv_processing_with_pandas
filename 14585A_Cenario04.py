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
    if (header == 's' or header =='S'):
        for k in range(0, barras):
            pdf.cell(w = cold_widht3, h= 6,align = 'C', border=1, txt= f'{k+1}' )
            pdf.cell(w = cold_widht3, h=6,align = 'C', border=1, txt= f'{t_conv_list[k]}')
            pdf.cell(w = cold_widht3, h= 6,align = 'C', border=1, txt= f'{t_header[k]}')
            pdf.cell(w = cold_widht3, h=6,align = 'C', border= 1, ln=1, txt= f'{battery[k]}')
    else: 
        pdf.multi_cell(w = 0, border= 1, txt= f'{comment}')        

    pdf.image(f'C:\\Users\\taylo\OneDrive\\Área de Trabalho\\Relatorios\\imagens\\{file_out}.jpg',x = -10, y = 100, w =225, h = 150)
    pdf.output(f"C:\\Users\\taylo\\OneDrive\\Área de Trabalho\\Relatorios\\pdf\\{file_out}.pdf",'F')

def saveAstxt():#open a txt file and write the results
    os.chdir(r'C:\Users\taylo\OneDrive\Área de Trabalho\Relatorios\txt')#create directory
    sys.stdout = open(f"{file_out}.txt", 'wt')#open file to write
    print(text)
    sys.stdout.close()

file_in = input("Digite o nome do arquivo de entrada: ")
file_out = input("Digite o nome do arquivo de saída: ")

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
plt.savefig(f'C:\\Users\\taylo\\OneDrive\\Área de Trabalho\\Relatorios\\imagens\{file_out}.jpg', dpi = 600)
plt.show()

opt = input('Truncar gráfico a partir de um tempo?[s] ou n[n]: ')
if (opt == 'N' or 'n'): pass
elif (opt == 'S'or 's'):#drop rows based on user input on time and generate updated graph
    zerar = int(input('Digite a partir de qual tempo em segundos os dados serão eliminados: '))
    df5 = df5.drop(range(zerar, int(df5.index[-1])+1))
    df5.plot( grid = True, legend = False, figsize = (19.20,10.80))
    plt.xlabel('tempo [s]', fontsize=22)
    plt.ylabel('Bateria [%]', fontsize=22)
    plt.suptitle(f'{file_out}'+" gráfico", fontsize= 26)
    plt.savefig(f'C:\\Users\\taylo\\OneDrive\\Área de Trabalho\\Relatorios\\imagens\{file_out}.jpg', dpi = 600)
    plt.show()

media = (round(df4["Tensão"].mean(), 5)) 
minimo = (round(df4["Tensão"].min(), 5))
maximo = (round(df4["Tensão"].max(), 5))
max_index = df4.index[df4["Tensão"] == df4["Tensão"].max()]#calculate the max voltage on column "Tensão"
max_index_list = max_index.tolist()#create a list with every max voltage index
t_carga = time.strftime('%H:%M:%S', time.gmtime(max_index_list[0]))#take the first time with the lowest voltage and convert to h:m:s format

header = input('É possível observar a carga pelo header? [s] ou [n]: ')
t_header =[]
t_conv_list = []
battery = []
if (header =='s' or header== 'S'):
    barras = int(input('Quantidade total de barras do header: '))  
    for k in range(0, barras):
        t_convert = (str(input(f'Tempo para atingir {k+1} barras: ')))#input time to reach a certain header on a hh:mm:ss format 
        t_header.append(t_convert)#convert input to seconds
        h, m, s = t_convert.split(':')
        t_convert2 = int(h)*3600 + int(m)*60 + int(s)
        t_conv_list.append(t_convert2)#will be printed on pdf as seconds and hh:mm:ss 
        battery.append(df5.iloc[t_convert2, 0])#loaclize battery % in dataframe and save in a list    
    battery = [int(round(n, 0)) for n in battery ]#printed as integer
else:
    comment = str(input('Comente: '))#if not is possible to read the header battery % the user input a comment    

saveAsPDF()

print("-"*50)
print(f"{file_out}.png foi salvo em Relatorios\imagens\n{file_out}.pdf foi salvo em Relatorios\pdf\n{file_out}.txt foi salvo em Relatorios"+'\\txt')
print("-"*25+"FIM"+"-"*25)

text = {'Tensao média': media, 'Tensão miníma': minimo, 'Tensão máxima': maximo, 'Tempo de carregamento': t_carga}

saveAstxt()
