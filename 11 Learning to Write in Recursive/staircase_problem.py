def staircase_problem(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return staircase_problem(n - 1) + staircase_problem(n - 2) + staircase_problem(n - 3)

print(staircase_problem(5))
