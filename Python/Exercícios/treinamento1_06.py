import math

linha1 = str(input()).split()
linha2 = str(input()).split()

x1 = linha1[0]
x2 = linha2[0]
y1 = linha1[1]
y2 = linha2[1]

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

dist = ((x2-x1)**2 + (y2-y1)**2)**0.5

print('{:.4f}'.format(dist))
