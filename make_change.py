def make_change(coins, n):
    memo = {}

    def get_change(coins, money, index):
        if money == 0:
            return 1

        if index >= len(coins):
            return 0

        amount_with_coin = 0
        ways = 0

        key = str(money) + "-" + str(index)
        if key in memo:
            return memo[key]

        while amount_with_coin <= money:
            remaining = money - amount_with_coin
            ways += get_change(coins, remaining, index + 1)
            amount_with_coin += coins[index]

        memo[key] = ways
        return ways

    print get_change(coins, n, 0)

make_change([25, 5, 10, 1], 27)
