h = [0, 1, 2, 3, 4, 5, 6, 7]
h[0] = 0
h[1] = 3
h[2] = 6
h[3] = 9
h[4] = 12
h[5] = 15
h[6] = 18
h[7] = 21

for i in range(8):
    if h[i] == 0:
        h[i] = "23"
    elif h[i] > 0:
        h[i] -= 1
    print(h[i])



