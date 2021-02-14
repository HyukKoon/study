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
    for i in participant:
        tmp = i
        for j in tmp:
            tmp2 += str(ord(j))
        if tmp2 in hashlist:
            for j in range(0, int(len(tmp2)/3)):
                index = j * 3
                f_str += chr(int(tmp2[index:index+3]))
            del(participant[participant.index(f_str)])
            print(participant)
            tmp2 = ''
            f_str = ''
        else:
            tmp2 = ''
    answer = participant
    return answer


test = ["leo", "kiki", "eden"]
test2 = ["eden", "kiki"]
print(solution(test, test2))
#
# a = [1, 2, 3, 1]
# del(a[a.index(1)])
# print(a)
# print(a.index(1))
