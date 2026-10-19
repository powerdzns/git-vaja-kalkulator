def sestej(a, b):
    return a + b


def odstej(a, b):
    return a - b


def pomnozi(a, b):
    return a * b


def deli(a, b):
    if b == 0:
        raise ValueError("Deljenje z nič ni dovoljeno.")
    return a / b


def main():
    print("Preprost kalkulator – Git vaja")
    print("1 - Seštevanje")
    print("2 - Odštevanje")
    print("3 - Množenje")
    print("4 - Deljenje")

    izbira = input("Izberi operacijo: ")

    if izbira not in ("1", "2", "3", "4"):
        print("Izbrana operacija ni veljavna.")
        return

    try:
        prvo_stevilo = float(input("Vnesi prvo število: "))
        drugo_stevilo = float(input("Vnesi drugo število: "))

        if izbira == "1":
            rezultat = sestej(prvo_stevilo, drugo_stevilo)
        elif izbira == "2":
            rezultat = odstej(prvo_stevilo, drugo_stevilo)
        elif izbira == "3":
            rezultat = pomnozi(prvo_stevilo, drugo_stevilo)
        else:
            rezultat = deli(prvo_stevilo, drugo_stevilo)

        print(f"Rezultat: {rezultat}")

    except ValueError as napaka:
        if izbira == "4" and str(napaka) == "Deljenje z nič ni dovoljeno.":
            print(str(napaka))
        else:
            print("Vnesi veljavno število.")


if __name__ == "__main__":
    main()