def words_sorting(*args):
    words = {}
    for word in args:
        if word not in words:
            words[word] = 0
            for letter in word:
                words[word] += ord(letter)

    sum_value = 0
    for value in words.values():
        sum_value += value

    if sum_value % 2 != 0:
        sorting_word = dict(sorted(words.items(), key=lambda x: -x[1]))
    else:
        sorting_word = dict(sorted(words.items(), key=lambda x: x[0]))

    result = ''
    for key, value in sorting_word.items():
        result += f"{key} - {value}\n"

    return result