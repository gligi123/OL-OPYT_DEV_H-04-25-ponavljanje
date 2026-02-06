"""
OOP (jednostavne klase) — 7 zadataka + assert testovi

Pravila:
- Student smije pisati SAMO unutar označenih blokova (# STUDENT CODE START/END).
- Nema @dataclass, nema @property — sve “ručno”.
- Ne mijenjati testove.
"""

# ------------------------------------------------------------
# ZAD01 — Klasa User
# ------------------------------------------------------------

class User:
    """
    Predstavlja korisnika pretplate.

    Polja:
    - name: string
    - balance: int  (pozitivno znači dugovanje, 0 znači nema duga)
    """

    def __init__(self, name: str, balance: int = 0):
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def charge(self, amount: int) -> None:
        """Povećaj dugovanje (balance) za amount ako je amount > 0."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def pay(self, amount: int) -> None:
        """Smanji dugovanje (balance) za amount ako je amount > 0. Balance ne smije pasti ispod 0."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ZAD02 — Klasa Product
# ------------------------------------------------------------

class Product:
    """
    Proizvod s cijenom.

    Polja:
    - name: string
    - price: int (>=0)
    """

    def __init__(self, name: str, price: int):
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def apply_discount(self, percent: int) -> None:
        """
        Smanji cijenu za percent (%).
        Cijena ostaje int; koristi int() za floor.
        Ako je percent <= 0, ne mijenjaj cijenu.
        """
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ZAD03 — Klasa Cart
# ------------------------------------------------------------

class Cart:
    """
    Košarica proizvoda.

    Polje:
    - items: lista Product objekata
    """

    def __init__(self):
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def add(self, product: Product) -> None:
        """Dodaj product u items."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def total(self) -> int:
        """Vrati zbroj cijena svih proizvoda u items."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ZAD04 — Klasa OrderLine
# ------------------------------------------------------------

class OrderLine:
    """
    Stavka narudžbe.

    Polja:
    - product: Product
    - qty: int (>=1)
    """

    def __init__(self, product: Product, qty: int):
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def line_total(self) -> int:
        """Vrati product.price * qty."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ZAD05 — Klasa Order
# ------------------------------------------------------------

class Order:
    """
    Narudžba ima listu stavki (OrderLine).

    Polje:
    - lines: lista OrderLine
    """

    def __init__(self):
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def add_line(self, line: OrderLine) -> None:
        """Dodaj line u lines."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def total(self) -> int:
        """Vrati sumu line_total() za sve stavke."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ZAD06 — Klasa SubscriptionManager
# ------------------------------------------------------------

class SubscriptionManager:
    """
    Upravljanje korisnicima pretplate.

    Polje:
    - users: dict {name: User}
    """

    def __init__(self):
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def add_user(self, user: User) -> bool:
        """
        Dodaj korisnika u dict.
        Ako user.name već postoji -> False, inače dodaj i True.
        """
        # STUDENT CODE START
        pass
        # STUDENT CODE END

    def total_debt(self) -> int:
        """Vrati ukupno dugovanje (zbroj balance za sve korisnike)."""
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ZAD07 — Klasa SimpleReport
# ------------------------------------------------------------

class SimpleReport:
    """
    Jednostavan izvještaj.

    Metoda build(manager) vraća string:
      "Users=<broj>, Debt=<ukupno>"
    """

    def build(self, manager: SubscriptionManager) -> str:
        # STUDENT CODE START
        pass
        # STUDENT CODE END


# ------------------------------------------------------------
# ASSERT TESTOVI
# ------------------------------------------------------------

# User
u = User("Ana", 0)
assert u.name == "Ana"
assert u.balance == 0
u.charge(20)
assert u.balance == 20
u.pay(5)
assert u.balance == 15
u.pay(100)
assert u.balance == 0
u.charge(-10)  # ignoriraj
assert u.balance == 0

# Product
p1 = Product("Kruh", 2)
p2 = Product("Sir", 10)
assert p1.name == "Kruh" and p1.price == 2
p2.apply_discount(10)
assert p2.price == 9
p2.apply_discount(0)
assert p2.price == 9

# Cart
c = Cart()
c.add(p1)
c.add(p2)
assert c.total() == 11

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

# SubscriptionManager
m = SubscriptionManager()
assert m.add_user(User("Marko", 10)) is True
assert m.add_user(User("Iva", 0)) is True
assert m.add_user(User("Marko", 5)) is False
assert m.total_debt() == 10
m.users["Iva"].charge(7)
assert m.total_debt() == 17

# SimpleReport
r = SimpleReport()
assert r.build(m) == "Users=2, Debt=17"

print("OOP (jednostavne klase) — testovi prolaze kad su klase implementirane.")
