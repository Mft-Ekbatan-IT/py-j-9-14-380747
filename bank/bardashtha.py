




balance = 0

transactions = []


def bardasht(bardashti:int)->list:
    """_summary_

    Args:
        bardashti (int): _description_

    Returns:
        list: _description_
    """
    global balance
    global transactions
    if amount > 0:
        if amount <= balance:
            balance -= amount
            transactions.append(amount)
            print("bardasht anjam shod. mojoodi:", balance)
        else:
            print("mojoodi kafi nist!")
    else:
        print("mablagh bayad mosbat bashe!")