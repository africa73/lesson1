def get_summ( one, two, delimiter = '&' ):
    s = str(one)
    f = str(two)
    p =s + delimiter + f
    return p

   
result=get_summ('Learn','python')
print(result.capitalize())