def main():
    path = 'books/frankenstein.txt'
    text = read_book(path)
    num_words = count_words(text)
    chars = count_letters(text)
    sorted_list = get_sorted_list(chars)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_list:
        print(f"The '{item['char']}'  character was found {item['num']} times")
    print("--- End report ---")


def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(string):
    words = string.split()
    return len(words)


def count_letters(string):
    new_dict = {}
    for letter in string.lower():
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    return new_dict


def get_sorted_list(chars):
    sorted_list = []
    for key, value in chars.items():
        if key.isalpha():
            sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=lambda dict: dict["num"])
    return sorted_list


main()