def function_with_uncommon_error_solution(x):
    if x == 0:
        return float('inf') # Or raise a more descriptive exception
    else:
        return x + 5