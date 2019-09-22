def cumulative(l):
    cumulative_sum = 0
    new_list = []
    for i in l:
        cumulative_sum += i
        new_list.append(cumulative_sum)
    return new_list
