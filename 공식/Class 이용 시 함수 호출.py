class Test:
    def fun_1(self):
        print('1')
        return

    def fun_2(self):
        print('2')
        return


def main():
    # Test.fun_1 이런식으로 하면 오류!
    T = Test()
    print(T.fun_1())
    print(T.fun_2())


main()