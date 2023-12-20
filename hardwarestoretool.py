#function that takes a string x then multiplies each element by a rate y
def poundconverter(x, y):
    poundlist = []
    poundstring = x.split(',')
    for i in poundstring:
        num = float(i)
        num = num * float(y)
        num = round(num, 2)
        poundlist.append(num)
    return poundlist

#function that takes a list x then if y is A it doubles all numbers + vat, or if y is B it triples all numbers
def retailprice(x,y):
    retaillist = []
    if (y == 'a') or (y == 'A'):
        for i in x:
            num = float(i)
            num = num*2 + (num*0.23)
            num = round(num, 2)
            retaillist.append(num)
        return retaillist
    if (y == 'b') or (y == 'B'):
        for i in x:
            num = float(i)
            num = num*3
            num = round(num, 2)
            retaillist.append(num)
        return retaillist


rate = input("Input the current conversion rate of STERLING to EURO: ")
goagain = 'y'
while goagain.lower() == 'y':
    numberlist = input("Please input your list of comma separated numbers: ")
    outputlist = poundconverter(numberlist, rate)
    print(f"Your converted list of values is: {outputlist}")
    retailoption = input("Would you like to\nA)Multiply each number by 2 and add VAT\nB)Multiply each number by 3\n(A/B): ")
    retailoutput = retailprice(outputlist, retailoption)
    print(f"Your converted retail list: {retailoutput}")
    
    