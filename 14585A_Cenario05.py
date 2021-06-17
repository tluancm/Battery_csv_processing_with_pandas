import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import sys
import os
import time

def saveAsPDF():#gera pdf com resultados e imagem
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 0, h=20, txt = f'Resultados {file_out}', align = 'C', ln=1 )
    pdf.set_font('Times', 'B', 12)
    epw = pdf.w -2*pdf.l_margin
    cold_widht = epw/4

    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border =1, txt= 'Tensão média [V]' )
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1, txt= 'Tensão miníma [V]')
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= 'Tensão máxima [V]' )
    pdf.cell(w= cold_widht+18, h= 6,align = 'C', border= 1, ln=1,txt= 'Tempo de carregamento [h:m:s]' )

    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= f'{media}' )
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= f'{minimo}')
    pdf.cell(w= cold_widht-6, h= 6, align = 'C',border= 1,txt= f'{maximo}' )
    pdf.cell(w= cold_widht+18, h= 6,align = 'C', border= 1, ln=1,txt= f'{t_descarga}' )

    pdf.cell(w = 0, h= 6,border= 0,align = 'C', ln= 1, txt='' )
    cold_widht2 = epw/3
    cold_widht3 = epw/4
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= ' ' )
    pdf.cell(w= 2*cold_widht3, h= 6,align = 'C', border= 1,txt= 'Tempo' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C',ln=1, border= 1,txt= ' ' )
    
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= 'Barras #' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= 's' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C', border= 1,txt= 'h:m:s' )
    pdf.cell(w= cold_widht3, h= 6,align = 'C',ln= 1, border= 1,txt= 'Bateria[%]')
    
    for k in range(0, barras):
        pdf.cell(w = cold_widht3, h= 6,align = 'C', border=1, txt= f'{k}' )
        pdf.cell(w = cold_widht3, h=6,align = 'C', border=1, txt= f'{t_conv_list[k]}')
        pdf.cell(w = cold_widht3, h= 6,align = 'C', border=1, txt= f'{t_header[k]}')
        pdf.cell(w = cold_widht3, h=6,align = 'C', border= 1, ln=1, txt= f'bbbbb')

    pdf.image(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg',x = 0, y = 100, w =200, h = 150)
    pdf.output(f"C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\pdf\\{file_out}.pdf",'F')


def saveAstxt():#gera txt com resultados
    os.chdir(r'C:\Users\VNTTAMA\Desktop\Relatorios\txt')
    sys.stdout = open(f"{file_out}.txt", 'wt')
    print('Tensão média: ' + str(media) + ' V\n'+'Tensão minima: ' + str(minimo)+' V\n'+'Tensão maxima: ' + str(maximo)+' V\n'+'Tempo de descarregamento: '+t_descarga)
    sys.stdout.close()


file_in = input("Digite o nome do arquivo de entrada: ")
file_out = input("Digite o nome do arquivo de saída: ")


df = pd.read_csv(file_in,skiprows=(3))#converte o arquivo csv em dataframe
df2 = df.rename(columns = {'File1 Instrument A Channel 1 Voltage Avg': "Tensão"}, inplace= False)#renomeia coluna de df e salva em df2
df3 = df2.set_index('Time')#troca a indexacao para a coluna Time e salva em df3
df4 = pd.DataFrame(df3, columns = ["Tensão"])#a partir do df3 cria um df4 com apenas colunas nomeadas Tensãos
print("-"*50)
print(f"{file_out}.png foi salvo em Relatorios\imagens\n{file_out}.pdf foi salvo em Relatorios\pdf\n{file_out}.txt foi salvo em Relatorios"+'\\txt')
print("-"*25+"FIM"+"-"*25)

df4['Bateria[%]'] = (df4["Tensão"]-df4["Tensão"].min())*100/(df4["Tensão"].max()-df4["Tensão"].min())
df5 = pd.DataFrame(df4, columns = ['Bateria[%]'])
df5.plot(xlabel= 'tempo[s]', ylabel = 'Bateria[%]', grid = True, legend = False, title = f'{file_out}', figsize = (19.20,10.80))
plt.savefig(f'C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg', dpi = 600)
plt.show()

opt = input('Truncar gráfico a partir de um tempo?[s] ou [n]: ')
if (opt == 'N' or 'n'): pass
    # print('\n Encerrado')
elif (opt == 'S'or 's'):
    zerar = int(input('Digite a partir de qual tempo em segundos os dados serão eliminados: '))
    df5 = df5.drop(range(zerar, int(df5.index[-1])+1))
    print(df5)
    df5.plot(xlabel= 'tempo[s]', ylabel = 'Bateria[%]', grid = True, legend = False, title = f'{file_out}', figsize = (19.20,10.80))
    plt.savefig(f"C:\\Users\\VNTTAMA\\Desktop\\Relatorios\\imagens\\{file_out}.jpg", dpi = 600)
    #plt.show()

media = (round(df4["Tensão"].mean(), 5)) 
minimo = (round(df4["Tensão"].min(), 5))
maximo = (round(df4["Tensão"].max(), 5))

min_index = df4.index[df4["Tensão"] == df4["Tensão"].min()]
min_index_list = min_index.tolist()
t_descarga = time.strftime('%H:%M:%S', time.gmtime(min_index_list[0]))

header = input('É possível observar a carga pelo header? [s] ou [n]: ')

t_header =[]
t_conv_list = []
if (header =='s' or header== 'S'):
    barras = int(input('Quantidade total de barras do header: '))
    barras2 = barras-1
    for i in range(0, barras):
        t_convert = (str(input(f'Tempo para atingir {barras2} barras: ')))   
        t_header.append(t_convert)
        h, m, s = t_convert.split(':')
        t_convert2 = int(h)*3600 + int(m)*60 + int(s)
        t_conv_list.append(t_convert2)
        barras2 = barras2-1    
    #       
else:
    comment = str(input('Comente: '))    


saveAsPDF()
#saveAstxt()