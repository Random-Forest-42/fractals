import matplotlib.pyplot as plt
import numpy as np
import cmath

motivo = [complex(0,0), complex(0.5, 0.5), complex(1,0)]

def convert_to_plot(a):
    x = [z.real for z in a]
    y = [z.imag for z in a]
    plt.plot(x,y)
    plt.show()

convert_to_plot(motivo)
point_list = motivo
iteraciones = 2

z0 = complex(0,0)
z1 = complex(1,1)
z2 = complex(2,0)
cmath.polar(z2-z1)
z1*z1
2**-1
get_punto_intermedio(z0,z1,0.5)
get_punto_intermedio(z1,z2,0.5)
def get_punto_intermedio(p0, p1, escala):
    print(escala)
    return p0+p1*(p1-p0)*escala

for i in range(iteraciones):
    next_point_list = []
    for j, p in enumerate(motivo[:-1]):
        # el base
        next_point_list.append(p)
        # punto intermedio
        next_point_list.append(get_punto_intermedio(p,point_list[j+1], 2**(-i)))
        # el siguiente
        next_point_list.append(point_list[j+1])
    convert_to_plot(next_point_list)
    point_list = next_point_list
