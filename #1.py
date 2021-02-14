# 참가자 복사해서 복사한 리스트에서 제거해야함 추후 작업은 알아서ㄱㄱ
def solution(participant, completion):
    answer = ''
    hashlist = []
    tmp2 = ''
    f_str = ''
    for i in completion:
        tmp = i
        for j in tmp:
            tmp2 += str(ord(j))
        hashlist.append(tmp2)
        tmp2 = ''
    for i in range(0, len(participant)):
        print(i)
        tmp = participant[i]
        print(tmp)
        for j in tmp:
            tmp2 += str(ord(j))
        # print(tmp2)
        # print(hashlist)
        if tmp2 in hashlist:
            for j in range(0, int(len(tmp2)/3)):
                index = j * 3
                f_str += chr(int(tmp2[index:index+3]))
            # print(f_str)
            del(participant[participant.index(f_str)])
            i -= 1
            tmp2 = ''
            f_str = ''
        else:
            tmp2 = ''
    answer = participant
    return answer


test = ["leo", "kiki", "eden"]
test2 = ["eden", "kiki"]
print(solution(test, test2))