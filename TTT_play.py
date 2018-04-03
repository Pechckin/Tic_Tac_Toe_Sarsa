from TTT_board import Board
from TTT_bot import Bot
import json


def run_test():
    board = Board()
    bot1 = Bot(1, board)
    bot2 = Bot(2, board)
    who_goes_first = input('КТО ХОДИТ ПЕРВЫЙ(Me/0)')
    if who_goes_first == '0':
        while not board.get_winner():
            print(board)
            if not board.can_be_played():
                break
            bot1.act()
            print(board)
            if not board.can_be_played():
                break
            where = []

            x = int(input('ВАШ ХОД:'))
            if x == 1:
                where.append(0)
                where.append(0)
            elif x == 2:
                where.append(0)
                where.append(1)
            elif x == 3:
                where.append(0)
                where.append(2)
            elif x == 4:
                where.append(1)
                where.append(0)
            elif x == 5:
                where.append(1)
                where.append(1)
            elif x == 6:
                where.append(1)
                where.append(2)
            elif x == 7:
                where.append(2)
                where.append(0)
            elif x == 8:
                where.append(2)
                where.append(1)
            elif x == 9:
                where.append(2)
                where.append(2)

            board.move(2, where)
        bot1.learning()
    else:
        while not board.get_winner():
            print(board)
            if not board.can_be_played():
                break
            where = []

            x = int(input('ВАШ ХОД:'))
            if x == 1:
                where.append(0)
                where.append(0)
            elif x == 2:
                where.append(0)
                where.append(1)
            elif x == 3:
                where.append(0)
                where.append(2)
            elif x == 4:
                where.append(1)
                where.append(0)
            elif x == 5:
                where.append(1)
                where.append(1)
            elif x == 6:
                where.append(1)
                where.append(2)
            elif x == 7:
                where.append(2)
                where.append(0)
            elif x == 8:
                where.append(2)
                where.append(1)
            elif x == 9:
                where.append(2)
                where.append(2)

            board.move(1, where)
            if not board.can_be_played():
                break
            bot2.act()
            print(board)
        bot2.learning()

    print(board)
    print('bot %d wins' % board.get_winner())


def main():
    test_number = 1
    while test_number:
        run_test()
        test_number -= 1


if __name__ == '__main__':
    main()
'''
   board = Board()
   bot1 = Bot(1, board)
   bot1.load_strategy()
   strategy = bot1.strategy
   print(strategy['11000002'])
   #strategy['11000002'].remove({'move': [0, 0], 'score': -187.57})
   #print(strategy['11000002'])

   
   fd = open('strategy.json', 'w')
   json.dump(strategy, fd)
   fd.close()
   '''
