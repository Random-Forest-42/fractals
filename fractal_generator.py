import matplotlib.pyplot as plt
import numpy as np

iteraciones = 4

motivo = [complex(0,0), complex(0.5, 0.5), complex(1,0)]
motivo = [complex(0,0), complex(0.25, 0), complex(0.25, 0.25), complex(0.75, 0.25), complex(0.75, 0), complex(1,0)]


def convert_to_plot(a):
    x = [z.real for z in a]
    y = [z.imag for z in a]
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
    convert_to_plot(next_point_list)
    point_list = next_point_list
