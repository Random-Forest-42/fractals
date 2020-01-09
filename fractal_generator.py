import matplotlib.pyplot as plt
import numpy as np
import copy

### PARAMETROS GENERALES
iteraciones = 5
flag_espejo_x = False
flag_espejo_y = False

### MOTIVOS
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
motivo = [complex(0,0), complex(0, 0.25), complex(0.5, 0.25), complex(0.5, -0.25), complex(1,-0.25), complex(1,0)]
# motivo = [complex(0,0), complex(0, 0.2), complex(0.5, 0.2), complex(0.5, -0.2), complex(1,-0.2), complex(1,0)]
# motivo = [complex(0, 0.25), complex(0.5, 0.25), complex(0.5, -0.25), complex(1,-0.25)]
# 2 PICOS
motivo = [complex(0,0), complex(0.1,0), complex(0.1,0.1), complex(0.2,0.1), complex(0.2,0), complex(0.6,0), complex(0.6,0.2), complex(0.8,0.2), complex(0.8,0), complex(1,0)]


# MOVIMIENTOS
r = np.sqrt(0.125)
mov = [0.5, 0.5j, 0.2, -0.2j]
mov = [0.5j, 0.5+0.2j, 0.5-0.2j]
mov = [0.5j, r+r*1j, r-r*1j, -0.5j]

def convert_movimientos(l, end_1=True, start_0=True):
    '''dada una lista con movimientos, los convierte a motivo
    asumimos que siempre empieza en 0,0 y termina en 1,0
    ex: [0.5, 0.5j, 0.2, -0.2j]
    --> [0j, (0.5+0j), (0.5+0.5j), (0.5+0.7j), (0.7+0.7j), (0.7+0.49999999999999994j), (1+0j)]
    '''
    last_point = 0
    l_out = [last_point]
    for m in l:
        last_point = last_point + m
        l_out.append(last_point)
    if end_1:
        l_out.append(1)
    return l_out

motivo = convert_movimientos(mov)




def convert_to_plot(a, flag_espejo_x=False, flag_espejo_y=False):
    x = [z.real for z in a]
    y = [z.imag for z in a]
    if flag_espejo_x:
        # para que pinte la version especular
        x2 = [z.real for z in a]
        x2.reverse()
        y2 = [-z.imag for z in a]
        y2.reverse()
        x += x2
        y += y2
    if flag_espejo_y:
        # para que pinte la version especular
        x3 = [-z.real for z in a]
        x.reverse()
        y3 = [z.imag for z in a]
        y.reverse()
        x += x3
        y += y3
    plt.plot(x,y)
    plt.axis('equal')
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
    convert_to_plot(next_point_list, flag_espejo_x, flag_espejo_y)
    point_list = next_point_list
