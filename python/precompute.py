import json
import pandas as pd
import numpy as np


# todo: scrape ncaa teams from here http://dynasties.operationsports.com/team-colors.php?sport=ncaa
# todo: hook in colormath

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


def rgb_to_cmyk(rgb_string):
    # formula taken from http://www.rapidtables.com/convert/color/rgb-to-cmyk.htm
    red, green, blue = unpack_rgb(rgb_string)

    r = red / 255
    g = green / 255
    b = blue / 255
    if r == 0 and g == 0 and b == 0:
        c = m = y = k = 0
    else:
        k = 1 - max(r, g, b)
        c = (1 - r - k) / (1 - k) * 100
        m = (1 - g - k) / (1 - k) * 100
        y = (1 - b - k) / (1 - k) * 100

    cmyk_string = ' '.join([str(c), str(m), str(y), str(k)])
    return cmyk_string


def fill_color_styles():
    with open('../teams.json') as data_file:
        data = json.load(data_file)

    df = pd.DataFrame(data)

    df['hex'] = np.nan
    df['rgb'] = np.nan
    df['cmyk'] = np.nan

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
            cmyk_conversion = [rgb_to_cmyk(r) for r in df.rgb[i]]
            df.cmyk[i] = cmyk_conversion

    df = df.drop('colors', axis=1)

    df.to_csv('../team_color_frame.csv', index=False)


if __name__ == "__main__":
    fill_color_styles()
