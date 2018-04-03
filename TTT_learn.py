from TTT_bot import Bot
from TTT_board import Board


def run_test():
    board = Board()
    bot1 = Bot(1, board)
    bot2 = Bot(2, board)
    # print(board)
    while not board.get_winner():

        if not board.can_be_played():
            break
        bot1.act()
        # print(board)

        if not board.can_be_played():
            break
        bot2.act()
        # print(board)

    bot1.learning()
    bot2.learning()
    # print(board)
    print('bot %d wins' % board.get_winner())
    return board.get_winner()


def main():
    test_number = 100000
    bot_1 = 0
    bot_2 = 0
    draw = 0
    while test_number:
        a = run_test()
        if a == 1:
            bot_1 += 1
        elif a == 2:
            bot_2 += 1
        else:
            draw += 1
        test_number -= 1
        print(test_number,
              '----------------------------------------------------------------------------------------------------')
    print('BOT 1:', bot_1, ',   BOT 2:', bot_2, ',   DRAW:', draw)


if __name__ == '__main__':
    main()
