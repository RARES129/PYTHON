def compare_dicts(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1.keys():
        val1 = dict1[key]
        val2 = dict2[key]

        if isinstance(val1, dict) and isinstance(val2, dict):
            if not compare_dicts(val1, val2):
                return False
        elif isinstance(val1, set) and isinstance(val2, set):
            if set(val1) != set(val2):
                return False
        elif isinstance(val1, list) and isinstance(val2, list):
            if val1 != val2:
                return False
        elif val1 != val2:
            return False
    return True


def main():
    dict1 = {"a": {"b": [1, 2, 3], "c": 2}, "d": {"e": 3, "f": 4}}
    dict2 = {"a": {"b": [3, 2, 1], "c": 2}, "d": {"e": 3, "f": 4}}
    print(compare_dicts(dict1, dict2))


main()
