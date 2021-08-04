def longest_word(some_string: str) -> str:
    some_list = some_string.split(' ')
    longest = some_list[0]
    for word in some_list:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word('What makes a good man'))