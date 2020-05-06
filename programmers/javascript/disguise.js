function solution(clothes) {
    let answer = 1;

    let obj = {};

    for (let cloth of clothes) {
        let tag = cloth[1];
        if (tag in obj) {
            obj[tag] += 1;
        } else {
            obj[tag] = 1;
        }
    }
    for (let tag in obj) {
        answer *= (obj[tag]+1);
    }

    return answer-1;
}

console.log(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]));