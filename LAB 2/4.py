def compose(notes, moves, start):
    song_list = notes[:]
    print(notes[0], start)
    result = []
    result.append(song_list[start])
    for index in moves:
        start += index
        if start > len(song_list) - 1:
            start = start % len(song_list)
        result.append(song_list[start])
    return result


def main():
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


main()
