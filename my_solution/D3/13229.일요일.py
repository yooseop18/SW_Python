dict = {
    'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}

T = int(input())

for test_case in range(1, T + 1):
    input_ = input()
    print(f'#{test_case} {dict[input_]}')
