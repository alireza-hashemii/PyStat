# Excercise 2.2
data_sum = 10 + 15 + 14 + 8 + 13
arithmetic_mean = data_sum / 5
print(arithmetic_mean)


# an average calculator
def avg_calculator(*arg):
    sum_of_datas = sum(arg)
    average = sum_of_datas / len(arg)
    return average

print(avg_calculator(5,8,10))