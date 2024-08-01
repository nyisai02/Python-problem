amount= 50
coinsert = [25, 10, 5]

while True:
    print('Amount Due:', amount)
    coin = int(input('Insert Coin: ').strip())
    for num in coinsert:
        if coin == num:
            amount -= coin
    if amount <= 0:
        print('Change Owed:', -amount)
        break