import sys

# read input
with open('input.txt') as f:
    draw_nums = [int(x) for x in f.readline().rstrip().split(',')]
    f.readline()
    raw_boards = f.read().replace('\n', ' ').split(' ')
    raw_boards = [int(x) for x in raw_boards if x]
    boards = [raw_boards[i*25:(i+1)*25] for i in range(len(raw_boards)//25)]

#----------part 1
# for draw_num in draw_nums:
#     for i in range(len(boards)):
#         board = boards[i]
#         bingo = False
#         if draw_num in board:
#             idx = board.index(draw_num)
#             board[idx] = '#'

#             offset = idx % 5
#             for y in range(5):
#                 if board[y*5 + offset] != '#':
#                     break  # no bingo
#             else:
#                 bingo = True

#             offset = (idx // 5) * 5
#             for x in range(offset, offset + 5):
#                 if board[x] != '#':
#                     break  # no bingo
#             else:
#                 bingo = True
#         if bingo:
#             rem_nums = [x for x in board if x != '#']
#             print(sum(rem_nums) * draw_num)
#             sys.exit()
#----------part 1


#----------part 2
not_won_boards = list(range(len(boards)))
for draw_num in draw_nums:
    for i in reversed(not_won_boards):
        board = boards[i]
        bingo = False
        if draw_num in board:
            idx = board.index(draw_num)
            board[idx] = '#'

            offset = idx % 5
            for y in range(5):
                if board[y*5 + offset] != '#':
                    break  # no bingo
            else:
                bingo = True

            offset = (idx // 5) * 5
            for x in range(offset, offset + 5):
                if board[x] != '#':
                    break  # no bingo
            else:
                bingo = True
        if bingo:
            if i in not_won_boards:
                del not_won_boards[not_won_boards.index(i)]
            if len(not_won_boards) == 0:
                rem_nums = [x for x in board if x != '#']
                print(sum(rem_nums) * draw_num)
                sys.exit()
#----------part 2