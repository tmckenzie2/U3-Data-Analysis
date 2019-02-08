import numpy as np

header = ["CarName", "ModelYear", "MSRP"]
msrp_table = [["ford pinto", 75, 2769],
            ["toyota corolla", 75, 2711],
            ["ford pinto", 76, 3025],
            ["toyota corolla", 77, 2789]]

# just made up some extra rows for testing
# not based on any real information
msrp_table_long = [["ford pinto", 75, 2769],
            ["toyota corolla", 75, 2711],
            ["toyota camry", 75, 3025],
            ["ford pinto", 76, 3300],
            ["toyota corolla", 76, 2789],
            ["ford f150", 76, 4023],
            ["toyota corolla", 77, 3789],
            ["ford pinto", 77, 1925],
            ["toyota camry", 77, 2999],
            ["toyota rav4", 77, 2399],
            ["toyota 4runner", 77, 3999]]

def get_column(table, column_index):
    column = []
    for row in table:
        if row[column_index] != "NA":
            column.append(row[column_index])

    return column

def get_frequencies(table, column_index):
    column = sorted(get_column(table, column_index))
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

def group_by(table, column_index, include_only_column_index=None):
    # first identify unique values in the column
    group_names = sorted(list(set(get_column(table, column_index))))

    # now, we need a list of subtables
    # each subtable corresponds to a value in group_names
    # parallel arrays
    groups = [[] for name in group_names]
    for row in table:
        # which group does it belong to?
        group_by_value = row[column_index]
        index = group_names.index(group_by_value)
        if include_only_column_index is None:
            groups[index].append(row.copy()) # note: shallow copy
        else:
            groups[index].append(row[include_only_column_index])

    return group_names, groups

def compute_bin_frequencies(values, cutoffs):
    freqs = [0] * len(cutoffs)
    for val in values:
        for i, cutoff in enumerate(cutoffs):
            if val <= cutoff:
                freqs[i] += 1
                break
    return freqs

def compute_equal_widths_cutoffs(values, num_bins):
    # first things first...need to compute the width using the range
    values_range = max(values) - min(values)
    width = values_range / num_bins
    # width is a float...
    # using range() we can compute the cutoffs
    # if possible, your application allows for it, convert min, max, width
    # to intgers
    # we will work with floats 
    # np.arange() works with floats
    cutoffs = list(np.arange(min(values) + width, max(values) + width, width))
    # round each cutoff to 1 decimal place before we return it
    cutoffs = [round(cutoff, 1) for cutoff in cutoffs]
    return cutoffs