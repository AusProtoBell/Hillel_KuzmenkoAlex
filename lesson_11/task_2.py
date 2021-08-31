def palindrome_check(some_string: str) -> bool:
    data = some_string.lower().\
        replace(' ', '').replace(',', '').replace('.', '')
    # Remove all punctuation and spaces for the test
    return data == data[::-1]


if __name__ == "__main__":
    print(palindrome_check("А роза упала на лапу Азора."))
    print(palindrome_check("Яро закусала ренегата генерала сука Зоря."))
    print(palindrome_check("Знамо, даже у ежа дома НЗ."))
    print(palindrome_check("Мастер жрет сам."))
    print(palindrome_check("Мастер орет сам."))
    print(palindrome_check("Хил, худ, а дух лих."))


    print(palindrome_check("Мастъъъер жрет сам"))
    print(palindrome_check("Мастер оръъъет сам"))
    print(palindrome_check("Хил, худ, а дух лиъъъх"))
