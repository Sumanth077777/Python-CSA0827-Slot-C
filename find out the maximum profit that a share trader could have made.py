def max_profit(prices):
    if not prices:
        return 0
    n = len(prices)
    first_buy = -prices[0]
    first_sell = 0
    second_buy = float('-inf')
    second_sell = 0
    for i in range(1, n):
        first_buy = max(first_buy, -prices[i])
        first_sell = max(first_sell, first_buy + prices[i])
        second_buy = max(second_buy, first_sell - prices[i])
        second_sell = max(second_sell, second_buy + prices[i])
    return second_sell
prices = [7,1,5,3,6,4]
print(prices)
print(max_profit(prices))
