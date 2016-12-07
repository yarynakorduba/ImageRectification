import unittest
from rectification import *


class TestRectification(unittest.TestCase):

    def testOutputImageExample1(self):
        originalImg = Image.open("examples/originalExample1.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg1.png")
        rectificate(originalImg, [(180, 20), (166,300), (296,84), (290, 240)])
        rectificated_img = Image.open("static/new.png")
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))

    def testOutputImageExample1(self):
        originalImg = Image.open("examples/originalExample1.png")
        self.assertRaises(WrongCoordinatesException, rectificate(originalImg, [(180, 20), (166,300), (296,84), (290, 240)]))

if __name__ == '__main__':
    unittest.main()