class RandomWalks:
    def __init__(self, repetition=20):
        self.repeat = repetition


    def one_D(self):
        from tools_1D.tools import tossing_thecoin, final_score
        p1points = 0
        p2points = 0
        rounds = 0
        
        while p1points < self.repeat and p2points < self.repeat:
            rounds += 1
            p1points, p2points = tossing_thecoin(p1points, p2points)
            print("Player 1:", p2points, "| Player 2:", p2points)

        final_score(p1points, p2points, rounds)

        return p1points, p2points


rw = RandomWalks()
# for i in range(1, 10):
#     print(rw.flip_coin())

print(rw.one_D())
