#Завершите функцию, которая принимает неотрицательное
#целое nчисло в качестве входных данных и возвращает список
#всех степеней 2с показателем степени от 0до n(включительно ).
#n = 0  ==> [1]        # [2^0]
#n = 1  ==> [1, 2]     # [2^0, 2^1]
#n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
def powers_of_two(n):
    a=[]
    while n != -1:
        a.append(2**n)
        n=n-1
    a=list(reversed(a))
    return a
   
def basic_test_cases():
        test.assert_equals(powers_of_two(0), [1])
        test.assert_equals(powers_of_two(1), [1, 2])
        test.assert_equals(powers_of_two(4), [1, 2, 4, 8, 16])
