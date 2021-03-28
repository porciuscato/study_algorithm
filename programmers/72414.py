def solution(play_time, adv_time, logs):
    # 전처리
    p_h, p_m, p_s = map(int, play_time.split(":"))
    adv_h, adv_m, adv_s = map(int, adv_time.split(":"))
    play_second = p_h * 3600 + p_m * 60 + p_s
    adv_second = adv_h * 3600 + adv_m * 60 + adv_s

    logs_seconds = []
    logs_interval = [0, play_second]
    for log in logs:
        start, end = log.split("-")
        s_h, s_m, s_s = map(int, start.split(":"))
        e_h, e_m, e_s = map(int, end.split(":"))
        start_second = s_h * 3600 + s_m * 60 + s_s
        end_second = e_h * 3600 + e_m * 60 + e_s
        logs_seconds.append((start_second, end_second))
        logs_interval.append(start_second)
        logs_interval.append(end_second)
    logs_seconds.sort(key=lambda x: (x[0], x[1]))

    logs_record_with_accum = []  # start, end, accumulate
    logs_interval = sorted(list(set(logs_interval)))
    for i in range(len(logs_interval) - 1):
        s, e = logs_interval[i], logs_interval[i + 1]
        logs_record_with_accum.append([s, e, 0])

    for log_start, log_end in logs_seconds:
        for i in range(len(logs_record_with_accum)):
            inter_start, inter_end, _ = logs_record_with_accum[i]
            if inter_end <= log_start:
                continue
            elif log_start <= inter_start and inter_end <= log_end:
                logs_record_with_accum[i][2] += 1
            else:
                break

    candidates = []  # [start, times]
    for i in range(len(logs_record_with_accum)):
        log_start, log_end, accum = logs_record_with_accum[i]
        adv_end = log_start + adv_second
        temp = [log_start, 0]
        j = i
        while j < len(logs_record_with_accum):
            log_start, log_end, accum = logs_record_with_accum[j]
            if adv_end <= log_end:
                temp[1] += (adv_end - log_start) * accum
                break
            else:
                temp[1] += (log_end - log_start) * accum
                j += 1
        candidates.append(temp)
    candidates.sort(key=lambda x: (-x[1], x[0]))

    answer = candidates[0][0]
    hour = answer // 3600
    minute = (answer % 3600) // 60
    second = answer - (3600 * hour) - (minute * 60)
    return "%02d:%02d:%02d" % (hour, minute, second)


cases = [
    ("02:03:55", "00:14:15",
     ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]),
    ("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]),
    ("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]),

]

for case in cases:
    print(solution(*case))
