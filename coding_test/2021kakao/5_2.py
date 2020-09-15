def time_to_sec(time):
    time = list(map(int, time.split(":")))
    result = time[0] * 60 * 60 + time[1] * 60 + time[2]
    return result


def sec_to_time(sec):
    hour = sec // 3600
    minute = (sec % 3600) // 60
    second = ((sec % 3600) % 60) % 60
    if hour == 0:
        hour = "00"
    elif hour < 10:
        hour = f"0{hour}"
    if minute == 0:
        minute = "00"
    elif minute < 10:
        minute = f"0{minute}"
    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"
    return "{}:{}:{}".format(hour, minute, second)


def solve(adv_time, intervals):
    mx = 0
    mx_time = 0
    length = len(intervals)
    for start in range(length):
        taken_time = 0
        end = intervals[start][0] + adv_time
        check = start
        interval = intervals[check]
        while interval[0] <= end:
            if interval[1] <= end:
                taken_time += (interval[1] - interval[0]) * interval[2]
            else:
                taken_time += (end - interval[0]) * interval[2]
                break
            check += 1
            if check < length:
                interval = intervals[check]
            else:
                break
        if taken_time > mx:
            mx = taken_time
            mx_time = intervals[start][0]
    return mx_time


def solution(play_time, adv_time, logs):
    a_time = time_to_sec(adv_time)

    intervals = []
    time_records = []
    for log in logs:
        start, end = map(time_to_sec, log.split("-"))
        intervals.append((start, 0))
        intervals.append((end, 1))
        time_records.append((start, end))

    intervals.sort(key=lambda x: (x[0], x[1]))

    possible_intervals = []
    i_length = len(intervals)
    for i in range(i_length - 1):
        if not ((intervals[i][1] == 1) and (intervals[i + 1][1] == 0)):
            possible_intervals.append([intervals[i][0], intervals[i + 1][0]])

    for p_interval in possible_intervals:
        p_start, p_end = p_interval
        check = 0
        for record in time_records:
            if p_start >= record[0] and p_end < record[1]:
                check += 1
        p_interval.append(check)
    return sec_to_time(solve(a_time, possible_intervals))


cases = [
    ("02:03:55", "00:14:15",
     ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]),
    ("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]),
    ("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
]

for case in cases:
    print(solution(*case))
