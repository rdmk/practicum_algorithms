def find_longest_word(string):
    quantity_of_word = 0
    for i in string:
        if len(i) > quantity_of_word:
            quantity_of_word = len(i)
            longest_word = i
    return longest_word, quantity_of_word


words = input().split()
print('\n'.join(map(str, find_longest_word(words))))
