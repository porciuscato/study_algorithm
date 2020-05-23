def solution(directory, command):
    structure = directory
    for comm in command:
        com = list(comm.split(' '))
        inpt = com[0]
        if inpt == 'mkdir':
            folder = com[1]
            if folder not in structure:
                structure.append(folder)
        elif inpt == 'cp':
            depart = com[1]
            arrive = com[2]
            keyword = com[1].split('/')[-1]
            _len = len(depart)
            total = []
            for struc in structure:
                try:
                    target = struc[:_len]
                    if depart == target:
                        total.append(struc)
                except:
                    continue
            mx = max(total)  # str /hello/tmp
            all_direc = keyword + mx[_len:]
            result = arrive + '/' + all_direc
            structure.append(result)
        elif inpt == 'rm':
            target = com[1]
            _len = len(target)
            for idx, struc in enumerate(structure):
                if struc[:_len] == target:
                    # print(struc)
                    # '/hello, /hello/tmp'
                    word_length = len(target.split('/')[-1])
                    # print(word_length)
                    structure[idx] = struc[:_len - word_length]

    answer = sorted(list(set(structure)))
    try:
        answer.remove('')
    except:
        pass
    return answer


# print(solution(["/hello", "/hello/tmp", "/", "/root", "/root/abcd", "/root/abcd/etc", "/root/abcd/hello"],
#                ["mkdir /root/tmp", "cp /hello /root/tmp", "rm /hello"]))

# ["/", "/root", "/root/abcd", "/root/abcd/etc", "/root/abcd/hello", "/root/tmp", "/root/tmp/hello", "/root/tmp/hello/tmp"]

print(solution(["/"], ["mkdir /a", "mkdir /a/b", "mkdir /a/b/c", "cp /a/b /", "rm /a/b/c"]))
