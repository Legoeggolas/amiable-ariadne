import matplotlib.pyplot as plt
from numpy import array


def show(maze: list):
    a = array(maze)
    plt.imshow(-a)
    plt.imshow(maze)
    plt.imsave("test.png", maze)
    plt.show()
