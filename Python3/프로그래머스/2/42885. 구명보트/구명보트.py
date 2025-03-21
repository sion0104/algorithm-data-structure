# 한 번에 최대 2명, 무게 제한: limit

def solution(people, limit):
    people.sort()
    answer = 0
    
    left, right = 0, len(people)-1
    
    while left <= right:
        if left != right and people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    return answer
# 반환값: 구명보트 개수의 최소값