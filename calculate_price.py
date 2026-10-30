def calculate_price(price: int, tax_rate = 0.1) -> float :
    total = float(price * (tax_rate + 1))
    return (total)

def main():
    while True:
        try:
            first = int(input())
        except EOFError:
            print("please Enter a number!")
            continue
        except ValueError:
            print("please Enter a correct number!")
            continue

        try:
            second = input()
            if second == "":
                print(calculate_price(first, second = 0.1))
            else:
                second = float(second)
                print(calculate_price(first, second))
        except EOFError:
            print(calculate_price(first, second = 0.1))
        except ValueError:
            print("please Enter a correct number!")
            continue