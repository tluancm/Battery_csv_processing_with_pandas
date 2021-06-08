import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import sys
import os

arquivo = input("Digite o nome do arquivo de entrada: ")
resultado = input("Digite o nome do arquivo de saída: ")
df = pd.read_csv(arquivo,skiprows=(3))
df2 = df.rename(columns = {'Active Instrument A Channel 1 Current Avg': "Corrente"}, inplace= False)
df3 = df2.set_index('Time')

df3["Corrente"] = df3["Corrente"].multiply(1000)
current01 = pd.DataFrame(df3, columns = ["Corrente"])
print("-"*50)
print(f"{resultado}.png foi salvo em Resultados\imagens\n{resultado}.pdf foi salvo em Resulados\pdf\n{resultado}.txt foi salvo em Resultados\txt")
print("-"*25+"FIM"+"-"*25)
current01.plot(xlabel= 'tempo[s]', ylabel = 'Corrente[mA]', grid = True, legend = False)
plt.savefig(f'Resultados\imagens\{resultado}.png', dpi=600)
plt.show()
df3["Corrente"] = df3["Corrente"].multiply(1/1000)
current01 = pd.DataFrame(df3, columns = ["Corrente"] )
media = (round(current01["Corrente"].mean(), 5))
minimo = (round(current01["Corrente"].min(), 5))
maximo = (round(current01["Corrente"].max(), 5))


def saveAsPDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(w = 0, h = 10, border = 1, txt = 'Corrente média: ' + str(media) + ' A\n'+'Corrente mínima: ' + str(minimo)+' A\n'+'Corrente máxima: ' + str(maximo)+' A')
    pdf.image(f'Resultados\imagens\{resultado}.png',x = 0, y = 50, w =200, h = 150)
    pdf.output(f'Resultados\pdf\{resultado}.pdf','F')

saveAsPDF()
os.chdir(r'C:\Users\vntlab\Documents\Keysight\BenchVue\Digital Multimeter\Exports\Resultados\txt')
sys.stdout = open(f"{resultado}.txt", 'wt')
print('Corrente média: ' + str(media) + ' A\n'+'Corrente minima: ' + str(minimo)+' A\n'+'Corrente maxima: ' + str(maximo)+' A')
sys.stdout.close()
