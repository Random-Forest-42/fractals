import matplotlib.pyplot as plt
import numpy as np
import copy

iteraciones = 6

# motivo = [complex(0,0), complex(0.5, 0.5), complex(1,0)]
# motivo = [complex(0,0), complex(0.5, -0.5), complex(1,0)]
motivo = [complex(0,0), complex(0.25, 0), complex(0.25, 0.25), complex(0.75, 0.25), complex(0.75, 0), complex(1,0)]
# motivo = [complex(0,0), complex(0.25, 0), complex(0.25, 0.25), complex(0.5,0.5), complex(0.75, 0.25), complex(0.75, 0), complex(1,0)]
# motivo = [complex(0,0), complex(0.25, 0), complex(0.25, 0.25), complex(0.75, 0.25), complex(0.75, 0), complex(1,0)]
motivo = [complex(0,0), complex(0.5, 0.5), complex(1,0), complex(0.5,-0.5), complex(0,0)]
# PICO
motivo = [complex(0,0), complex(0.25, 0), complex(0.5, 0.4), complex(0.75, 0), complex(1,0)]
motivo = [complex(0,0), complex(0.25, 0), complex(0.5, 0.4), complex(0.75, 0), complex(1,0), complex(0.5,-0.4), complex(0,0)]
motivo = [complex(0,0), complex(0.4, 0), complex(0.5, 0.45), complex(0.6, 0), complex(1,0)]
# #HAAR
# motivo = [complex(0,0), complex(0, 0.25), complex(0.5, 0.25), complex(0.5, -0.25), complex(1,-0.25), complex(1,0)]
# motivo = [complex(0, 0.25), complex(0.5, 0.25), complex(0.5, -0.25), complex(1,-0.25)]

flag_inverse = True

def convert_to_plot(a, flag_inverse=False):
    x = [z.real for z in a]
    y = [z.imag for z in a]
    if flag_inverse:
        # para que pinte la version especular
        x2 = [z.real for z in a]
        x2.reverse()
        y2 = [-z.imag for z in a]
        y2.reverse()
        x += x2
        y += y2
    plt.plot(x,y)
    plt.show()

convert_to_plot(motivo)
point_list = motivo

def get_puntos_intermedios(p1, p2):
    # la rotacion es el angulo por i
    rotacion = np.exp(complex(0,1)*np.angle(p2-p1))
    # la escala es la longitud del vector p1_p2
    escala = np.abs(p2-p1)
    puntos = [p1+m*escala*rotacion for m in motivo[1:-1]]
    return puntos


for i in range(iteraciones):
    next_point_list = []
    for j, p in enumerate(point_list[:-1]):
        # el base
        next_point_list.append(p)
        # puntos intermedios
        next_point_list += get_puntos_intermedios(p,point_list[j+1])
        # el siguiente
        next_point_list.append(point_list[j+1])
    convert_to_plot(next_point_list, flag_inverse)
    point_list = next_point_list
