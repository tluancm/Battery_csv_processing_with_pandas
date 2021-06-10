import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import sys
import os
import time

def saveAsPDF():#gera pdf com resultados e imagem
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 20)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    pdf.set_xy(5, 35)
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell( w = 0, h = 5, border = 0, txt = 'Tensão média: ' + str(media) + ' V\n'+'Tensão mínima: ' + str(minimo)+' V\n'+'Tensão máxima: ' + str(maximo)+' V\n'+'Tempo de carregamento: '+t_carga)
    pdf.image(f'Resultados\imagens\{file_out}.jpg',x = 0, y = 70, w =200, h = 150)
    pdf.output(f'Resultados\pdf\{file_out}.pdf','F')


def saveAstxt():#gera txt com resultados
    os.chdir(r'C:\Users\vntlab\Documents\Keysight\BenchVue\Digital Multimeter\Exports\Resultados\txt')
    sys.stdout = open(f"{file_out}.txt", 'wt')
    print('Tensão média: ' + str(media) + ' V\n'+'Tensão minima: ' + str(minimo)+' V\n'+'Tensão maxima: ' + str(maximo)+' V\n'+'Tempo de carregamento: '+t_carga)
    sys.stdout.close()


file_in = input("Digite o nome do arquivo de entrada: ")
file_out = input("Digite o nome do arquivo de saída: ")

df = pd.read_csv(file_in,skiprows=(3))#converte o arquivo csv em dataframe
df2 = df.rename(columns = {'File1 Instrument A Channel 1 Voltage Avg': "Tensão"}, inplace= False)#renomeia coluna de df e salva em df2
df3 = df2.set_index('Time')#troca a indexacao para a coluna Time e salva em df3
df4 = pd.DataFrame(df3, columns = ["Tensão"])#a partir do df3 cria um df4 com apenas colunas nomeadas Tensãos

print("-"*50)
print(f"{file_out}.png foi salvo em Resultados\imagens\n{file_out}.pdf foi salvo em Resulados\pdf\n{file_out}.txt foi salvo em Resultados"+'\\txt')
print("-"*25+"FIM"+"-"*25)

df4['Bateria[%]'] = (df4["Tensão"]-df4["Tensão"].min())*100/(df4["Tensão"].max()-df4["Tensão"].min())
df5 = pd.DataFrame(df4, columns = ['Bateria[%]'])
df5.plot(xlabel= 'tempo[s]', ylabel = 'Bateria[%]', grid = True, legend = False, title = f'{file_out}', figsize = (19.20,10.80))
plt.savefig(f'Resultados\imagens\{file_out}.jpg', dpi = 600)


media = (round(df4["Tensão"].mean(), 5)) 
minimo = (round(df4["Tensão"].min(), 5))
maximo = (round(df4["Tensão"].max(), 5))
max_index = df4.index[df4["Tensão"] == df4["Tensão"].max()]
max_index_list = max_index.tolist()
t_carga = time.strftime('%H:%M:%S', time.gmtime(max_index_list[0]))
saveAsPDF()
saveAstxt()
