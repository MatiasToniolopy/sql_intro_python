import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as sql


def fetch():
    conexion = sql.connect('heart.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT pulso FROM sensor')
    data = cursor.fetchall()
    #print(data)

    conexion.close()
    return data
    
def show(data):
    plt.figure()
    plt.suptitle('RITMO CARDIACO BASADO EN UN PARTIDO DE FUTBOL', color='black')
    plt.subplot()
    plt.plot(data, linestyle= '--', label= 'Pulso y tiempo')
    plt.xlabel('Tiempo')
    plt.ylabel('Pulso')
    plt.grid()
    plt.legend()
    plt.show()
    
def estadisticas():
    valor_med = np.mean(data)
    print('El valor medio es de: ', valor_med)
    valor_min = np.min(data)
    print('El valor minimo es de: ', valor_min)
    valor_max = np.max(data)
    print('El valor maximo es de: ', valor_max)
    valor_standar = np.std(data)
    print('El valor standar es de: ', valor_standar)
    
def regiones(data):
    
    v_med = np.mean(data)
    v_std = np.std(data)
    
    x1 = [x for x in range(len(data)) if data[x] <= (v_med-v_std)]
    y1 = [data[x] for x in range(len(data)) if data[x] <= (v_med-v_std)]
    
    x2 = [x for x in range(len(data)) if data[x] >= (v_med+v_std)]
    y2 = [data[x] for x in range(len(data)) if data[x] >= (v_med+v_std)]
    
    x3 = [x for x in range(len(data)) if (v_med-v_std) <= data[x] <= (v_med+v_std)]
    y3 = [data[x] for x in range(len(data)) if (v_med-v_std) <= data[x] <= (v_med+v_std)]
    
    plt.figure()
    plt.subplot(2,2,1)
    plt.scatter(x1, y1, color='r', label='Aburrido', marker='.')
    plt.legend()
    plt.colorbar()
    
    plt.subplot(2,2,2)
    plt.scatter(x2, y2, color='g', label='Enganchado', marker='.')
    plt.legend()
    plt.colorbar()
    
    plt.subplot(2,2,3)
    plt.scatter(x3, y3, color='b', label='Entusiasmado', marker='.')
    plt.legend()
    plt.colorbar()
    
    plt.show()
    
    
    

    
    
    
        
    
    
    
    




















if __name__ == '__main__':
    
    data = fetch()
    
    show(data)
    
    estadisticas()
    
    regiones(data)
    
