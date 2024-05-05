# STATUS 8 PASSED / 13
def find_fewest_coins(coins, target):
    coins_change = []
    coins = coins[::-1]

    ctr = 0
    one_loop = False

    if target < 0:
        raise ValueError("target can't be negative")
    elif target == 0:
        return []
    else:
        change = [target % coins[i] == 0 for i in range(len(coins))]

        if len(list(set(change))) == 1 and list(set(change))[0] == False:
            raise ValueError("can't make target with given coins")

        else:
            for coin in coins:
                if target - coin == 0:
                    return [coin]

            while target > 0:
                if target % coins[ctr] == 0 and not one_loop:
                    coins_change.append(coins[ctr])
                    target -= coins[ctr]

                # elif target - coins[ctr] >= 0 and one_loop:
                #     coins_change.append(coins[ctr])
                #     target -= coins[ctr]

                else:
                    ctr += 1

                if ctr == len(coins):
                    ctr = 0
                    one_loop = True


    return sorted(coins_change)