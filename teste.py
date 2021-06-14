loop = int(input("tamanho do laço: "))
ti = [0]
tf = [0]
dt = [0]

# for k in range(1,loop):
#     ti[k][0] = int(input('ti_1 = '))
#     ti[k][1] = int(input('ti_1 = '))
#     ti[k][2] = int(input('ti_1 = '))  
# print(ti)

for k in range(-1,loop):
    inicio = int(input(f'ti_{k} = '))
    ti.append(inicio)
    final = int(input(f'tf_{k} = '))
    tf.append(final)
    print(tf[k],ti[k])
    diftotal = tf[k] - ti[k]
    dt.append(diftotal)
print(ti,tf)