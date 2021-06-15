
ti = []
tf = []
dt = []

# for k in range(1,loop):
#     ti[k][0] = int(input('ti_1 = '))
#     ti[k][1] = int(input('ti_1 = '))
#     ti[k][2] = int(input('ti_1 = '))  
# print(ti)

for k in range(0,5):
    ti.append(int(input(f'ti_{k} = ')))
    tf.append(int(input(f'tf_{k} = ')))
    print(tf[k],ti[k])
    dt.append(tf[k] - ti[k])
    
print(ti,tf, dt)