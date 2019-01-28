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

# summary statistics