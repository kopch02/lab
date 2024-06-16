def one():
    money = [1, 3, 4, 10, 50, 100]
    n = int(input("Сумма: "))

    ans = {}
    m_r = reversed(money)
    for coin in m_r:
        count = n // coin
        if count > 0:
            ans[coin] = count
        n = n % coin
    print(ans)


def two():
    money = [1, 3, 4, 10, 50, 100]
    n = int(input("Сумма: "))

    t = [float("inf")] * (n + 1)
    t[0] = 0

    for m in range(1, n + 1):
        for i in range(len(money)):
            if m >= money[i] and t[m - money[i]] + 1 < t[m]:
                t[m] = t[m - money[i]] + 1

    ans = {}

    while (n > 0):
        for i in range(len(money)):
            if t[n - money[i]] == t[n] - 1:
                n -= money[i]
                if money[i] in ans:
                    ans[money[i]] += 1
                else:
                    ans[money[i]] = 1
                break

    res = sorted(ans.items(), key=lambda x: -x[0])
    print(dict(res))