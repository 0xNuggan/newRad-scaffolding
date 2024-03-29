from ..distributions.standard_praise import PraiseDistribution
import plotly.express as px
import pandas as pd
from IPython.display import Markdown, display
import json


# header = "# Histogram"
# description = f"This is a histogram of the { self.objectName} object. It's stored in /reward_systems/straight_distribution as a regular python module. Apart from perfoming the analysis, it can also output a visual representation with a specific header (above) and description text. "
author = "Nuggan"
Last_updated = "2022."
version = ""


def run(praise_distribution_data, _config={}):
    """
    Runs the main module function: a table with the highest rated contributions of this round

    Args:
        praise_distribution_data: The object with the reward distribuiton system
    Raises:
        [TODO]: Check for errors and raise them
    Returns:
        res: a DataFrame with the requested results.

    """

    praise_distribution = PraiseDistribution.generate_from_dict(
        praise_distribution_data
    )

    toppraise = (
        pd.DataFrame(praise_distribution.praiseTable)
        .sort_values(by=["AVG SCORE"], ascending=False)
        .iloc[:10]
    )

    return toppraise


def printDescription(praise_distribution_data, _config={}):
    """
    Prints the description of the analysis module to be displayed above the graph

    Args:
        praise_distribution_data: The object with the reward distribuiton system
    Raises:
        [TODO]: Check for errors and raise them
    Returns:
        nothing, it prints the texts

    """
    name = praise_distribution_data["name"]
    header = f"### Top 10 highest rated contributions"
    description = (
        f"The ten highest rated contributions for this round were the following:"
    )

    display(Markdown(header))
    display(Markdown(description))


def printGraph(praise_distribution_data, _config={}):
    """
    Prints a visualization of the histogram generated by run(). This function is itended to be called from inside the jupyter notebook

    Args:
        praise_distribution_data: The object with the reward distribuiton system
    Raises:
        [TODO]: Check for errors and raise them
    Returns:
        nothing, it prints the figure

    """

    toppraise = run(praise_distribution_data)

    top10_table = f"\
| Avg. score | To | Reason |\n \
|:-----------|----|-------:|\n"
    for kr, row in toppraise.iterrows():
        from_user = row["FROM USER ACCOUNT"]
        to_user = row["TO USER ACCOUNT"]
        reason = row["REASON"]
        score = row["AVG SCORE"]

        top10_table += f"| {score} | {to_user} | {reason} |\n"
        # print(f'Praise score average: {score}\nFROM {from_user} TO {to_user},reason:\n{reason}\n')

    display(Markdown(top10_table))
