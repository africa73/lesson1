def format_price(Price) :
     Price = abs(int(Price))
     p = f'Цена :  {Price} Рублей.'
     return  p 
#255
print(format_price(56.24))