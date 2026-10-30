




factor=[]

def resid(num_sefaresh:int,price:int)->list:
    
    """چاپ رسید خرید مشتری و محاصبه قیمت آن 
    num_sefaresh:int-> تعداد سفارش محصول 
    price:int-> مبلغ محصول 
    returns:
    چاپ فاکتور مشتری گرامممممیییی"""
    
    
    mohasebe=num_sefaresh*price*1.1
    factor.append(mohasebe)
    print(factor)