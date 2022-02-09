prices = [57.8, 46.51, 97, 89.876, 1.567, 46, 23.2, 67.895, 34.67, 84.558]
price_str=[]
for price in prices:
    if str(price).find('.') != -1:
        if (int(str(round(price, 2)).split(".")[-1])) > 9:
            price_str.append(f'"{(int(price)):02d} руб {(int(str(round(price, 2)).split(".")[-1])):2d} коп"')
        else:
            price_str.append(f'"{(int(price)):02d} руб {(int(str(round(price, 2)).split(".")[-1])*10):2d} коп"')
    else:
        price_str.append(f'"{(int(price)):02d} руб {0:02d} коп"')
print(','.join(price_str))


print(sorted(prices, key=float))
print(prices)



for i in range(len(prices)):
    max_price = prices[i]
    for idx in range(i, len(prices)):
        if max_price < prices [idx]:
            max_price = prices [idx]
    prices.remove(max_price)
    prices.insert(i, max_price)
print (prices)


print(f'5 максимальных цен по возрастанию: {sorted(prices[:5], reverse=False)}')

for i in range(len(prices)):
    min_price = prices[i]
    for idx in range(i, len(prices)):
        if min_price > prices [idx]:
            min_price = prices [idx]
    prices.remove(min_price)
    prices.insert(i, min_price)
print (prices)

