import numpy
from PIL import Image

class WrongCoordinatesException(Exception):
    pass

def rectificate(im, coords):

    def move2board(a):
        a.tolist()
        a[0] = a[0] / a[2]
        a[1] = a[1] / a[2]
        a[2] = 1

        return a

    def make_equations(x1, x2, w1, w2):
        u = [-x1, -x2, -1, 0, 0, 0, w1 * x1, w1 * x2, w1]
        v = [0, 0, 0, -x1, -x2, -1, w2 * x1, w2 * x2, w2]
        return u, v

    w = [1] + [0 for i in range(8)]
    b = [0 for i in range(8)] + [1]

    def make_more_equations(points):
        return [make_equations(points[0][0], points[0][1], 0, 0)[0],
                make_equations(points[0][0], points[0][1], 0, 0)[1],
                make_equations(points[1][0], points[1][1], 0, 1)[0],
                make_equations(points[1][0], points[1][1], 0, 1)[1],
                make_equations(points[2][0], points[2][1], 1, 0)[0],
                make_equations(points[2][0], points[2][1], 1, 0)[1],
                make_equations(points[3][0], points[3][1], 1, 1)[0],
                make_equations(points[3][0], points[3][1], 1, 1)[1],
                w]
    try:
        L = make_more_equations(coords)
    except:
        raise WrongCoordinatesException("Wrong coordinates")

    h = numpy.linalg.solve(L, b)
    H = numpy.matrix([h[:3], h[3:6], h[6:]])

    new_coords = [[0 for j in range(im.width)] for i in range(im.height)]

    def h(coords):
        return H * numpy.matrix(coords).transpose()

    new_height = 0
    new_width = 0


    for j in range(im.height):
        for k in range(im.width):
            newxyz = move2board(h((j, k, 1)))
            new_coords[j][k] = (int(newxyz[0]*100), int(newxyz[1]*100))
            new_height = max(new_coords[j][k][0], new_height)
            new_width = max(new_coords[j][k][1], new_width)


    new_im = Image.new("RGB", (new_height, new_width))

    for j in range(im.height):
        for k in range(im.width):
            try:
                new_im.putpixel(new_coords[j][k], im.getpixel((j, k)))
            except:
                print(new_coords[j][k])

    new_im.save("results/new.png")
    return "/results/new.png"

