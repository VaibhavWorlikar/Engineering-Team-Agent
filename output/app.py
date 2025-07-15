import gradio as gr
from accounts import Account

# Initialize global account
account = Account(username="user1", initial_deposit=10000.0)

# ==== Business logic functions ====
def create_account(username, initial_deposit):
    global account
    account = Account(username, initial_deposit)
    return f"✅ Account created for '{username}' with initial deposit of ₹{initial_deposit}"

def deposit_funds(amount):
    account.deposit_funds(amount)
    return f"💰 Deposited ₹{amount}. Current balance: ₹{account.get_balance()}"

def withdraw_funds(amount):
    success = account.withdraw_funds(amount)
    if success:
        return f"💸 Withdrew ₹{amount}. Current balance: ₹{account.get_balance()}"
    else:
        return f"⚠️ Insufficient funds. Current balance: ₹{account.get_balance()}"

def buy_shares(symbol, quantity):
    success = account.buy_shares(symbol, quantity)
    if success:
        return f"📈 Bought {quantity} shares of {symbol}. Holdings:\n{account.report_holdings()}"
    else:
        return f"⚠️ Insufficient funds to buy {quantity} shares of {symbol}."

def sell_shares(symbol, quantity):
    success = account.sell_shares(symbol, quantity)
    if success:
        return f"📉 Sold {quantity} shares of {symbol}. Holdings:\n{account.report_holdings()}"
    else:
        return f"⚠️ Not enough shares to sell {quantity} of {symbol}."

def calculate_portfolio():
    return f"💼 Total portfolio value: ₹{account.calculate_portfolio_value()}"

def report_profit_loss():
    return f"📊 Profit/Loss Report:\n{account.report_profit_loss()}"

def list_transactions():
    transactions = account.list_transactions()
    return "📝 Transactions:\n" + "\n".join(map(str, transactions)) if transactions else "No transactions yet."


# ==== Gradio UI ====
with gr.Blocks() as demo:
    gr.Markdown("# 📊 Trading Simulation Platform")
    gr.Markdown("Simulate trading with deposits, withdrawals, buying/selling shares, and track your portfolio.")

    with gr.Tab("👤 Account Setup"):
        with gr.Column():
            username = gr.Textbox(label="Username", value="user1")
            initial_deposit = gr.Number(label="Initial Deposit", value=10000.0)
            create_acc_btn = gr.Button("Create Account")
            create_acc_output = gr.Textbox(label="Account Creation Status", lines=2)
            create_acc_btn.click(create_account, [username, initial_deposit], outputs=create_acc_output)

    with gr.Tab("💸 Transactions"):
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 💰 Deposit Funds")
                deposit_amount = gr.Number(label="Deposit Amount")
                deposit_btn = gr.Button("Deposit")
                deposit_output = gr.Textbox(label="Deposit Status", lines=2)
                deposit_btn.click(deposit_funds, [deposit_amount], outputs=deposit_output)
                
                gr.Markdown("### 💸 Withdraw Funds")
                withdraw_amount = gr.Number(label="Withdraw Amount")
                withdraw_btn = gr.Button("Withdraw")
                withdraw_output = gr.Textbox(label="Withdraw Status", lines=2)
                withdraw_btn.click(withdraw_funds, [withdraw_amount], outputs=withdraw_output)

            with gr.Column():
                gr.Markdown("### 📈 Buy Shares")
                buy_symbol = gr.Textbox(label="Symbol (e.g. TCS)")
                buy_quantity = gr.Number(label="Quantity")
                buy_btn = gr.Button("Buy")
                buy_output = gr.Textbox(label="Buy Status", lines=4)
                buy_btn.click(buy_shares, [buy_symbol, buy_quantity], outputs=buy_output)

                gr.Markdown("### 📉 Sell Shares")
                sell_symbol = gr.Textbox(label="Symbol (e.g. INFY)")
                sell_quantity = gr.Number(label="Quantity")
                sell_btn = gr.Button("Sell")
                sell_output = gr.Textbox(label="Sell Status", lines=4)
                sell_btn.click(sell_shares, [sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Tab("📈 Reports"):
        with gr.Column():
            portfolio_btn = gr.Button("📊 Calculate Portfolio Value")
            portfolio_output = gr.Textbox(label="Portfolio Value", lines=2)
            portfolio_btn.click(calculate_portfolio, outputs=portfolio_output)

            profit_loss_btn = gr.Button("📈 Report Profit/Loss")
            profit_loss_output = gr.Textbox(label="Profit/Loss Report", lines=4)
            profit_loss_btn.click(report_profit_loss, outputs=profit_loss_output)

            transactions_btn = gr.Button("📝 List Transactions")
            transactions_output = gr.Textbox(label="Transactions History", lines=10)
            transactions_btn.click(list_transactions, outputs=transactions_output)

demo.launch()
