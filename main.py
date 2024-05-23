def main():
    book = "books/frankenstein.txt"
    content = get_content(book)
    total_char = get_total_char(content)
    letter_dict = count_letters(content)
    sorted_dict = dict_to_sorted_list(letter_dict)

    print(f"--- Begin report of {book} ---")
    print(f"{(total_char)} words found in the document")
    print()

    for item in sorted_dict:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")


def get_content(book):
    with open(book) as f:
        return f.read()
    

def get_total_char(text):
    return len(text.split())


def sort_on(dict):
    return dict["count"]


def count_letters(string):
    count = {}
    for s in string.lower():
        if s.isalpha():
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
    return count


def dict_to_sorted_list(dict):
    sorted_list = []
    for item in dict:
        sorted_list.append({'char': item, 'count': dict[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()