def format_price(Price) :
     Price = abs(int(Price))
     p = f'Цена :  {Price} Рублей.'
     return  p 

print(format_price(56.24))