def get_into_error(handle):
    """
    Read in log file and roughly parse into INFO and ERROR
    """
    error_msg = ["ERROR", "IOError", "MemoryError"]
    pipeline_msg = "INFO:PipelineStatistics"
    info = []
    error = []
    with open(handle) as f:
        for line in f:
            if pipeline_msg in line:
                if not line.startswith("\x1b"):
                    info.append(line)
            elif any(msg in line for msg in error_msg):
                if not line.startswith("\x1b"):
                    error.append(line)
    return [info, error]


def clean_entry(entry):
    """
    Some INFO entries contain left-over java exceptions
    Remove these to just leave clean INFO messages
    """
    return [i[i.find("INFO"):] for i in entry]


def check_entry_list(entry_list):
    """
    Check entry list, some entries are nonsense such as wall-clock messages
    or cellprofiler version.
    """
    good_entries = []
    for entry in entry_list:
        if len(entry.split()) == 14:
            good_entries.append(entry)
    return good_entries


def parse_entry(entry):
    """
    Extract data from INFO entry
    """
    time = entry[3]
    image_no = entry[7][:-1]
    module_name = entry[9]
    module_num = entry[11][:-1]
    module_time = entry[12]
    return [image_no, time, module_name, module_num, module_time]