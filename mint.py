import json
from mintapi import mintapi as mp

def calculate_loan_payoff(loanBalance, extraPayment):
    interestRate = 0.0275
    monthlyPayment = 800.15
    monthsToPayoff = 0
    while loanBalance > 0:
        monthsToPayoff = monthsToPayoff + 1
        loanBalance = loanBalance - (monthlyPayment - (loanBalance * interestRate / 12) + extraPayment)
    if extraPayment > 0:
        return f"Current mortgage payoff rate {monthsToPayoff} months with extra payments of ${extraPayment}."
    else:
        return f"Current mortgage payoff rate {monthsToPayoff} months."

mint = mp.Mint(
'YOUR EMAIL HERE',  # Email used to log in to Mint
'YOUR PASSWORD HERE',  # Your password used to log in to mint
# Optional parameters
# mfa_method='soft-token',  # See MFA Methods section
                    # Can be 'sms' (default), 'email', or 'soft-token'.
                    # if mintapi detects an MFA request, it will trigger the requested method
                    # and prompt on the command line.
mfa_input_callback=None,  # see MFA Methods section
                            # can be used with any mfa_method
                            # A callback accepting a single argument (the prompt)
                            # which returns the user-inputted 2FA code. By default
                            # the default Python `input` function is used.
# mfa_token='RECSOYYMO465V2NSAQZQ24XQYXNGLBS4',   # see MFA Methods section
                    # used with mfa_method='soft-token'
                    # the token that is used to generate the totp
headless=True,  # Whether the chromedriver should work without opening a
                    # visible window (useful for server-side deployments)
use_chromedriver_on_path=True,  # True will use a system provided chromedriver binary that
                                    # is on the PATH (instead of downloading the latest version)
)
accounts = mint.get_account_data()

loan_payoff_no_extra_payments = ""
loan_payoff_extra_payments = ""
mortgage_balance = ""
for account in accounts:
    if(account['name'] == 'FICS Mortgage - XXXX0671'):
        mortgage_balance = f"Mortgage Balance: ${abs(float(account['value']))}"
        loan_payoff_extra_payments = calculate_loan_payoff(abs(float(account['value'])), 2500)
        loan_payoff_no_extra_payments = calculate_loan_payoff(abs(float(account['value'])), 0)

networth = f"Net Worth: ${mint.get_net_worth()}"

x = {
    "netWorth" : networth,
    "mortgageBalance": mortgage_balance,
    "loanPayoffExtra": loan_payoff_extra_payments,
    "loanPayoffNoExtra": loan_payoff_no_extra_payments
}

y = json.dumps(x)

print(y)


