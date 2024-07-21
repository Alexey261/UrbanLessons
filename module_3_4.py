def single_root_words(root_word, *other_words):
    y = root_word.casefold()
    same_words = [x for x in other_words if y in x.casefold() or x.casefold() in y]
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)