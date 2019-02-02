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
    # task: add a cubed curve
    y2 = [value ** 3 for value in x]

    plt.plot(x, y, label="X values squared")
    plt.plot(x, y2, label="X values cubed")

    # labels!!
    plt.title("My First Plot :)")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.legend()

    # lets say you want to change the axes ticks and labels
    xtick_locations = list(range(0, 5, 1))
    xtick_labels = [str(val) for val in xtick_locations]
    plt.xticks(xtick_locations, xtick_labels)
    

    #plt.show() # shows a window
    plt.savefig("line_chart_example.pdf")

def bar_chart_example():
    # when we want a figure
    plt.figure() # new figure for current figure
    x = list(range(4))
    y = list(range(100, 500, 100))

    plt.bar(x, y)
    plt.savefig("bar_chart_example.pdf")
    # task: bar chart the ModelYear count information

def pie_chart_example():
    # when we want a figure
    plt.figure() # new figure for current figure
    x = list(range(4))
    y = list(range(100, 500, 100))

    plt.pie(y, labels=x, autopct="%1.2f%%")
    plt.savefig("pie_chart_example.pdf")
    # task: pie chart the ModelYear count information

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

def histogram_example():
    plt.figure()

    mean = 100
    stddev = 5
    x = np.random.normal(mean, stddev, 1000)

    plt.hist(x, bins=20) # bins by default is 10
    plt.savefig("histogram_example.pdf")

# lets chart!!
def main():
    line_chart_example()
    bar_chart_example()
    pie_chart_example()
    histogram_example()

    values, counts = get_frequencies(utils.msrp_table, utils.header.index("ModelYear"))
    print(values)
    print(counts)

if __name__ == "__main__":
    main()