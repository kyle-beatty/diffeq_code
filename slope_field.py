import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def derivative_magnitude(dt, dy):
    return np.sqrt(dt * dt + dy * dy)

def show_slope_field(dy, t_lower, t_upper, y_lower, y_upper, t_points, y_points):
    # make data
    t_range = np.linspace(t_lower, t_upper, t_points)
    y_range = np.linspace(y_lower, y_upper, y_points)
    T, Y = np.meshgrid(t_range, y_range)

    # find slope at each point
    U = np.ones((len(t_range), len(y_range)))
    V = dy(T, Y)
    #rescale U and V by the magnitudes for display
    MAG = derivative_magnitude(U, V)
    U = U / MAG
    V = V / MAG

    # plot
    fig, ax = plt.subplots()

    ax.quiver(T, Y, U, V, angles='xy',
              pivot='mid', width=.005,
              headwidth=0, headlength=0, headaxislength=0)

    ax.set(xlim=(t_lower, t_upper), ylim=(y_lower, y_upper))

    plt.show()


if __name__ == '__main__':
    def dy(t, y):
        return y + t

    t_lower = -1.5
    t_upper = 3.5

    y_lower = -2
    y_upper = 3

    # Number of points sampled -- (y_points * t_points) coordinate pairs
    t_points = 8
    y_points = 8
    show_slope_field(dy, t_lower, t_upper, y_lower, y_upper, t_points, y_points)
