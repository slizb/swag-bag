
import pandas as pd


df = pd.read_pickle('../data/team_color_frame.pkl')


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

print(TeamColors().get_colors("Arsenal", 5, 'hex'))
