#price = 100
#discount = 5

#price_with_discount = price - price * discount /100

#print(price_with_discount)




def discounted(price,discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99 :
        raise ValueError('Максимальная скидка не может быть больще 99%')
    if discount >= max_discount :
        price_with_discount = price
    else:
       price_with_discount = price - price * discount /100
    return price_with_discount

discounted(100,50,max_discount=100)
#p = discounted(100,101)
#print(p)
#discounted(60,-30)
#discounted(80,500)
#product = {'name': 'Samsung s10', 'stock': 8,'price':50000.0,'discount':50}
#product['witch_discount'] = discounted(product['price'], product['discount'])
#print(product)
#discount('Привет',[1,2,3])