def count_chars(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def main():
    text = input()
    print(count_chars(text))


main()
