def solution(board, moves):
    answer = 0

    st = []
    moves.reverse()

    while moves:
        move = moves.pop() - 1
        toy = putFromMove(board, move)
        if toy==-1:
            continue
        if st and st[-1]==toy:
            st.pop()
            answer += 2
        else:
            st.append(toy)

    return answer

def putFromMove(board, move):
    boardLen = len(board)
    i = 0

    while i<boardLen and board[i][move]==0:
        i += 1

    if i==boardLen:
        return -1
    else:
        ret = board[i][move]
        board[i][move] = 0
        return ret

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
print(solution([[2]], [1]))