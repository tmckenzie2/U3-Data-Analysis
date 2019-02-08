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

def histogram_example():
    plt.figure()

    mean = 100
    stddev = 5
    x = np.random.normal(mean, stddev, 1000)

    plt.hist(x, bins=20) # bins by default is 10
    plt.savefig("histogram_example.pdf")

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
    # task: define/call a function that creates a box plot of MSRP data grouped
    # by ModelYear
    # hint: write a utility function (or ??) to get the MSRP data only out of
    # the groups
    plt.savefig("box_plot_example.pdf")

def mrsp_grouped_by_year_box_plot_example(msrps, year_names):
    plt.figure()
    plt.boxplot(msrps)
    xtick_locs = list(range(1, len(msrps) + 1))
    plt.xticks(xtick_locs, year_names)
    plt.title("MSRP Grouped by Model Year")
    plt.xlabel("Model Year")
    plt.ylabel("MSRP")
    plt.savefig("msrp_grouped_by_year_box_plot_example.pdf")

# lets chart!!
def main():
    line_chart_example()
    bar_chart_example()
    pie_chart_example()
    histogram_example()

    values, counts = utils.get_frequencies(utils.msrp_table, utils.header.index("ModelYear"))
    # parallel arrays
    print(values)
    print(counts)

    # solutions to bar and pie chart tasks
    bar_chart_example(values, counts, "model_year_bar_chart.pdf")
    pie_chart_example(values, counts, "model_year_pie_chart.pdf")

    year_names, year_groups = utils.group_by(utils.msrp_table, utils.header.index("ModelYear"))
    print(year_names)
    print(year_groups)

    box_plot_example()

    # solution to msrp grouped by model year box plot task
    print("operating on a longer table for testing msrp grouped by year")
    year_names, year_msrp_groups = utils.group_by(utils.msrp_table_long, utils.header.index("ModelYear"), 
        include_only_column_index=utils.header.index("MSRP"))
    print(year_names)
    print(year_msrp_groups)
    mrsp_grouped_by_year_box_plot_example(year_msrp_groups, year_names)

    # discretization
    # converting a numeric (continuous) attribute to discrete (categorical)
    # we will implement equal width bin discretization
    values = sorted(np.random.choice(100, 20)) # 20 values in [0, 100)
    print(values)
    cutoffs = utils.compute_equal_widths_cutoffs(values, 5)
    print("cutoffs:", cutoffs)
    # compare to np.histogram()
    np_freqs, np_cutoffs = np.histogram(values, 5)
    print("np_cutoffs:", np_cutoffs[1:])
    # task: write a function to compute the frequencies for the
    # bins defined by cutoffs
    # check your work with numpy np_freqs
    freqs = utils.compute_bin_frequencies(values, cutoffs)
    print("freqs:", freqs)
    print("np_freqs:", np_freqs)
    # now we can plot our own histogram using cutoffs, freqs, and a bar chart
    # TODO: adjust bar widths to be width of bins
    bar_chart_example(cutoffs, freqs, "our_own_histogram_example.pdf")


if __name__ == "__main__":
    main()