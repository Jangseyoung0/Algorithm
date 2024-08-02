def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sub=array[commands[i][0]-1:commands[i][1]]
        sub.sort()
        answer.append(sub[commands[i][2]-1])
    return answer