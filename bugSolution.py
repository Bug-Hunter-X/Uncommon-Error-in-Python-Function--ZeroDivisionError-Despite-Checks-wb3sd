def function_with_uncommon_error_solution(a, b):
    if b == 0:
        if a == 0:
            return 0  # Handle the case where both are zero
        else:
            return float('inf') # Or raise a ValueError, depending on desired behavior
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0)
print(result) #This will return inf

result2 = function_with_uncommon_error_solution(0, 10)
print(result2) #This will return 0.0

result3 = function_with_uncommon_error_solution(10,5)
print(result3) #This will return 2.0