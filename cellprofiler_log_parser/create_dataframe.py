"""
something something docstring
"""

import pandas as pd

def to_dataframe(output):
    """
    output to dataframe
    """
    dataframe = pd.DataFrame(output)
    dataframe.columns = ["ImageNumber", "Time", "Module",
                         "Module_num", "Module_time"]
    return dataframe


def group_modules(dataframe):
    """
    convert list of lists into module names and module times
    """
    times = []
    names = []
    grouped = dataframe.groupby("Module")
    for name, group in grouped:
        names.append(name)
        time_vals = map(float, group.Module_time.values)
        times.append(time_vals)
    return [names, times]
