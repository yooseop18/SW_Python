
# 리스트 컴프리핸션
def jewel_and_stone(jewel: str, stone: str) -> int:
    return sum(s in jewel for s in stone)


def main():
    jewel = 'aA'
    stone = 'aAAbbbbb'

    answer = jewel_and_stone(jewel, stone)

    print(answer)


if __name__ == '__main__':
    main()