import unittest
import os
import sys

my_wd = os.getcwd()
print(my_wd)

sys.path.append(my_wd + '/python')

from swagbag import swag
from PIL.PngImagePlugin import PngImageFile


class TestTeamLogos(unittest.TestCase):
    def test_fake_team_doesnt_work(self):
        img = swag.TeamLogos().get_logo('Decatur Fakers')
        self.assertNotIsInstance(img, PngImageFile)

    def test_real_team_works(self):
        img = swag.TeamLogos().get_logo('Chicago Bulls')
        self.assertIsInstance(img, PngImageFile)


class TestUtil(unittest.TestCase):
    def test_read_svg_from_web(self):
        homer_svg = 'http://thenewcode.com/assets/images/thumbnails/homer-simpson.svg'
        img = swag.Util().read_svg_from_web(homer_svg, 1)
        self.assertIsInstance(img, PngImageFile)

if __name__ == '__main__':
    unittest.main()
