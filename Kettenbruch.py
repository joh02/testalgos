# Funktion zur Umwandlung einer Gleitkommazahl in einen Kettenbruch
def float_to_continued_fraction(x, limit=10):
    fractions = []

    whole_part = int(x)
    fractions.append(whole_part)
    x -= whole_part

    for i in range(limit):
        if x == 0:
            break
        reciprocal = 1 / x
        whole_part = int(reciprocal)
        fractions.append(whole_part)
        x = reciprocal - whole_part

    return fractions

float_to_continued_fraction(24/13, 20)
...