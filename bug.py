def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result) # This will raise a ZeroDivisionError

result2 = function_with_uncommon_error(0, 10)
print(result2) #This will return 10 correctly