def make_real_intervals(interval):
    interval = [[i[0], i[1]] for i in interval]
    if len(interval) == 1:
        return interval
    sorted_i = sorted(interval)
    print(sorted_i)
    real_intervals = []
    i = 0
    while i < (len(sorted_i) - 1):
        j = i
        while j < len(sorted_i) - 1 and sorted_i[j][1] > sorted_i[j + 1][0]:
            if sorted_i[j][1] > sorted_i[j + 1][1]:
                sorted_i[j + 1][1] = sorted_i[j][1]
                j += 1
                continue
            j += 1
        real_intervals.append([sorted_i[i][0], sorted_i[j][1]])
        i = j + 1
        if j == len(sorted_i) - 2:
            real_intervals.append(sorted_i[j + 1])
    return real_intervals


def sum_of_intervals(intervals):
    intervals = make_real_intervals(intervals)
    return sum(i[1] - i[0] for i in intervals)
