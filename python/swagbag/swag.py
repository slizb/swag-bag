
import pandas as pd
import cairosvg
import PIL
import os
import data

data_path = data.__path__

df = pd.read_pickle(data_path[0] + '/team_color_frame.pkl')


class TeamColors:

    def get_colors(self, team, n, style):
        frame = df[df.name == team].reset_index()
        colors = frame[style]
        top_n_colors = colors[0][:n]
        if style == 'rgb':
            top_n_colors = [self.unpack_rgb(x) for x in top_n_colors]
        return top_n_colors

    @staticmethod
    def unpack_rgb(rgb_string):
        rgb_list = rgb_string.split()
        red = int(rgb_list[0])
        green = int(rgb_list[1])
        blue = int(rgb_list[2])
        return (red, green, blue)


class TeamLogos:
    pass


class Util:

    def read_svg_from_web(self, url, size):
        cairosvg.svg2png(url=url,
                         write_to='temp_swag.png',
                         scale=size)
        img = PIL.Image.open('temp_swag.png')
        os.remove('temp_swag.png')
        return img
