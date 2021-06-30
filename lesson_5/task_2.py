def symb_amount(x):
    return len(x)


def words_amount(x):
    x = x.split()
    return len(x)


some_string = input("Input your sentence: ")

print("Your sentence contains {0} words and {1} symbols"
      .format(words_amount(some_string), symb_amount(some_string)))


