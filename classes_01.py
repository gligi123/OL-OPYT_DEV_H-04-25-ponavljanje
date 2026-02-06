
class User:
    """
    Predstavlja korisnika pretplate.

    Polja:
    - name: string
    - balance: int  (pozitivno znači dugovanje, 0 znači nema duga)
    """
    # STUDENT CODE START
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance
    # STUDENT CODE END

    def charge(self, amount: int) -> None:
        """Povećaj dugovanje (balance) za amount ako je amount > 0."""
        # STUDENT CODE START
        if amount > 0:
            self.balance = self.balance + amount
        # STUDENT CODE END

    def pay(self, amount: int) -> None:
        """Smanji dugovanje (balance) za amount ako je amount > 0. Balance ne smije pasti ispod 0."""
        # STUDENT CODE START
        # self.balance = max(0, self.balance - amount)
        if amount > 0:
            if self.balance - amount < 0:
                self.balance = 0
            else:
                self.balance = self.balance - amount
        # STUDENT CODE END


#region User
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
#endregion
