import collections


def anagram(input_: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)    # dict: 존재하지 않은 키값은 에러 유발,
                                                # 그래서 defaultdict() 으로 추가

    for word in input_:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())



def main():
    input_ = ["eat", "tea", "tan", "ate", "nat", "bat", "bta"]
    answer = anagram(input_)
    print(answer)


if __name__ == '__main__':
    main()
