def solution(bin1, bin2):
    bin_number1, bin_number2 = int(bin1, 2), int(bin2, 2)
    return str(format(bin_number1 + bin_number2, 'b'))
    