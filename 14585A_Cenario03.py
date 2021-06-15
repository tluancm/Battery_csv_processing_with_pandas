import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import sys
import os

def saveAsPDF():#gera pdf com resultados e imagem
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 20)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    pdf.set_xy(5, 35)
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell( w = 0, h = 5, border = 0, txt = 'Corrente média: ' + str(media) + ' A\n'+'Corrente mínima: ' + str(minimo)+' A\n'+'Corrente máxima: ' + str(maximo)+' A')
    pdf.image(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg',x = 0, y = 50, w =200, h = 150)
    pdf.output(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\pdf\\{file_out}.pdf','F')


def saveAstxt():#gera txt com resultados
    os.chdir(r'C:\Users\VNTTAMA\Desktop\Relatorios\txt')
    sys.stdout = open(f"{file_out}.txt", 'wt')
    print('Corrente média: ' + str(media) + ' A\n'+'Corrente minima: ' + str(minimo)+' A\n'+'Corrente maxima: ' + str(maximo)+' A')
    sys.stdout.close()


file_in = input("Digite o nome do arquivo de entrada: ")
file_out = input("Digite o nome do arquivo de saída: ")

model = (input('Este modelo tem impressao?[s][n] '))
for k in range(0,5):
    ti.append(int(input(f'ti_{k} = ')))
    tf.append(int(input(f'tf_{k} = ')))
    dt.append(tf[k] - ti[k])
    


df = pd.read_csv(file_in,skiprows=(3))#converte o arquivo csv em dataframe
df2 = df.rename(columns = {'Active Instrument A Channel 1 Current Avg': "Corrente"}, inplace= False)#renomeia coluna de df e salva em df2
df2['Time'] = int(round(df2['Time']))
df3 = df2.set_index('Time')#troca a indexacao para a coluna Time e salva em df3
df3["Corrente"] = df3["Corrente"].multiply(1000)#multiplica toda coluna corrente por 1000 para mostrar no grafico em mA
df4 = pd.DataFrame(df3, columns = ["Corrente"])#a partir do df3 cria um df4 com apenas colunas nomeadas correntes

print("-"*50)
print(f"{file_out}.png foi salvo em Relatorios\imagens\n{file_out}.pdf foi salvo em Relatorios\pdf\n{file_out}.txt foi salvo em Relatorios"+'\\txt')
print("-"*25+"FIM"+"-"*25)

df4.plot(xlabel= 'tempo[s]', ylabel = 'Corrente[mA]', grid = True, legend = False, title = f'{file_out}', figsize = (19.20,10.80))
plt.savefig(f'Resultados\imagens\{file_out}.jpg', dpi = 600)

df4["Corrente"] = df4["Corrente"].multiply(1/1000)#divide a corrente por 1000 para mostrar resultados  em A
media = (round(df4["Corrente"].mean(), 5))
minimo = (round(df4["Corrente"].min(), 5))
maximo = (round(df4["Corrente"].max(), 5))

saveAsPDF()
saveAstxt()
