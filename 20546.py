money = int(input())
price = list(map(int, input().split()))

def BNP():
    todayMoney = money
    share = 0
    for todayPrice in price:
        share += todayMoney // todayPrice
        todayMoney = todayMoney % todayPrice
    return todayMoney + share * price[-1]

def TIMING():
    todayMoney = money
    share = 0
    for i in range(14):
        todayPrice = price[i]
        if i < 3:
            continue
        if price[i] > price[i-1] > price[i-2] > price[i-3]:
            todayMoney += share * todayPrice
            share = 0
        elif price[i] < price[i-1] < price[i-2] < price[i-3]:
            share += todayMoney // todayPrice
            todayMoney = todayMoney % todayPrice
    return todayMoney + share * price[-1]

bnp = BNP()
timing = TIMING()

if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")
