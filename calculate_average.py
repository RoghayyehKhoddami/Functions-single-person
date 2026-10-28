def numbers_sum(num):
    list = num
    First_calculate = sum(num)
    return(numbers_avr(First_calculate, list))


def numbers_avr(a, b):  
    total = a
    count = len(b)
    avr = total / count
    print(f"{avr:.2f}")


def main(*recive):
    while True:
        try:
            recive = input() .split()
            numbers = list(map(float, recive))
            break
        except ValueError:
            print("Invalid Input! Enter a valid input.")
    return(numbers_sum(numbers))

main()