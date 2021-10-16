import random


def one_action(levers, a_t):
    n = random.random()
    if n < levers[a_t]:
        return 1
    return 0


def main():
    levers = [0.4, 0.6, 0.2, 0.3, 0.8, 0.5]
    a_t = 4
    print(one_action(levers, a_t))


if __name__ == "__main__":
    main()
