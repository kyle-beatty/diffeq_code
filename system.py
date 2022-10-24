import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def euler(t_0, t_1, x_0, y_0, dx, dy, dt=1):
    t_values = np.arange(t_0, t_1, dt)

    x_values = np.empty(len(t_values))
    y_values = np.empty(len(t_values))

    x_values[0] = x_0
    y_values[0] = y_0

    for (t, i) in zip(t_values, range(len(t_values)- 1)):
        delta_x = dx(x_values[i], y_values[i], t)
        delta_y = dy(x_values[i], y_values[i], t)

        x_values[i+1] = x_values[i] + delta_x * dt
        y_values[i+1] = y_values[i] + delta_y * dt



    return (t_values, x_values, y_values)
    

if __name__ == '__main__':
    def dx(x, y, t):
        return 2 * (1 - x / 3) * x - (x * y)

    def dy(x, y, t):
        return -16 * y + 4 * x * y


    t_0 = 0
    t_1 = 2
    dt = 0.02

    x_values = list()
    y_values = list()

    initial_x = [8, 10, 7]
    initial_y = [1, 1, 2]

    for (x_0, y_0) in zip(initial_x, initial_y):
        values = euler(t_0, t_1, x_0, y_0, dx, dy, dt)
        x_values.append(values[1])
        y_values.append(values[2])

    colors = ['r', 'b', 'g', 'y', 'm']

    for (x, y, c, x_0, y_0) in zip(x_values, y_values, colors, initial_x, initial_y):
        line_label = '(%.2f, %.2f)' % (x_0, y_0)
        plt.plot(x, y, c , label=line_label)

    plt.xlabel('Rabbits')
    plt.ylabel('Foxes', rotation=0)
    plt.legend()
    plt.show()
