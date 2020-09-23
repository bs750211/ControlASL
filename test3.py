h = [0, 1, 2, 3, 4, 5, 6, 7]
h1 = [0, 1, 2, 3, 4, 5, 6, 7]
m = [0, 1]

h[0] = 0
h[1] = 3
h[2] = 6
h[3] = 9
h[4] = 12
h[5] = 15
h[6] = 18
h[7] = 21

m[0] = 50

for i in range(8):
    if h[i] == 0:
        h1[i] = "23"
        h[i] = "00"
    elif h[i] > 0 and h[i] <= 9:
        h1[i] = h[i] - 1
        h1[i] = str(h1[i])
        h1[i] = h1[i].rjust(2, '0')
        h[i] = str(h[i])
        h[i] = h[i].rjust(2, '0')
    else:
        h1[i] = h[i] - 1
        h1[i] = str(h1[i])
        h[i] = str(h[i])
    print(h1[i])

if h1[0] == 22 or h1[1] == 22 or h1[2] == 22 or h1[3] == 22 or h1[4] == 22 or h1[5] == 22 or h1[6] == 22 or h1[7] == 22 and m[0] == 50:
    print("in condition")
else:
    print("out condition")
