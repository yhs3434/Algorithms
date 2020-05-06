function solution(participant, completion) {
    let answer = '';

    let obj = {};
    for (let part of participant) {
        if (part in obj) {
            obj[part] += 1;
        } else {
            obj[part] = 1;
        }
    }

    for (let comp of completion) {
        if (comp in obj) {
            obj[comp] -= 1;
            if (obj[comp] == 0) {
                delete obj[comp];
            }
        } else {
            console.log('error');
        }
    }

    answer = Object.keys(obj)[0];

    return answer;
}

console.log(solution(["leo", "kiki", "eden"], ['eden', 'kiki']))