import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def test_initialization(self):
        account = Account('test_user', 1000.0)
        self.assertEqual(account.username, 'test_user')
        self.assertEqual(account.cash_balance, 1000.0)
        self.assertEqual(account.shares, {})
        self.assertEqual(account.transactions, [])

    def test_deposit_funds(self):
        account = Account('test_user', 1000.0)
        account.deposit_funds(500.0)
        self.assertEqual(account.cash_balance, 1500.0)
        self.assertIn(('deposit', None, 500.0), account.transactions)

    def test_withdraw_funds(self):
        account = Account('test_user', 1000.0)
        success = account.withdraw_funds(300.0)
        self.assertTrue(success)
        self.assertEqual(account.cash_balance, 700.0)
        self.assertIn(('withdraw', None, 300.0), account.transactions)

        success = account.withdraw_funds(800.0)
        self.assertFalse(success)
        self.assertEqual(account.cash_balance, 700.0)

    def test_buy_shares(self):
        account = Account('test_user', 1000.0)
        success = account.buy_shares('AAPL', 5)
        self.assertTrue(success)
        self.assertEqual(account.cash_balance, 250.0)
        self.assertEqual(account.shares['AAPL'], 5)
        self.assertIn(('buy', 'AAPL', 5, 150.0), account.transactions)

        success = account.buy_shares('GOOGL', 1)
        self.assertFalse(success)
        self.assertEqual(account.cash_balance, 250.0)

    def test_sell_shares(self):
        account = Account('test_user', 1000.0)
        account.buy_shares('AAPL', 5)

        success = account.sell_shares('AAPL', 3)
        self.assertTrue(success)
        self.assertEqual(account.shares['AAPL'], 2)
        self.assertEqual(account.cash_balance, 700.0)
        self.assertIn(('sell', 'AAPL', 3, 150.0), account.transactions)

        success = account.sell_shares('AAPL', 3)
        self.assertFalse(success)
        self.assertEqual(account.shares['AAPL'], 2)
        self.assertEqual(account.cash_balance, 700.0)

    def test_calculate_portfolio_value(self):
        account = Account('test_user', 1000.0)
        account.buy_shares('AAPL', 5)
        account.buy_shares('TSLA', 1)
        portfolio_value = account.calculate_portfolio_value()
        self.assertEqual(portfolio_value, 1350.0)

    def test_calculate_profit_loss(self):
        account = Account('test_user', 1000.0)
        account.buy_shares('AAPL', 5)
        profit_loss = account.calculate_profit_loss()
        self.assertEqual(profit_loss, -750.0)

    def test_report_holdings(self):
        account = Account('test_user', 1000.0)
        account.buy_shares('AAPL', 2)
        account.buy_shares('TSLA', 1)
        self.assertEqual(account.report_holdings(), 'AAPL: 2 shares, TSLA: 1 shares')

    def test_list_transactions(self):
        account = Account('test_user', 1000.0)
        account.deposit_funds(500.0)
        account.withdraw_funds(200.0)
        self.assertEqual(account.list_transactions(), [('deposit', None, 500.0), ('withdraw', None, 200.0)])

    def test_get_balance(self):
        account = Account('test_user', 1000.0)
        self.assertEqual(account.get_balance(), 1000.0)

    def test_get_share_quantity(self):
        account = Account('test_user', 1000.0)
        account.buy_shares('AAPL', 2)
        self.assertEqual(account.get_share_quantity('AAPL'), 2)
        self.assertEqual(account.get_share_quantity('TSLA'), 0)

if __name__ == '__main__':
    unittest.main()