print("Программа, просит ввести слово и список похожих не него через пробел, как результат найдётся самое похожее из списка")
word = input("Введите слово-> ")
words_list = input("Введите список слов-> ").split()

words = {}
for word_s in words_list:
    m = len(word)
    n = len(word_s)
    t = [[0]*(n+1) for _ in range(m+1)]
    max = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word[i-1] == word_s[j-1]:
                t[i][j] = t[i-1][j-1] + 1
                if t[i][j] > max:
                    max = t[i][j]
    words[word_s] = max
keys_words = list(words.keys())
res = sorted(words.items(), key=lambda x: -x[1])
print("Самое похожее слово -> ", res[0][0])
