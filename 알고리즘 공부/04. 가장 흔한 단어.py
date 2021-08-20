import collections
import re


def count_word(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)  # 리스트 컴프리헨션
             .lower().split()
             if word not in banned]

    counts = collections.Counter(words) # collection.Counter -> word 갯수 세준다.
    return counts.most_common(1)[0][0]  # most_common(최빈값)


def main():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    answer = count_word(paragraph, banned)
    print(answer)


if __name__ == '__main__':
    main()
