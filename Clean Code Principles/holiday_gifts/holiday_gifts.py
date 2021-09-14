# your task is to clean this script in
# a way that uses the code as a single function
# that takes a path and returns the total_price variable
# that meets pep8 standards and receives a 10 score using pylint

# You may need to:
# pip install autopep8
# pip install pylint


"""
Use pylint and Autopep8 to format python code
"""

import numpy as np


def gift_cost(gift_cost_path):
    """
    This function calculates the cost of all gifts whose value is under $25

    Args:
    gift_cost_path: the path of the file

    Returns:
    total_price: total price of all gifts under $25
    """
    with open(gift_cost_path, encoding="UTF-8") as gift_file:
        gift_costs = gift_file.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int

    total_price = np.sum(np.extract(gift_costs < 25, gift_costs)) * 1.08

    return total_price


if __name__ == "__main__":
    print(gift_cost('gift_costs.txt'))
