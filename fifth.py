import tkinter
import math

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.pack()

r = int(input('Размер:'))

n = 6

for k in range(n):
    k1 = (k + n / 2 - 1) % n

    p1 = (300 + r * math.cos(2 * 3.14 * k / n), 300 + r * math.sin(2 * 3.14 * k / n))
    p2 = (300 + r * math.cos(2 * 3.14 * k1 / n), 300 + r * math.sin(2 * 3.14 * k1 / n))
    canvas.create_line(p1, p2, fill='red')

master.mainloop()