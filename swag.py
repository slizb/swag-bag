
import json
import pandas as pd

with open('teams.json') as data_file:
    data = json.load(data_file)

df = pd.DataFrame(data)


class TeamColors:

    def get_colors(self, team, n, style):
        frame = df[df.name == team].reset_index()
        colors = frame.colors[0][style]
        top_n_colors = colors[:n]
        if style == 'rgb':
            top_n_colors = [self.unpack_rgb(x) for x in top_n_colors]
        return top_n_colors

    @staticmethod
    def unpack_rgb(rgb_string):
        return rgb_string.split()

    @staticmethod
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    @staticmethod
    def rgb_to_hex(red, green, blue):
        return '#%02x%02x%02x' % (red, green, blue)


class TeamLogos:
    pass


print(TeamColors().get_colors("Chicago Bulls", 2, 'rgb'))
