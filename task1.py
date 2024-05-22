import timeit
from collections import defaultdict


def find_coins_greedy(coins, change):
    coins = sorted(coins, reverse=True)
    result = defaultdict(int)

    for coin in coins:
        if coin <= change:
            coin_num = change // coin
            result[coin] = coin_num
            change -= coin * coin_num
    return dict(result)


def find_min_coins(coins: list, change: int, result=None):
    result = defaultdict(int) if result is None else result

    if change <= 0:
        return dict(result)

    coins = sorted(coins, reverse=True)

    max_coin = coins.pop(0)

    if max_coin <= change:
        max_coin_num = change // max_coin
        result[max_coin] = max_coin_num
        change -= max_coin * max_coin_num

    return find_min_coins(coins, change, result)


coins = [50, 25, 10, 5, 2, 1]

greedy_result = timeit.timeit(lambda: find_coins_greedy(coins, 52138), number=1000000)
dynamic_result = timeit.timeit(lambda: find_min_coins(coins, 52138), number=1000000)
print('Greedy: ', greedy_result)
print('Dynamic:', dynamic_result)
