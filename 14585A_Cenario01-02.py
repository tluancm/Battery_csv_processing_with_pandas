import pandas as pd#provide way to process a csv file
import matplotlib.pyplot as plt#provide way to generate graph
from fpdf import FPDF# print output as pdf file
import sys#provide access to variable wich interact with the phyon interpreter
import os# provid way to interact with the OS

def saveAsPDF():#print output as pdf file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    epw = pdf.w -2*pdf.l_margin#widht of page minus 2x the margin, make possible to create cells with wide from margin to margin
    col_widht = epw/3#the margin to margin dimension will be ocupped by 3 cells
    pdf.set_font('Times', 'B', 12)
    pdf.cell(w= col_widht, h= 6, border =1,align = 'C', txt= 'Corrente média [A]' )
    pdf.cell(w= col_widht, h= 6, border= 1,align = 'C', txt= 'Corrente miníma [A]')
    pdf.cell(w= col_widht, h= 6, border= 1,align = 'C', ln=1,txt= 'Corrente máxima [A]' )

    pdf.cell(w= col_widht, h= 6,align = 'C', border= 1,txt= f'{media}' )
    pdf.cell(w= col_widht, h= 6,align = 'C', border= 1,txt= f'{minimo}')
    pdf.cell(w= col_widht, h= 6,align = 'C', border= 1, ln=1,txt= f'{maximo}' )
    
    pdf.image(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg',x = -10, y = 50, w =225, h = 150)
    pdf.output(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\pdf\\{file_out}.pdf','F')

def saveAstxt():#open a txt file and write the results
    os.chdir(r'C:\Users\VNTTAMA\Desktop\Relatorios\txt')#create directory
    sys.stdout = open(f"{file_out}.txt", 'wt')#open file to write
    print(text)
    sys.stdout.close()

file_in = input("Digite o nome do arquivo de entrada: ")
file_out = input("Digite o nome do arquivo de saída: ")

df = pd.read_csv(file_in,skiprows=(3))#convert csv to dataframe
df2 = df.rename(columns = {'Active Instrument A Channel 1 Current Avg': "Corrente"}, inplace= False)#rename the column "Corrente"
df3 = df2.set_index('Time')#create df3 with index seted as "Time" column from df2
df3["Corrente"] = df3["Corrente"].multiply(1000)
df4 = pd.DataFrame(df3, columns = ["Corrente"])#create a subdataframe df4 with column "Corrente" from df3

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

print("-"*60)
print(f"{file_out}.png foi salvo em Relatorios\imagens\n{file_out}.pdf foi salvo em Relatorios\pdf\n{file_out}.txt foi salvo em Relatorios"+'\\txt')
print("-"*30+"FIM"+"-"*30)

text = {'Corrente média': media, 'Corrente minima': minimo, 'Corrente máxima': maximo}
saveAstxt()



