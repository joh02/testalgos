# Funktionale Programmierung in Python

# Beispiel 1: Verzicht auf innere Zustände und Zustandsänderungen (Seiteneffekte)

# Imperative Programmierung
def add_numbers_imperative(a, b):
    result = a + b
    print(f"Sum: {result}")
    return result

# Funktionale Programmierung
def add_numbers_functional(a, b):
    result = a + b
    return result

# Beispiel 2: Semantische Analyse und regelbasierte Transformation

# Imperative Programmierung
def square_numbers_imperative(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

# Funktionale Programmierung
def square_numbers_functional(numbers):
    return list(map(lambda x: x ** 2, numbers))

# Beispiel 3: Anwendung funktionaler Programmierung für die Bedeutung in der Informatik

# Imperative Programmierung (Beispiel: Summe der Quadrate)
def sum_of_squares_imperative(numbers):
    squared_numbers = square_numbers_imperative(numbers)
    result = sum(squared_numbers)
    return result

# Funktionale Programmierung (Beispiel: Summe der Quadrate)
def sum_of_squares_functional(numbers):
    return sum(square_numbers_functional(numbers))

# Beispielanwendung
input_numbers = [1, 2, 3, 4, 5, 7]

# Imperative Programmierung
print("Imperative Programmierung:")
result_imperative = sum_of_squares_imperative(input_numbers)
print(f"Summe der Quadrate: {result_imperative}")

# Funktionale Programmierung
print("\nFunktionale Programmierung:")
result_functional = sum_of_squares_functional(input_numbers)
print(f"Summe der Quadrate: {result_functional}")

# Funktion, die eine Higher-Order Funktion zurückgibt
def adder(summand):
    def add_to(x):
        return x+summand
    return add_to

add5 = adder(5)

print(add5(10))