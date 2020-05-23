def solution(dataSource, tags):
    documents = []
    for data in dataSource:
        tag_list = data[1:]
        tag_count = 0
        for tag in tags:
            if tag in tag_list:
                tag_count += 1
        documents.append([data[0], tag_count])
    documents.sort(key=lambda x: (-x[1], x[0]))

    answer = []
    tot = 0
    for document in documents:
        if document[1]:
            answer.append(document[0])
            tot += 1
            if tot == 10:
                break
    return answer


print(solution(
    [["doc1", "t1", "t2", "t3"], ["doc2", "t0", "t2", "t3"], ["doc3", "t1", "t6", "t7"], ["doc4", "t1", "t2", "t4"],
     ["doc5", "t6", "t100", "t8"]], ["t1", "t2", "t3"]))
