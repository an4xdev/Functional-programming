# Z2.
from IPython.display import HTML
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math

# Inicjalizacja pozycji, kąta i prędkości
position_x = 5
position_y = 5
angle = random.randint(0, 360)
velocity = .3  # przesunięcie na klatkę

# Obliczenie komponentów prędkości w osiach x i y
velocity_x = velocity * math.cos(math.radians(angle))
velocity_y = velocity * math.sin(math.radians(angle))

# Ustawienie wykresu
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
point, = ax.plot([], [], 'bo')

# Inicjalizacja punktu na wykresie


def init():
    point.set_data([], [])
    return point,

# Funkcja animująca


def animate(i):
    global position_x, position_y, velocity_x, velocity_y

    if position_x > 10:
        velocity_x = - velocity_x

    if position_y > 10:
        velocity_y = - velocity_y

    if position_x < 0:
        velocity_x = - velocity_x

    if position_y < 0:
        velocity_y = - velocity_y
    position_x += velocity_x
    position_y += velocity_y

    point.set_data(position_x, position_y)
    return point,


# Stworzenie animacji
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=range(100), interval=100, blit=True)

plt.close()  # Zamknięcie wykresu - bez tej linii Colab wyświetli pusty wykres poniżej

# Wyświetlenie animacji w Google Colab
HTML(ani.to_html5_video())
