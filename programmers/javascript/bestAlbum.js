function solution(genres, plays) {
    let answer = [];

    let obj = {};
    let obj2 = {};
    for (let i=0; i<genres.length; i++) {
        let genre = genres[i];
        let play = plays[i];
        if (genre in obj) {
            obj[genre].push([play, i]);
            obj[genre].sort((a,b) => b[0]-a[0]);
        } else {
            obj[genre] = [[play, i]];
        }
        if (genre in obj2) {
            obj2[genre] += play;
        } else {
            obj2[genre] = play;
        }
    }
    let newGenres = [];
    for (let genre in obj2) {
        newGenres.push([obj2[genre], genre]);
    }
    newGenres.sort((a, b) => {
        return b[0]-a[0];
    });
    for (let arr of newGenres) {
        let genre = arr[1];
        for (let i=0; i<obj[genre].length && i<2; i++) {
            answer.push(obj[genre][i][1]);
        }
    }

    return answer;
}

console.log(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]));