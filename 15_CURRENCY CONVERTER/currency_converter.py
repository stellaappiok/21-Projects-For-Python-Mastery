import requests
from pprint import PrettyPrinter

API_KEY = "ENTER YOUR API KEY HERE"

printer = PrettyPrinter()


def get_currencies():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
    data = requests.get(url).json()

    return data["supported_codes"]


def print_currencies(currencies):
    for code, name in currencies:
        print(f"{code} - {name}")


def exchange_rate(currency1, currency2):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency1}"

    data = requests.get(url).json()

    if data["result"] != "success":
        print("Invalid currencies.")
        return

    rates = data["conversion_rates"]

    if currency2 not in rates:
        print("Invalid currency.")
        return

    rate = rates[currency2]

    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = amount * rate

    print(f"{amount} {currency1} is equal to {converted_amount:.2f} {currency2}")

    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        print("")
        command = input(
            "Enter one of the commands above or (q to quit): ").lower()

        if command == "q":
            break

        elif command == "list":
            print_currencies(currencies)

        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()

            convert(currency1, currency2, amount)

        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()

            exchange_rate(currency1, currency2)

        else:
            print("Unrecognized command!")


main()
