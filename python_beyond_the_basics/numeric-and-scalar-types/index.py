def sign(x):
    # if x < 0:
    #     return -1
    # elif x > 0:
    #     return 1
    # return 0
    return (x > 0) - (x < 0)


def orientation(p, q, r):
    d = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return sign(d)


a = (0, 0)
b = (4, 0)
c = (4, 3)

a = orientation(a, b, c)

if __name__ == "__main__":
    print(a)
