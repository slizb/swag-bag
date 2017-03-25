import json
import pandas as pd
import numpy as np

with open('../teams.json') as data_file:
    data = json.load(data_file)

df = pd.DataFrame(data)

df['hex'] = np.nan
df['rgb'] = np.nan
df['cmyk'] = np.nan


def hex_to_rgb(value):
    lv = len(value)
    rgb_list = [int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]
    rgb_str = ' '.join(str(x) for x in rgb_list)
    return rgb_str


def rgb_to_hex(rgb_string):
    red, green, blue = unpack_rgb(rgb_string)
    return '%02x%02x%02x' % (red, green, blue)


def unpack_rgb(rgb_string):
    rgb_list = rgb_string.split()
    red = int(rgb_list[0])
    green = int(rgb_list[1])
    blue = int(rgb_list[2])
    return (red, green, blue)

def rgb_to_cmyk():

    # RGB to CMYK conversion formula
    # The R,G,B values are divided by 255 to change the range from 0..255 to 0..1:
    # R' = R/255
    # G' = G/255
    # B' = B/255
    # The black key (K) color is calculated from the red (R'), green (G') and blue (B') colors:
    # K = 1-max(R', G', B')
    # The cyan color (C) is calculated from the red (R') and black (K) colors:
    # C = (1-R'-K) / (1-K)
    # The magenta color (M) is calculated from the green (G') and black (K) colors:
    # M = (1-G'-K) / (1-K)
    # The yellow color (Y) is calculated from the blue (B') and black (K) colors:
    # Y = (1-B'-K) / (1-K)
    pass


for i, row in enumerate(df.colors):
    # hex
    try:
        df.hex[i] = row['hex']
    except KeyError:
        hex_conversion = [rgb_to_hex(r) for r in row['rgb']]
        df.hex[i] = hex_conversion
    # rgb
    try:
        df.rgb[i] = row['rgb']
    except KeyError:
        rgb_conversion = [hex_to_rgb(h) for h in row['hex']]
        df.rgb[i] = rgb_conversion
    # cmyk
    try:
        df.cmyk[i] = row['cmyk']
    except KeyError:
        pass


df = df.drop('colors', axis = 1)

df.to_csv('../team_color_frame.csv', index = False)
