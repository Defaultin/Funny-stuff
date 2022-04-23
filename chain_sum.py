class chain_sum(int):
    def __call__(self, number=0):
        return chain_sum(self + number)


def main():
    print(chain_sum(1)(2)(3)())
    print(chain_sum(1)(2)(3))
    print(1 + chain_sum(2)(3))


if __name__ == '__main__':
    main()
