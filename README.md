# Swag-Bag

Swag-Bag is a convenient package for accessing the color palettes and logos of your favorite sports teams.

## Installation

python and R packages are both currently under construction.  Stay tuned for install instructions!

## Usage

    from swagbag import swag
    colors = swag.TeamColors("Chicago Bulls", 2, "hex")

Then, you can hook into your favorite plotting package...

    import seaborn as sns
    import pandas as pd

    df = pd.DataFrame([{'A':'Hodor', 'B':7},
                       {'A':'Bran', 'B':3}])
    
    my_palette = sns.color_palette(colors)
    sns.barplot(x='A', y='B', data=df, palette=my_palette, saturation=1)
    
![bulls plot](https://github.com/slizb/swag-bag/blob/master/python/examples/bulls.png "bulls plot")

*_NOTE: this project is in beta, so documentation may lag from present usage_
