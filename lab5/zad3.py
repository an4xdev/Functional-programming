from IPython.display import HTML
from abc import ABC, abstractmethod
import math
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Abstract_Shape(ABC):

    @abstractmethod
    def move(self, x, y):
        pass


class Point(Abstract_Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Ball(Point):

    def __init__(self, x, y, velocity):
        super().__init__(x, y)
        self.point, = ax.plot([], [], 'bo')
        self.angle = random.randint(0, 360)
        self.velocity = velocity
        self.velocity_x = self.velocity * math.cos(math.radians(self.angle))
        self.velocity_y = self.velocity * math.sin(math.radians(self.angle))

    def bounce(self, i):

        if self.x > 10:
            self.velocity_x = - self.velocity_x

        if self.y > 10:
            self.velocity_y = - self.velocity_y

        if self.x < 0:
            self.velocity_x = - self.velocity_x

        if self.y < 0:
            self.velocity_y = - self.velocity_y

        self.move(0, 0)

        return self.point,

    def move(self, x, y):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.point.set_data(self.x, self.y)


class Box(Abstract_Shape):

    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def move(self, x, y):
        self.x_max += x
        self.x_min += x
        self.y_max += y
        self.y_min += y


# Ustawienie wykresu
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ball = Ball(5, 5, .5)
# point = ax.plot([ball.x], [ball.y], 'bo')


def initial():
    ball.point.set_data([], [])
    return ball.point,


box = Box(0, 10, 0, 10)

# Stworzenie animacji
ani = FuncAnimation(fig, ball.bounce, init_func=initial,
                    frames=range(100), interval=100, blit=True)

plt.close()  # Zamknięcie wykresu - bez tej linii Colab wyświetli pusty wykres poniżej

# Wyświetlenie animacji w Google Colab
HTML(ani.to_html5_video())
