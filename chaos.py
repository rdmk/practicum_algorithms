def chaos(temp):
    chaos_days = 0
    for i in range(len(temp)):
        if len(temp) == 1:
            return 1
        elif i == 0:
            if temp[i] > temp[i + 1]:
                chaos_days += 1
        elif i == (len(temp) - 1):
            if temp[(len(temp) - 1)] > temp[(len(temp) - 2)]:
                chaos_days += 1
        else:
            if temp[i - 1] < temp[i] > temp[i + 1]:
                chaos_days += 1
    return chaos_days


k = int(input())
timeseries = list(map(int, input().split()))
print(chaos(timeseries))
