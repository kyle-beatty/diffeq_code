import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def euler(t_0, y_0, dy, lower, upper, dt=1):
    left_t = np.arange(t_0, lower, -1 * dt)
    right_t = np.arange(t_0, upper, dt)

    left_y = np.empty(len(left_t))
    right_y = np.empty(len(right_t))

    if len(left_y) > 0: left_y[0] = y_0
    if len(right_y) > 0: right_y[0] = y_0

    for (t, i) in zip(right_t, range(len(right_t)- 1)):
        slope = dy(t, right_y[i])
        val = right_y[i] + slope * dt

        right_y[i+1] = right_y[i] + slope * dt

    for (t, i) in zip(left_t, range(len(left_t)- 1)):
        slope = dy(t, left_y[i])
        left_y[i+1] = left_y[i] + slope * -1 * dt

    t_values = np.append(left_t[::-1], right_t[1:])
    y_values = np.append(left_y[::-1], right_y[1:])

    return (t_values, y_values)
    

if __name__ == '__main__':
    def f(t, y):
        return (y-1) * (y+1) / 2

    lower = -5
    upper = 5
    dt = 0.2

    t_values = list()
    y_values = list()

    initial_t = [0, 0, 0]
    initial_y = [0, 1, -0.5]

    for (t, y) in zip(initial_t, initial_y):
        points = euler(t, y, f, lower, upper, dt)
        t_values.append(points[0])
        y_values.append(points[1])

    colors = ['r', 'b', 'g', 'y', 'm']

    for (t, y, c, t_0, y_0) in zip(t_values, y_values, colors, initial_t, initial_y):
        line_label = '(%.2f, %.2f)' % (t_0, y_0)
        plt.plot(t, y, c , label=line_label)

    plt.legend()
    plt.show()
