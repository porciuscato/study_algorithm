def time_to_ms(st):
    st = list(st.split(" "))
    taken_time = int(float(st[2][:-1]) * 1000)
    end_time_str = list(map(float, st[1].split(":")))
    end_time = int((end_time_str[0] * 3600 + end_time_str[1] * 60 + end_time_str[2]) * 1000 + 2999)
    start_time = end_time - taken_time + 1
    return start_time, end_time


def condition(start, end, log):
    log_s, log_e = log
    if (log_s <= start <= log_e) or (log_s <= end <= log_e) or (log_s > start and log_e < end):
        return True
    return False


def solution(lines):
    logs = []
    all_times = []
    for line in lines:
        start, end = time_to_ms(line)
        logs.append((start, end))
        all_times.append(start)
        all_times.append(end)
    all_times.sort()

    intervals = []
    try:
        idx = 0
        while True:
            s = all_times[idx]
            e = all_times[idx + 1]
            intervals.append((s, e))
            idx += 1
    except IndexError:
        pass

    answer = 0
    for interval_start, _ in intervals:

        temp = 0
        one_minute = interval_start + 999
        for log in logs:
            if log[0] > interval_start:
                break
            if condition(interval_start, one_minute, log):
                temp += 1
        answer = max(answer, temp)
    return answer


cases = [
    # ["2016-09-15 00:00:00.000 3s"],
    # ["2016-09-15 23:59:59.999 0.001s"],
    # ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"],
    # ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
    #  "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
    #  "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
    #  "2016-09-15 21:00:02.066 2.62s"]
]

for case in cases:
    print(solution(case))
