# Program który policzy za którym razem komputerowi udało sie wygrać w LOTTO
# Będziemy losowsać 6 różnych liczb tak długa aż będą to liczby z poprzedniego losowania Lotto
import random
wynik = [10, 15, 18, 26, 32, 40]
t =[]
licznik = 0
while t != wynik:
    t = []
    licznik += 1
    for i in range(5):
        x = random.randint(1, 49)
        while t.__contains__(x):
            x= random.randint(1, 49)
        else:
            t.append(x)
    t.sort()
    print(t)
print(f"Udało sie wylosować wygrane liczby, za {licznik} razem ")