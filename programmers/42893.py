import re


def divide(page):
    result = []
    pos = 0
    while pos < len(page):
        if page[pos] == '<':
            end = pos
            while page[end] != '>':
                end += 1
            result.append(page[pos:end + 1])
            pos = end + 1
        else:
            end = pos
            while page[end] != '<':
                end += 1
            result.append(page[pos:end])
            pos = end
    return result


def geturl(data):
    for tag in data:
        if '<meta ' in tag and 'content=' in tag:
            for ele in tag.split(' '):
                if 'content' in ele:
                    for word in ele.split('\"'):
                        if 'http' in word:
                            return word


def gethref(data):
    result = []
    for tag in data:
        if '<a href' in tag:
            for ele in tag.split('\"'):
                if 'http' in ele:
                    result.append(ele)
                    break
    return result


def getpoint(word, data):
    point = 0
    for tag in data:
        line = re.split('[^a-z]', tag.lower())
        for ele in line:
            if ele == word:
                point += 1
    return point


def solution(word, pages):
    word = word.lower()
    database = []
    for idx in range(len(pages)):
        page = pages[idx]
        data = divide(page)
        report = {
            'index': idx,
            'point': getpoint(word, data),
            'url': geturl(data),
            'href': gethref(data),
            'link_point': 0,
            'matching': 0
        }
        database.append(report)

    for idx in range(len(database)):
        E = database[idx]
        for href in E['href']:
            for j in range(len(database)):
                ele = database[j]
                if ele['url'] == href:
                    ele['link_point'] += E['point'] / len(E['href'])

    for idx in range(len(database)):
        E = database[idx]
        E['matching'] = E['point'] + E['link_point']

    mx = -1
    mx_idx = -1
    for idx in range(len(database)):
        ele = database[idx]
        if ele['matching'] > mx:
            mx = ele['matching']
            mx_idx = ele['index']
    return mx_idx


cases = [
    ["blind", [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]],
    ["Muzi", [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]]
]

for case in cases:
    print(solution(*case))