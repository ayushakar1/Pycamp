def input(a,b,c,d):
    summ = a+b+c+d
    product= a*b*c*d
    diff = (a+b)+(c-d)
    random_operation = ((a+b-3)**c)//d
    return summ,product,diff,random_operation      #returns multiple values as a result


print(input(5,33,6,9))   #passes multiple arguments as input