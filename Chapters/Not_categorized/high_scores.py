class HighScores:
    def __init__(self, scores):
        self.scores = scores
        self.top_three = scores.copy()

    def latest(self):
        self.latest = self.scores[len(self.scores) - 1]
        return self.latest

    def personal_best(self):
        self.personal_best = max(self.scores)
        return self.personal_best

    def personal_top_three(self):
        self.personal_top_three = []
        if len(self.scores) >= 3:
            while len(self.personal_top_three) < 3:
                self.personal_top_three.append(max(self.top_three))
                self.top_three.pop(self.top_three.index(max(self.top_three)))
        else:
            while len(self.top_three) > 0:
                self.personal_top_three.append(max(self.top_three))
                self.top_three.pop(self.top_three.index(max(self.top_three)))

        return self.personal_top_three