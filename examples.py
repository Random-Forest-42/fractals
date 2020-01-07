import matplotlib.pyplot as plt
import numpy as np

# edited locally
x=[0,0.5,1]
y=[0,0.5,0]
# plt.plot(x,y)
# plt.show()

x2=[0,0.25,0.75,1]
y2=[0,0.5,0.5,0]
# plt.plot(x2,y2)
# plt.show()
def get_motivo(x,y):
    motivo = []
    for i in range(len(x)-1):
        motivo.append((x[i+1]-x[i], y[i+1]-y[i]))
    return motivo

motivo = get_motivo(x,y)
print(motivo)
def get_nuevo_punto(p0, p1, step, escala):
    '''donde
        p0 = (x0,y0), p1=(x1,y1)
        step es el motivo
        escala = 2^(-nº paso)
    '''
    # TODO: falta "girar", aplicar algo de p1?? cos(angulo)
    x_f = p0[0] + motivo[step][0] * escala * (np.sqrt(2) / 2)
    y_f = p0[1] + motivo[step][1] * escala * (np.sqrt(2) / 2)
    return (x_f, y_f)

print(get_nuevo_punto((x[0],y[0]),(x[1],y[1]),0,0.5))

iteraciones=3
for i in range(iteraciones-1):
    for j in x:
        # nuevo_punto(x_0,y_0,x_1,y_1)
        pass