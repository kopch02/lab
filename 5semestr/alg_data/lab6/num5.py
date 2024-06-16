print("Программа, просит ввести слово и список похожих не него через пробел, как результат найдётся самое похожее из списка")
word = input("Введите слово-> ")
similar_words = input("Введите список слов-> ").split()

words = {}
for word_s in similar_words:
    m = len(word)
    n = len(word_s)
    lookup = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word[i-1] == word_s[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])
    words[word_s] = lookup[n][m]
keys_words = list(words.keys())
sorted_tuple = sorted(words.items(), key=lambda x: -x[1])
print("Самое похожее слово -> ", sorted_tuple[0][0])