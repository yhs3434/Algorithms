#include <iostream>

using namespace std;

long long getCommonDiv(long long w, long long h);
long long getSub(long long n1, long long n2);

long long solution(int wo,int ho)
{
    long long w = (long long)wo;
    long long h = (long long)ho;
	long long answer = w*h;

    long long commonDiv = getCommonDiv(w, h);
    long long sw = w / commonDiv;
    long long sh = h / commonDiv;
    long long cnt = (sw + sh - 1)*commonDiv;
    answer -= cnt;

	return answer;
}

long long getCommonDiv(long long w, long long h){
    while (w != h) {
        long long subVal = getSub(w, h);
        if (w > h) {
            w = subVal;
        }
        else {
            h = subVal;
        }
    }
    return w;
}

long long getSub(long long n1, long long n2) {
    long long ret = 0;
    n1 - n2 > 0 ? ret = n1 - n2 : ret = n2 - n1;
    return ret;
}

int main(void) {
    cout << solution(8,12) << "\n" ;
    return 0;
}