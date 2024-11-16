# Exercise 2.3
datas = (3 * 5) + (2 * 6) + (10 * 5) + (12 * 6) + (15 * 4)
weighed_avg = datas / (3 + 2 + 5 + 6 + 4)
print(weighed_avg)

# a weighed average calculator
def weighed_mean(datas:list = None, weighs:list = None):
    ordered_pair = zip(datas, weighs)
    sum_datas = 0
    for i in ordered_pair:
        sum_datas += i[0] * i[1]

    avg = sum_datas / sum(weighs) 
    return avg


print(weighed_mean([5,6,10,12,15],[3,2,5,6,4]))