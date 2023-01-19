import numpy as np
import matplotlib.pyplot as plt

limit = 100
step = 0.01
increase_high = True
color = 'r'
line_style = '-.'

x_change = {-limit: 'inc'}

x = np.arange(-limit, limit, step)

a, b, c, d, e = -12, -18, 5, 10, -30

def f(x):
    func = a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
    return func

def switch_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color

def switch_line():
    global line_style
    if line_style == '-':
        line_style = '-.'
    else:
        line_style = '-'
    return line_style

x_min = -limit
f_min = f(-limit)

for x_cur in x:
    if f(x_cur) < f_min:
        f_min = np.round(f(x_cur), 2)
        x_min = np.round(x_cur, 2)

print(x_min, f_min)

for i  in range(len(x)-1):
    if (f(x[i]) > 0 and f(x[i+1]) < 0) or (f(x[i]) < 0 and f(x[i+1]) > 0):
        x_change[x[i]] = 'zero'
    if increase_high:
        if f(x[i]) > f(x[i+1]):
            increase_high = False
            x_change[x[i]] = 'inc'
    else:
        if f(x[i]) < f(x[i+1]):
            increase_high = True
            x_change[x[i]] = 'inc'

x_change[limit] = 'inc'
print(x_change)

x_keys = [x for x in x_change]
x_keys.sort()
print(x_keys)

for i in range(len(x_keys) - 1):
    x_cur = np.arange(x_keys[i], x_keys[i+1] + step, step)
    if x_change.get(x_keys[i]) == 'zero':
        switch_line()
    else:
        switch_color()
    plt.rcParams['lines.linestyle'] = line_style
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.grid(True)
    plt.plot(x_cur, f(x_cur), color)

ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()