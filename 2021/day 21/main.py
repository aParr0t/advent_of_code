# read input
with open('input.txt') as f:
    s1, s2 = f.readline().rstrip(), f.readline().rstrip()
    pos = [0, 0]
    pos[0] = int(s1[s1.index(':')+2:])-1
    pos[1] = int(s2[s2.index(':')+2:])-1

#----------part 1
# import sys
# sc = [0, 0]
# dice = 0
# throw_count = 0
# while True:
#     for turn in range(2):
#         throw_count += 3
#         throw = 0
#         for _ in range(3):
#             throw += dice+1
#             dice = (dice+1)%100
#         pos[turn] = (pos[turn]+throw)%10
#         sc[turn] += pos[turn]+1

#         if max(sc) >= 1000:
#             print(min(sc) * throw_count)
#             sys.exit()
#----------part 1

#----------part 2
win_score = 21
sc = [0, 0]
mem = {}
def play(pos: list, sc: list, pers: int, step: int, left: int):
    global mem
    # memoization
    play_id = f'{pos[0]},{pos[1]},{sc[0]},{sc[1]},{pers},{step},{left}'
    if play_id in mem:
        return mem[play_id]
    # memoization

    # base loop
    if left > 0:
        # roll the dice and play onward
        u1 = play(pos.copy(), sc.copy(), pers, step + 1, left-1)
        u2 = play(pos.copy(), sc.copy(), pers, step + 2, left-1)
        u3 = play(pos.copy(), sc.copy(), pers, step + 3, left-1)
        wins = [sum(x) for x in zip(u1, u2, u3)]
        mem[play_id] = wins
        return wins
    # base loop

    # termination
    if left == 0:
        # print('Score before move:', sc)
        pos[pers] = (pos[pers]+step)%10
        sc[pers] += pos[pers]+1  # +1 because the spaces are in range 0-9
        # print('score after move:', sc)
        if sc[0] >= win_score:
            mem[play_id] = [1, 0]
            return [1, 0]
        elif sc[1] >= win_score:
            mem[play_id] = [0, 1]
            return [0, 1]
        else: 
            # no one has won so keep playing
            pers = (pers+1)%2
            step = 0
            left = 3
            res = play(pos.copy(), sc.copy(), pers, step, left)
            mem[play_id] = res
            return res
    # termination

wins = play(pos, sc, pers=0, step=0, left=3)
print(max(wins))
#----------part 2