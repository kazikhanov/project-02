board = list(range(1, 10))  # одномерный массив

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9,), (7, 5, 3), (1, 5, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9)]


def draw_board():
    print('-------------')
    for i in range(3):
        # выводим список board с индексов внутри -> board[0 + i * 3] = 0 ... 1 ... 2 ... 3 ... 4 ... 5 ... 6 ... 7 ... 8 ... 9
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):  # функция take_input имеет позиционный аргемент player_token, хранящий X или O
    while True:
        value = input('Куда поставить: ' + player_token +
                      ' ?')
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':  # Если поле является занятым, то "Эта клетка уже занята"
            print(
                'Эта клетка уже занята')
            continue
        board[value - 1] = player_token
        break


def check_win():
    for each in wins_coord:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:  # Проверка нашего списка кортежей
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'Выиграл')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья')
            break

main()