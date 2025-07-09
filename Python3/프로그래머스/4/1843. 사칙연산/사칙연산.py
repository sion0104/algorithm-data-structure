def solution(arr):
    numbers = []
    op = []
    
    # 입력 배열에서 숫자와 연산자 분리
    for item in arr:
        if item == "+":
            op.append(0)  # 0은 덧셈을 의미
        elif item == "-":
            op.append(1)  # 1은 뺄셈을 의미
        else:
            numbers.append(int(item))
    
    if len(numbers) == 0:
        return 0
    
    # 연산 수행 함수
    def run_op(op_type, lhs, rhs):
        return lhs + rhs if op_type == 0 else lhs - rhs
    
    # 기록을 위한 리스트 초기화
    record = []
    
    for i in range(len(numbers)):
        # 각 숫자에 대해 (최댓값, 최솟값) 튜플을 담은 리스트 초기화
        record.append([(numbers[i], numbers[i])])
        
        if i > 0:
            # 바로 인접한 두 숫자 간의 연산 결과 추가
            result = run_op(op[i-1], record[i-1][0][0], numbers[i])
            record[i-1].append((result, result))
            
            if i > 1:
                # i-2부터 0까지 역순으로 순회
                for n in range(i-2, -1, -1):
                    max_val = 0
                    min_val = 0
                    
                    # record[n]의 마지막 인덱스부터 0까지 역순으로 순회
                    for j in range(len(record[n])-1, -1, -1):
                        # 모든 가능한 조합의 연산 결과 계산
                        new_results = [
                            run_op(op[n+j], record[n][j][0], record[n+j+1][len(record[n])-1-j][0]),
                            run_op(op[n+j], record[n][j][0], record[n+j+1][len(record[n])-1-j][1]),
                            run_op(op[n+j], record[n][j][1], record[n+j+1][len(record[n])-1-j][0]),
                            run_op(op[n+j], record[n][j][1], record[n+j+1][len(record[n])-1-j][1])
                        ]
                        
                        new_min = min(new_results)
                        new_max = max(new_results)
                        
                        if j == len(record[n])-1:
                            min_val = new_min
                            max_val = new_max
                        else:
                            min_val = new_min if new_min < min_val else min_val
                            max_val = new_max if new_max > max_val else max_val
                    
                    record[n].append((max_val, min_val))
    
    # 최종 결과 반환
    return record[0][-1][0] if record[0] else 0