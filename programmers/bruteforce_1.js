function solution(answers) {
    let answer = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    let len = answers.length
    let vals = [answer[0].length, answer[1].length, answer[2].length]
    for (let i = 0; i < 3; i++){
        for (let j = answer[i].length; j < len; j++){
            answer[i][j] = answer[i][j % vals[i]]
        }
    }
    let ans_list = [0, 0, 0]
    for (let i = 0; i < len; i++){
        for (let j = 0; j < 3; j++){
            if (answers[i] === answer[j][i]){
                ans_list[j]++
            }
        }
    }
    let mx = Math.max(ans_list[0], ans_list[1], ans_list[2])
    let ans = Array()
    let idx = 0
    for (let i = 0; i < 3; i++){
        if (mx === ans_list[i]){
            ans[idx] = i + 1
            idx++
        }
    }
    return ans
}