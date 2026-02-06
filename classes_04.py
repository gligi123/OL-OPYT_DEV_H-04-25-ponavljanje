from typing import List


class Product:
    """
    Proizvod s cijenom.

    Polja:
    - name: string
    - price: int (>=0)
    """

    def __init__(self, name: str, price: int):
        # STUDENT CODE START
        self.name = name
        self.price = max(0, price)
        # self.price = price if price >= 0 else 0
        # if price >= 0:
        #     self.price = price
        # else:
        #     self.price = 0
        # STUDENT CODE END

    def apply_discount(self, percent: int) -> None:
        """
        Smanji cijenu za percent (%).
        Cijena ostaje int;
        Ako je percent <= 0, ne mijenjaj cijenu.
        """
        # STUDENT CODE START
        if percent > 0:
            # self.price -= int(self.price * (percent / 100))
            self.price = self.price - int(self.price * (percent / 100))
        # STUDENT CODE END


class OrderLine:
    """
    Stavka narudžbe.

    Polja:
    - product: Product
    - qty: int (>=1)
    """

    def __init__(self, product: Product, qty: int):
        # STUDENT CODE START
        self.product: Product = product
        self.qty: int = max(1, qty)
        # STUDENT CODE END

    def line_total(self) -> int:
        """Vrati product.price * qty."""
        # STUDENT CODE START
        return self.product.price * self.qty
        # STUDENT CODE END


class Order:
    """
    Narudžba ima listu stavki (OrderLine).

    Polje:
    - lines: lista OrderLine
    """

    def __init__(self):
        # STUDENT CODE START
        self.lines: List[OrderLine] = []
        # STUDENT CODE END

    def add_line(self, line: OrderLine) -> None:
        """Dodaj line u lines."""
        # STUDENT CODE START
        self.lines.append(line)
        # STUDENT CODE END

    def total(self) -> int:
        """Vrati sumu line_total() za sve stavke."""
        # STUDENT CODE START
        return sum(line.line_total() for line in self.lines)
        # STUDENT CODE END




# Product
p1 = Product("Kruh", 2)
p2 = Product("Sir", 10)
assert p1.name == "Kruh" and p1.price == 2
p2.apply_discount(10)
assert p2.price == 9
p2.apply_discount(0)
assert p2.price == 9


# OrderLine
line1 = OrderLine(p1, 3)
line2 = OrderLine(p2, 2)
assert line1.line_total() == 6
assert line2.line_total() == 18

# Order
o = Order()
o.add_line(line1)
o.add_line(line2)
assert o.total() == 24