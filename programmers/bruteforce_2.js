function get_prime_list(n){
    let prime_list = Array()
    for (let i = 0; i < n; i++){
        prime_list[i] = true
    }
    prime_list[0] = false
    prime_list[1] = false
    let mx = Math.sqrt(n)
    for (let i = 2; i < mx + 1; i++){
        if (prime_list[i] === true){
            for (let j = i + i; j < n; j += i){
                prime_list[j] = false
            }
        }   
    }
    return prime_list
}

var answer = 0
var visited = new Array()
var prime_list = new Array()


function solution(numbers) {
    var answer = 0;
    return answer;
}