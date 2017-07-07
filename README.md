# Swag-Bag

[![Travis](https://img.shields.io/travis/slizb/swag-bag.svg)]()
[![Codecov](https://img.shields.io/codecov/c/github/slizb/swag-bag.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p align="center">
    <img src="https://github.com/slizb/swag-bag/blob/master/swag-bag.png" alt="swag-bag logo">
</p>

Swag-Bag is a convenient package for accessing the color palettes and logos of your favorite sports teams.  It enables you to create beautifully themed visualizations with a little *swag*.

## Installation

python and R packages are both currently under construction.  Stay tuned for install instructions!

## Usage

``` python
from swagbag import swag

colors = swag.TeamColors("Chicago Bulls", 2, "hex")
```

Then, you can hook into your favorite plotting package...

``` python
import seaborn as sns
import pandas as pd

df = pd.DataFrame([{'A':'Hodor', 'B':7},
                   {'A':'Bran', 'B':3}])

my_palette = sns.color_palette(colors)
sns.barplot(x='A', y='B', data=df, palette=my_palette, saturation=1)
```
<p align="center">
    <img src="https://github.com/slizb/swag-bag/blob/master/python/swagbag/examples/bulls.png" alt="bulls plot">
</p>
Logos are queryable too...

``` python
import matplotlib.pyplot as plt

logo = swag.TeamLogos("Chicago Bulls")
plt.imshow(logo)
```
<p align="center">
    <img src="https://github.com/slizb/swag-bag/blob/master/python/swagbag/examples/bulls_logo.png" width="500">
</p>

*_NOTE: this project is in beta, so documentation may lag from present usage_
