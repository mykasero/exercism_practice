"exchange tasks"
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchanged_value = budget / exchange_rate
    
    return exchanged_value
def get_change(budget, exchanging_value):
    """
 
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    budget_left = budget - exchanging_value
    
    return budget_left
def get_value_of_bills(denomination, number_of_bills):
    """
 
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    bills_value = denomination * number_of_bills
    return bills_value
def get_number_of_bills(amount, denomination):
    """
 
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    bills_amount = int(amount/denomination)
    
    return bills_amount
def get_leftover_of_bills(amount, denomination):
    """
 
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    bills_leftover = amount%denomination
   
    return bills_leftover
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_exchange_rate = exchange_rate + (exchange_rate*(spread/100))
    after_exchange = budget/new_exchange_rate
    leftover = after_exchange%denomination
    exchange_value = int(after_exchange - leftover)
    
    return exchange_value
