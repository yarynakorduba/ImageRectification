import unittest
from rectification import *


class TestRectification(unittest.TestCase):

    def testOutputImageExample1(self):
        originalImg = Image.open("examples/originalExample1.png")
        prepared_rectificated_img = Image.open("examples/recticifatedImg1.png")
        rectificate(originalImg, [(180, 20), (166,300), (296,84), (290, 240)])
        rectificated_img = Image.open("static/new.png")
        self.assertEqual(list(prepared_rectificated_img.getdata()), list(rectificated_img.getdata()))
"""
    def testOutputImageExample2(self):
        originalImg = Image.open("originalExample2.png")
        prepared_rectificated_img = Image.open("recticifatedImg2.png")
        rectificate(originalImg, [])
        rectificated_img = Image.open("static/new.png")
        self.assertEqual(prepared_rectificated_img, rectificated_img)

    def testOutputImageExample3(self):
        originalImg = Image.open("originalExample3.png")
        prepared_rectificated_img = Image.open("recticifatedImg3.png")
        rectificate(originalImg, [])
        rectificated_img = Image.open("static/new.png")
        self.assertEqual(prepared_rectificated_img, rectificated_img)
"""


if __name__ == '__main__':
    unittest.main()