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
            groups[index].append(row)
        else:
            groups[index].append(row[include_only_column_index])

    return group_names, groups