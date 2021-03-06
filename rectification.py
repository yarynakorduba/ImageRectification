import numpy
from PIL import Image
import datetime
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
        h = numpy.linalg.solve(L, b)
        H = numpy.matrix([h[:3], h[3:6], h[6:]])
    except :
        raise WrongCoordinatesException("Wrong coordinates")

    new_coords = [[0 for j in range(im.size[1])] for i in range(im.size[0])]

    def h(coords):
        return H * numpy.matrix(coords).transpose()

    new_height = 0
    new_width = 0
    new_negative_width = 0
    new_negative_height = 0

    for j in range(im.size[0]):
        for k in range(im.size[1]):
            newxyz = move2board(h((j, k, 1)))
            new_coords[j][k] = (int(newxyz[0] * im.size[0]/2), int(newxyz[1]*im.size[1]/2))
            new_height = max(new_coords[j][k][1], new_height)
            new_width = max(new_coords[j][k][0], new_width)
            new_negative_width = min(new_coords[j][k][0], new_negative_width)
            new_negative_height = min(new_coords[j][k][1], new_negative_height)

    new_im = Image.new("RGB", ( abs(new_negative_width) + new_width, abs(new_negative_height) + new_height), color=(255,255,255))

    for j in range(im.size[0]-1):
        for k in range(im.size[1]-1):
            try:
                new_im.putpixel((new_coords[j][k][0] + abs(new_negative_width), abs(new_negative_height) + new_coords[j][k][1]), im.getpixel((j, k)))
                new_im.putpixel((new_coords[j][k][0] + abs(new_negative_width)+1, abs(new_negative_height) + new_coords[j][k][1]+1), im.getpixel((j, k)))
                
            except Exception as e:
                print(e)
               # print((new_coords[j][k][1]+ abs(new_negative_width),  abs(new_negative_height) + new_coords[j][k][0]))
                print(str(j)+"  "+str(k))
    print(new_im.size)
    new_address = "results/" + datetime.datetime.now().strftime("%m-%d-%Y_%H:%M:%S") + ".png"
    new_im.save("static/" + new_address)
    return new_address

if __name__ == '__main__':
    im = Image.open("board.png")
    print(im.size)
    rectificate(Image.open("k.jpg"), [[358,36],[329,597],[592,157],[580,483]])