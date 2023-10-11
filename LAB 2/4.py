def song(notes, moves, start):
    song = []
    for move in moves:
        song.append(notes[start + move])
    return song


notes = input().split()
moves = input().split()
moves = [int(index) for index in moves]
start = int(input())
print(song(notes, moves, start))
