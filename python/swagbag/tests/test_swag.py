import unittest
import os
import sys

my_wd = os.getcwd()
print(my_wd)

sys.path.append(my_wd + '/python')

from swagbag import swag

class TestUtil(unittest.TestCase):
    def test_read_svg_from_web(self):
        homer_svg = 'http://thenewcode.com/assets/images/thumbnails/homer-simpson.svg'
        img = swag.Util().read_svg_from_web(homer_svg, 1)
        self.assertIsInstance(img, swag.PIL.PngImagePlugin.PngImageFile)

if __name__ == '__main__':
    unittest.main()
