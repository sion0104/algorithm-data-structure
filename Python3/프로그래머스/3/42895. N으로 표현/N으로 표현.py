def solution(N, number):
    # 8번 초과하여 사용하면 -1 반환
    if N == number:  # N이 한 번으로 만들 수 있는 경우
        return 1
        
    # 1~8번 사용하여 만들 수 있는 모든 수를 저장할 집합
    # dp[i]는 N을 i번 사용하여 만들 수 있는 수들의 집합
    dp = [set() for _ in range(9)]
    
    # N을 i번 이어붙인 수를 각 집합의 초기값으로 설정
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    # 2부터 8까지 N 사용 횟수별로 계산
    for i in range(2, 9):
        # j와 k의 합이 i가 되도록 조합
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)  # 덧셈
                    dp[i].add(num1 - num2)  # 뺄셈
                    dp[i].add(num1 * num2)  # 곱셈
                    if num2 != 0:  # 나눗셈(0으로 나누기 방지)
                        dp[i].add(num1 // num2)
        
        # i번 사용하여 number를 만들 수 있는지 확인
        if number in dp[i]:
            return i
            
    return -1  # 8번 이하로 만들 수 없는 경우