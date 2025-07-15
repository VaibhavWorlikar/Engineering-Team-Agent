class Account:
    def __init__(self, username: str, initial_deposit: float):
        self.username = username
        self.initial_deposit = initial_deposit
        self.cash_balance = initial_deposit
        self.shares = {}  # symbol: quantity
        self.transactions = []

    def deposit_funds(self, amount: float):
        self.cash_balance += amount
        self.transactions.append(('deposit', None, amount))
    
    def withdraw_funds(self, amount: float) -> bool:
        if amount > self.cash_balance:
            return False
        self.cash_balance -= amount
        self.transactions.append(('withdraw', None, amount))
        return True

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        cost = price * quantity
        if cost > self.cash_balance:
            return False
        self.cash_balance -= cost
        self.shares[symbol] = self.shares.get(symbol, 0) + quantity
        self.transactions.append(('buy', symbol, quantity, price))
        return True

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if symbol not in self.shares or self.shares[symbol] < quantity:
            return False
        price = get_share_price(symbol)
        revenue = price * quantity
        self.shares[symbol] -= quantity
        if self.shares[symbol] == 0:
            del self.shares[symbol]
        self.cash_balance += revenue
        self.transactions.append(('sell', symbol, quantity, price))
        return True

    def calculate_portfolio_value(self) -> float:
        return sum(get_share_price(symbol) * quantity for symbol, quantity in self.shares.items())

    def calculate_profit_loss(self) -> float:
        total_value = self.calculate_portfolio_value() + self.cash_balance
        return total_value - self.initial_deposit

    def report_holdings(self) -> str:
        holdings = [f"{symbol}: {quantity} shares" for symbol, quantity in self.shares.items()]
        return ', '.join(holdings) if holdings else 'No shares owned'

    def report_profit_loss(self) -> str:
        return f"Profit/Loss: {self.calculate_profit_loss()}"

    def list_transactions(self) -> list:
        return self.transactions

    def get_balance(self) -> float:
        return self.cash_balance

    def get_share_quantity(self, symbol: str) -> int:
        return self.shares.get(symbol, 0)

def get_share_price(symbol: str) -> float:
    prices = {'AAPL': 150.0, 'TSLA': 600.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)

# The accounts.py module is now implemented as per the specified requirements.