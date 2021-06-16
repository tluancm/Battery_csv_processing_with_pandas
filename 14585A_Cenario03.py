import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import sys
import os
import statistics as sts
import time

def saveAsPDF():#gera pdf com resultados e imagem
    pdf = FPDF()
    pdf.add_page()
    epw = pdf.w -2*pdf.l_margin
    col_widht = epw/5
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    #pdf.set_xy(5, 35)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(w = col_widht, h =6, border = 1, align = 'C',  txt = "Transação#" )
    pdf.cell(w = col_widht, h =6, border =1, align = 'C', txt = "Início [s]")
    pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = "Fim [s]")
    pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = "Duração [s]")
    pdf.cell(w = 45, h =6, border =1,ln =1, align = 'C', txt = "Corrente média [mA]")
    for k in range(0,5):
        pdf.cell(w = col_widht, h =6, border = 1, align = 'C',  txt = f"{k}" )
        pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = f"{ti[k]}")
        pdf.cell(w = col_widht, h =6, border =1, align = 'C',  txt = f"{tf[k]}")
        pdf.cell(w = col_widht, h =6, border =1, align = 'C', txt = f"{dt[k]}")
        pdf.cell(w = 45, h =6, border =1,ln =1, align = 'C', txt = f"{mean2[k]}")
    
    pdf.image(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg',x = 0, y = 140, w =200, h = 150)
    pdf.output(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\pdf\\{file_out}.pdf','F')


def saveAstxt():#gera txt com resultados
    os.chdir(r'C:\Users\VNTTAMA\Desktop\Relatorios\txt')
    sys.stdout = open(f"{file_out}.txt", 'wt')
    print('Corrente média: ' + str(media) + ' A\n'+'Corrente minima: ' + str(minimo)+' A\n'+'Corrente maxima: ' + str(maximo)+' A')
    for k in range(0, 5):
        print(f'ínicio: {ti[k]}       fim: {tf[k]}            duração: {dt[k]}       corrente media{k}: {mean2[k]}   mA ')
    print(f'corrente media nas transações: {mean_t}   mA')    
    sys.stdout.close()



file_in = input("Digite o nome do arquivo de entrada: ")
file_out = input("Digite o nome do arquivo de saída: ")

#model = (input('Este modelo tem impressao?[s][n] '))
ti =[]
tf = []
dt = []
for k in range(0,5):
    ti.append(int(input(f'ti_{k} = ')))
    tf.append(int(input(f'tf_{k} = ')))
    dt.append(tf[k] - ti[k])

ti_m = [c*2 for c in ti]    
tf_m = [c*2 for c in tf]


df = pd.read_csv(file_in,skiprows=(3))#converte o arquivo csv em dataframe
df['Time'] = df['Time'].round(decimals = 1)
df2 = df.rename(columns = {'Active Instrument A Channel 3 Current Avg': "Corrente"}, inplace= False)#renomeia coluna de df e salva em df2
df3 = df2.set_index('Time')#troca a indexacao para a coluna Time e salva em df3
df3["Corrente"] = df3["Corrente"].multiply(1000)#multiplica toda coluna corrente por 1000 para mostrar no grafico em mA
df4 = pd.DataFrame(df3, columns = ["Corrente"])#a partir do df3 cria um df4 com apenas colunas nomeadas correntes

mean = []

for k in range(0, 5):
    mean.append(df4.iloc[ti_m[k]:tf_m[k]+1,0].mean())
mean2 = [round(n, 3) for n in mean ]  
mean_t = round(sts.mean(mean), 3)
print("-"*50)
print(f"{file_out}.png foi salvo em Relatorios\imagens\n{file_out}.pdf foi salvo em Relatorios\pdf\n{file_out}.txt foi salvo em Relatorios"+'\\txt')
print("-"*25+"FIM"+"-"*25)

df4.plot(xlabel= 'tempo[s]', ylabel = 'Corrente[mA]', grid = True, legend = False, title = f'{file_out}', figsize = (19.20,10.80))
plt.savefig(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg', dpi = 600)
#time.sleep(4)


df4["Corrente"] = df4["Corrente"].multiply(1/1000)#divide a corrente por 1000 para mostrar resultados  em A
media = (round(df4["Corrente"].mean(), 5))
minimo = (round(df4["Corrente"].min(), 5))
maximo = (round(df4["Corrente"].max(), 5))

saveAsPDF()
#saveAstxt()
