def loop(mapping):
    visited = set()
    result = []
    current_key = "start"
    while current_key not in visited:
        visited.add(current_key)
        if mapping[current_key] not in visited:
            result.append(mapping[current_key])
        current_key = mapping[current_key]
    return result


print(
    loop(
        {
            "start": "a",
            "b": "a",
            "a": "6",
            "6": "z",
            "x": "2",
            "z": "2",
            "2": "2",
            "y": "start",
        }
    )
)
