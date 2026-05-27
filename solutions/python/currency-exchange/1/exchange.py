"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """calculating exchange money"""
    value = budget / exchange_rate
    return value
 
    
    

    



def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange."""
    currency_left = budget - exchanging_value
    return currency_left




def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination."""
    bill = denomination * number_of_bills
    return bill
    
    
    



def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount."""
    bills_unit = amount // denomination
    return bills_unit

   





def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills."""
    left_over_amount = amount % denomination
    return left_over_amount
    

    


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency."""
    actual_rate = exchange_rate * (1 + (spread/100))
    total_value = budget / actual_rate
    number_of_bills = total_value // denomination
    max_value = number_of_bills * denomination
    return int(max_value)
    
