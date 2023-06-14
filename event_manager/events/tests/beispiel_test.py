def summe(a: int, b: int) -> int:
    return int(a + b)


def test_summe():
    assert summe(2, 2) == 4, "Summe von 2 und 2 muss 4 sein"
    assert isinstance(summe(2, 2), int), "Ergebnis von Summe muss Integer sein"


test_summe()
