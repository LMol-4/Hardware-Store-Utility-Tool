# Function that takes a string x, then multiplies each element by a rate y
def poundconverter(x, y):
    poundlist = []
    poundstring = x.split(',')
    for i in poundstring:
        num = float(i)
        num = num * float(y)
        num = round(num, 2)
        poundlist.append(num)
    return poundlist

# Function that takes a list x, then if y is A it doubles all numbers + VAT, or if y is B it triples all numbers
def retailprice(x, y):
    retaillist = []
    if (y == 'a') or (y == 'A'):
        for i in x:
            num = float(i)
            num2 = num * 2
            num3 = num * (0.23)
            num4 = num2 + num3
            num4 = round(num4, 2)
            retaillist.append(num4)
        return retaillist
    if (y == 'b') or (y == 'B'):
        for i in x:
            num = float(i)
            num = num * 3
            num = round(num, 2)
            retaillist.append(num)
        return retaillist

while True:
    currentmenu = 0
    while currentmenu == 0:
        print("1) Convert STERLING to EURO\n2) Retail price calculator\n3) Quit")
        currentmenu = int(input("Please select an option: "))

    if currentmenu == 1:
        rate = float(input("Input the current conversion rate of STERLING to EURO: "))
        numberlist = input("Please input your list of comma-separated numbers: ")
        eurooutputlist = poundconverter(numberlist, rate)
        print(f"Your converted list of values is: {eurooutputlist}")

    elif currentmenu == 2:
        useownlist = int(input("Would you like to - \n1) Use own list \n2) Use list previously converted from STERLING \n(1/2): "))
        if useownlist == 2:
            retailpriceinput = eurooutputlist
        else:
            retailpriceinput = input("Please input your list of comma-separated numbers: ")
            retailpriceinput = retailpriceinput.split(',')
        x2_list = retailprice(retailpriceinput, 'A')
        x3_list = retailprice(retailpriceinput, 'B')
        print("|Original ----> X2 + VAT ----> X3|")
        for x2, x3, orig in zip(x2_list, x3_list, retailpriceinput):
            print(f"|{orig}\t---->\t{x2}\t---->\t{x3}|")

    elif currentmenu == 3:
        break
