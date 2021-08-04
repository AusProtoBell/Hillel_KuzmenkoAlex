def fake_string(origin: str, change_word: str, new_word: str, qty_changes: int) -> str:
    return origin.replace(change_word, new_word, qty_changes)


some_string = 'DC makes good movies, DC makes good comics'
print(fake_string(some_string, 'DC', 'Marvel', 2))
