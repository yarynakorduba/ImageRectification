import numpy

from PIL import Image

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

    L = make_more_equations(coords)
    h = numpy.linalg.solve(L, b)
    H = numpy.matrix([h[:3], h[3:6], h[6:]])

    def h(coords):
        return H * numpy.matrix(coords).transpose()

    new_im = Image.new("RGB", (im.height, im.width))
    for k in range(im.height):
        for j in range(im.width):
            try:
                new_im.putpixel(
                    (int(move2board(h((j, k, 1)))[:2][0] * 300), int(move2board(h((j, k, 1)))[:2][1] * 300)),
                    im.getpixel((j, k)))
            except IndexError:
                print("er")
    new_im.show()
    new_im.save("results/new.png")
    return "/results/new.png"
   # return render_template('index.html', new_im=new_im)


