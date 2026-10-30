

balance = 0

transactions = []
def variz(meghdar:int)->list:
    """واریزی 

    Args:
        meghdar (int): مقدار پول واریزی 

    Returns:
        list: موجودی
    """
    global balance
    global transactions
    if meghdar > 0:
        balance += meghdar
        transactions.append(meghdar)
        print("variz anjam shod. mojoodi:", balance)
    else:
        print("mablagh bayad mosbat bashe!")