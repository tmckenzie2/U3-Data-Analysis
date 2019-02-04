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

def bar_chart_example(x=None, y=None, filename="bar_chart_example.pdf"):
    # when we want a figure
    plt.figure() # new figure for current figure
    if x is None:
        x = list(range(4))
    if y is None:
        y = list(range(100, 500, 100))

    plt.bar(x, y)
    plt.savefig(filename)
    # task: bar chart the ModelYear count information

def pie_chart_example(x=None, y=None, filename="pie_chart_example.pdf"):
    # when we want a figure
    plt.figure() # new figure for current figure
    if x is None:
        x = list(range(4))
    if y is None:
        y = list(range(100, 500, 100))

    plt.pie(y, labels=x, autopct="%1.2f%%")
    plt.savefig(filename)
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

def group_by(table, column_index):
    # first identify unique values in the column
    group_names = sorted(list(set(utils.get_column(table, column_index))))
    print(group_names)

    # now, we need a list of subtables
    # each subtable corresponds to a value in group_names
    # parallel arrays
    groups = [[] for name in group_names]
    for row in table:
        # which group does it belong to?
        group_by_value = row[column_index]
        index = group_names.index(group_by_value)
        groups[index].append(row)

    return group_names, groups

def box_plot_example():
    plt.figure()
    # the box corresponds to the 1st and 3rd quartiles of the data distribution
    # the line in the "middle" of the box is the median (AKA 2nd quartile)
    # whiskers correspond to +/- 1.5 * IQR
    # points or stars denote outliers (outside of whiskers)
    # lets do dummy data first
    mean = 100
    stdev = 5
    # we will have two boxes, so we need a list of 2 distributions
    # 1 list per distribution
    x1 = np.random.normal(mean, stdev, 1000) # 1000 samples
    x2 = np.random.normal(mean, stdev, 100) # 100 samples
    plt.boxplot([x1, x2])
    plt.xticks([1, 2], ["1000 samples", "100 samples"])
    # how to add an annotation to a plot
    ax = plt.gca() # get current axes
    ax.annotate("mean=%d\nstdev=%d" %(mean, stdev), xy=(1.5, 100.0), 
        xycoords="data", horizontalalignment="center")
    # xycoords="axes fraction" 0,0 in the bottom left and 1,1 in upper right
    ax.annotate("mean=%d\nstdev=%d" %(mean, stdev), xy=(0.5, 0.5), 
        xycoords="axes fraction", horizontalalignment="center", color="b")
    plt.savefig("box_plot_example.pdf")


# lets chart!!
def main():
    line_chart_example()
    bar_chart_example()
    pie_chart_example()
    histogram_example()

    values, counts = get_frequencies(utils.msrp_table, utils.header.index("ModelYear"))
    # parallel arrays
    print(values)
    print(counts)

    # solutions to tasks
    bar_chart_example(values, counts, "model_year_bar_chart.pdf")
    pie_chart_example(values, counts, "model_year_pie_chart.pdf")

    year_names, year_groups = group_by(utils.msrp_table, utils.header.index("ModelYear"))
    print(year_names)
    print(year_groups)

    box_plot_example()

if __name__ == "__main__":
    main()