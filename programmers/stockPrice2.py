def solution(prices):
    st = []
    st_idx = [-1]

    length = len(prices)
    answer = [0 for i in range(length)]

    for i in range(length):
        p = prices[i]
        while(len(st)>0):
            cur_p = st_get(st, st_idx)
            if(p<cur_p[0]):
                idx = cur_p[1]
                answer[idx] = i - idx
                continue
            else:
                st_put(cur_p, st, st_idx)
                break
        st_put((p, i), st, st_idx)
    index = length-1
    while(len(st)):
        cur_p = st_get(st, st_idx)
        idx = cur_p[1]
        answer[idx] = index - idx
    return answer

def st_put(val, st, idx):
    st.append(val)
    idx[0]+=1
    return

def st_get(st, idx):
    value = st[idx[0]]
    del st[idx[0]]
    idx[0]-=1
    return value

print(solution([1, 2, 3, 2, 3]))