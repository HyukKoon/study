#아스키코드 2글자 해결해야 하는 과제.
'''
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
    i = 0
    while i < len(participant):
        tmp = participant[i]
        for j in tmp:
            tmp2 += str(ord(j))
        if tmp2 in hashlist:
            for j in range(0, int(len(tmp2)/3)):
                index = j * 3
                f_str += chr(int(tmp2[index:index+3]))
            del(participant[participant.index(f_str)])
            tmp2 = ''
            f_str = ''
            i -= 1
        else:
            tmp2 = ''
        i += 1
    answer = participant
    return answer
'''

#내장함수 hash 사용 #효율성 탈락
def solution(participant, completion):
    answer = ''
    table = []
    hashpartic = []
    for i in participant:
        table.append(hash(i))
        hashpartic.append(hash(i))
    for i in completion:
        if hash(i) in table:
            del(table[table.index(hash(i))])
    answer = participant[hashpartic.index(table[0])]
    return answer

test = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
test2 = ['josipa', 'filipa', 'marina', 'nikola']
print(solution(test, test2))

# collections의 Counter를 사용하여 dic자료형 형태인 상태로 - 연산이 가능