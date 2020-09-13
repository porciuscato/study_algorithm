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


def solution(play_time, adv_time, logs):
    p_time = time_to_sec(play_time)
    a_time = time_to_sec(adv_time)

    all_time = [0 for _ in range(p_time)]
    dp = [0 for _ in range(p_time)]
    for log in logs:
        start, end = map(time_to_sec, log.split("-"))
        for i in range(start, end):
            all_time[i] += 1

    intervals = []
    check = 0
    while check < p_time:
        if all_time[check]:
            i_start = check
            i_end = i_start
            while i_end < p_time and all_time[i_end]:
                i_end += 1
            intervals.append((i_start, i_end))
            check = i_end + 1
        check += 1

    for interval in intervals:
        length = 0
        for i in range(interval[0], interval[1]):
            if length < a_time:
                dp[i] = dp[i - 1] + all_time[i]
                length += 1
            else:
                value = dp[i - 1] + all_time[i] - all_time[i - length]
                dp[i] = value

    mx = 0
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            if dp[i] > mx:
                mx = dp[i]
                mx_time = i - a_time + 1
                if mx_time < 0:
                    mx_time = 0
    return sec_to_time(mx_time)


cases = [
    ("02:03:55", "00:14:15",
     ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]),
    ("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]),
    ("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
]

for case in cases:
    print(solution(*case))
