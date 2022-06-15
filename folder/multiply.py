#input - 2 
#output - 2 4 8 16 ///   256

n = input('число')
for i in range(1, 17):
    i=i**n
    print(i)