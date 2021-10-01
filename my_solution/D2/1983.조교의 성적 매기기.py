import collections
import operator


def test3(N, K, score_arr):
    scoring_dic = {0: "A+", 1: "A0", 2: "A-",
                   3: "B+", 4: "B0", 5: "B-",
                   6: "C+", 7: "C0", 8: "C-", 9: "D0"}

    # 학생들의 총점 계산
    total_score = collections.defaultdict(float)
    for i in range(N):
        total_score[i + 1] = score_arr[i][0] * 0.35 + score_arr[i][1] * 0.45 + score_arr[i][2] * 0.2
    # dict value 값으로 정렬
    total_score = sorted(total_score.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
    # 평점 출력
    for i, student_id in enumerate(dict(total_score)):
        if student_id == K:
            return scoring_dic[i // (N / 10)]
    # 예외 처리
    return


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        score_arr = [list(map(float, input().split())) for _ in range(N)]
        answer = test3(N, K, score_arr)

        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()