bank = {
    1: 10,
    3: 5,
    4: 4,
    10: 10,
    50: 3,
    100: 4,
}
money = [1, 3, 4, 10, 50, 100]

client_n = int(input("Кол-во клиентов: "))

for c in range(client_n):
    print("Клиент", c+1)
    sum = int(input("Сумма: "))
    t = [float("inf")] * (sum+1)
    t[0] = 0
    for m in range(1, sum+1):
        for i in range(len(money)):
            if m >= money[i] and t[m-money[i]] + 1 < t[m]:
                t[m] = t[m-money[i]] + 1

    ans = {}
    while (sum > 0):
        for i in range(len(money)):
            if t[sum-money[i]] == t[sum] - 1:
                sum -= money[i]
                if money[i] in ans:
                    ans[money[i]] += 1
                else:
                    ans[money[i]] = 1
                break

    ans_keys = list(ans.keys())
    bank_copy = bank.copy()

    status = True
    for coin in ans_keys:
        bank_copy[coin] -= ans[coin]
        if bank_copy[coin] < 0:
            status = False
            break
    if status:
        bank = bank_copy
        sorted_tuple = sorted(ans.items(), key=lambda x: -x[0])
        print("Выдача: ", dict(sorted_tuple))
        print("Банк:", bank)
    else:
        print("Сумму выдать невозможно")