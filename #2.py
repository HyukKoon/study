#한 사람의 전화번호가 다른사람의 전화번호로 시작되면 안됨
def solution(phone_book):
    answer = True
    for i in range(0, len(phone_book)):
        if i+1 < len(phone_book): #<= 이여야 할 수도 있음
            next = phone_book[i+1]
        if len(phone_book[i]) < len(next[0:len(phone_book[i])]):
            if phone_book[i] == phone_book[i+1]:
                answer = False
                return answer

    return answer
# 슬라이싱을 이용하여 문자열끼리 비교하려는 방법을 쓰려했으나 hash와 관련이 있는 방법으로 고민 필요.
tmp = ['119', '97674223', '1195524421']

print(solution(tmp))


# if tmp == tmp2[0:len(tmp)]:
#     print(True)