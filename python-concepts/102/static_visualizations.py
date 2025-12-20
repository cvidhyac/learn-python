"""
Visualizations are a powerful way to get to know your data. Python has many libraries for this.
Bar chart - summarize the spread distribution when a die is rolled a million times
Calculating descriptive stats - Big data

Matplotlib = support into jupyter notebooks out-of-box, seaborn is built on top of matplotlib.
"""
import seaborn as sns
import random as rand
import numpy as np
from matplotlib import pyplot as plt


def demo_die_roll():
    """
    Roll a die 600 times and plot it as a bar chart.
    :return: the visualization plot
    """
    rolls = [rand.randrange(1, 7) for i in range(600)]
    values, frequencies = np.unique(rolls, return_counts=True)
    axes = sns.barplot(x=values, y=frequencies, palette="muted", hue=values, legend=False)
    axes.set_title(f"Die rolls for {len(rolls)} times")
    plt.show()

if __name__ == '__main__':
    demo_die_roll()