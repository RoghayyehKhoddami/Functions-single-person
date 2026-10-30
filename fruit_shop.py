def list_check(list_fruit, list_price):
    fruits = {}
    while True:
        user_input = input() . split()

        if user_input[0] != "finish":
            list_fruit = user_input[0]
            list_price = int(user_input[1])
        else:
            break
        fruits [list_fruit] = list_price
    return(list_counter(**fruits))

def list_counter(**a):
    count = len(a)
    print(f"You have {count} fruits in your shopping list")
    price = a.values()
    return(list_sum(price), list_max_min(a))

def list_sum(c):
    price = c
    sums = sum(price)
    print(f"The total cost of the shopping list is {sums}")
    # return(list_max_min(price))


def list_max_min(b):
    maximum = (max(b.values()))
    for name, price in b.items():
        if price == maximum:
            print(f"The most expensive fruit is {name} with the price of {price}")

    minimum = (min(b.values()))
    for name, price in b.items():
            if price == minimum:
                print(f"The cheapest fruit is {name} with the price of {price}")


def main():
    return(list_check(0 , 0))


main()