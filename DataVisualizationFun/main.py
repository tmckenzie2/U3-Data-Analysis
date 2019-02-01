import numpy as np
import matplotlib.pyplot as plt 

import utils

# data visualization fun
# EDA: exploratory data analysis
# goals of data vis:
# 1. clearly and accurate represent data
# 2. be creative with the goal of increasing readability and understanding
# 3. label the units and points of interest

# jargon
# 2D visualizations are usually called charts
# plot: is a chart of data points for example scatter plot
# graph: is a chart of a math function e.g. sine curve

# how to use matplotlib
# 1. pyplot module: like state machine where there is a current "figure"
# 2. OOP interface: maintain object references
# 3. mix of the two

def line_chart_example():
    x = [0, 1, 2, 3, 4]
    y = [value ** 2 for value in x]

    plt.plot(x, y, label="X values squared")

    # labels!!
    plt.title("My First Plot :)")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.legend()
    

    #plt.show() # shows a window
    plt.savefig("line_chart_example.pdf")

def get_frequencies(table, column_index):
    column = sorted(utils.get_column(table, column_index))
    values = []
    counts = []

    for value in column:
        if value not in values:
            values.append(value)
            # first time we have seen this value
            counts.append(1)
        else: # we've seen it before, the list is sorted...
            counts[-1] += 1

    return values, counts

# lets chart!!
def main():
    line_chart_example()

    values, counts = get_frequencies(utils.msrp_table, utils.header.index("ModelYear"))
    print(values)
    print(counts)

if __name__ == "__main__":
    main()