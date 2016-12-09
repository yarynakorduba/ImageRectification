import unittest
from rectification import *


class TestRectification(unittest.TestCase):

    def testOutputImageExample1(self):
        originalImg = Image.open("examples/originalExample1.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg1.png")

        rectificated_img = Image.open("static/results/"
                                      +rectificate(originalImg, [(180, 20), (166,300), (296,84), (290, 240)]))
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testOutputImageExample2(self):
        originalImg = Image.open("examples/originalExample2.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg2.png")
        rectificated_img = Image.open("static/results/"+
                                      rectificate(originalImg, [(20, 20), (166, 300), (296, 84), (290, 240)]))
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testOutputImageExample3(self):
        originalImg = Image.open("examples/originalExample3.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg3.png")
        rectificated_img = Image.open("static/results/" +
                                      rectificate(originalImg, [(180, 20), (600, 300), (296, 84), (290, 240)]))
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testOutputImageExample4(self):
        originalImg = Image.open("examples/originalExample1.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg1.png")
        rectificated_img = Image.open("static/results/" +
                                      rectificate(originalImg, [(180, 20), (166, 300), (296, 84), (290, 240)]))
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testOutputImageExample5(self):
        originalImg = Image.open("examples/originalExample1.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg1.png")
        rectificated_img = Image.open("static/results/" +
                                      rectificate(originalImg, [(180, 20), (200, 300), (296, 84), (290, 240)]))
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testOutputImageExample6(self):
        originalImg = Image.open("examples/originalExample2.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg2.png")
        rectificated_img = Image.open("static/results/" +
                                      rectificate(originalImg, [(180, 20), (166, 300), (15, 84), (290, 240)]))
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testRaiseError(self):
        originalImg = Image.open("examples/originalExample1.png")
        self.assertRaises(WrongCoordinatesException, rectificate(originalImg, [(0, 0), (0,0), (0,0), (0, 0)]))

    def testRaiseError1(self):
        originalImg = Image.open("examples/originalExample1.png")
        self.assertRaises(WrongCoordinatesException, rectificate(originalImg, [(-100, 0), (0,0), (0,0), (0, 0)]))

    def testRaiseError2(self):
        originalImg = Image.open("examples/originalExample1.png")
        self.assertRaises(WrongCoordinatesException, rectificate(originalImg, [(100000, 0), (0,0), (0,0), (0, 0)]))

    def testRaiseError3(self):
        originalImg = Image.open("examples/originalExample1.png")
        self.assertRaises(WrongCoordinatesException, rectificate(originalImg, [(12, 0), (0,12), (12,12), (0, 0), (5,5)]))



if __name__ == '__main__':
    unittest.main()