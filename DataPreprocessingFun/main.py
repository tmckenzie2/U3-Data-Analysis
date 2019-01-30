import numpy as np
# data preprocessing notes
# more about attributes
# 1. how is the attributes values stored
# int, str, float, tuple, etc.
# 2. semantic value of our attributes
# what do the values represent/mean
# 3. what scale was the attribute measured on
# scales are roughly categorized into two categories
# categorical vs continuous
# nominal: categorical without an inherent ordering
# name, colors
# ordinal: cateogircal with an inherent ordering
# T-shirt sizes: S, M, L, XL,...
# alphabet grades: A, A-, 
# integer: continuous based on integer values
# ratio-scaled: continuous and have a 0 value that 
# denotes "absence"
# height, weight... 0lbs that would be absence of weight
# interval-scaled: continous without a 0 value
# temperature in C or F
# 0 degrees F does not mean absence of temperature
# task: take a look the automobile dataset from PA1 
# or from the first day of class and label each attribute
# with its measurement scale

# noisy vs invalid data
# noisy: valid on the scale, but recorded incorrectly
# invalid: not valid on the scale

# missing values
# usually representing ? or NA or NaN
# few ways to deal with missing values
# 1. discard values... really only do this when dataset
# is large and number of instances missing data is small
# never throw away data
# 2. fill missing values
# categorical: majority voting system
# continous: avergae, median, central tendency
# do it intelligently... "group by" or kNN (more on this later)

def get_column(table, column_index):
    column = []
    for row in table:
        if row[column_index] != "NA":
            column.append(row[column_index])

    return column

def get_min_max(values):
    # a tuple is an immutable list
    return min(values), max(values) # return a tuple

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", "NA", 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789]]
    msrps = get_column(msrp_table, header.index("MSRP"))
    print(msrps)
    min_msrp, max_msrp = get_min_max(msrps) # unpack the returned tuple
    print(min_msrp, max_msrp)

    # summary statistics
    # mid range (mid value) (min + max) / 2
    # min, max: use the built in functions to compute
    # arithmetic mean
    mean_msrp = sum(msrps) / len(msrps)
    print("Mean:", mean_msrp)
    # sensitive to extreme values... sometimes prefer median instead
    # median is the middle value in a sorted list
    # mode is the frequently occuring value
    # we will compute the mode on friday when we talk about frequency diagrams

    # data dispersion
    # variance measures the spread of the data
    # low variance then the data is close to the mean
    # lets compute variance for msrps
    mean_diffs_squared = [(value - mean_msrp) ** 2 for value in msrps] # list comprehension
    msrp_variance = sum(mean_diffs_squared) / len(mean_diffs_squared)
    # standard deviation is the square root of variance
    msrp_std = np.sqrt(msrp_variance)
    print("Standard deviation:", msrp_std, np.std(msrps))
    # quantiles are used to partition a sequence into roughly equal sized groups
    # quartiles: 4 groups 3 data points
    # percentiles: 100 groups
    # 2-quantile: 2 groups

if __name__ == "__main__":
    main()