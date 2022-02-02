# Storing a sequence of high score entries


class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"({self._name}, {self._score})"


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity. All entries are initially None"""

        self._board = [None] * capacity  # reserve space for future scores
        self._n = 0

    def __getitem__(self, k):
        """Return entry at index k"""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list"""
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores"""

        score = entry.get_score()

        # Does the new entry qualify as a high score? Answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):  # no score drops from the list
                self._n += 1  # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
                j -= 1  # and decrement j
            self._board[j] = entry  # when done, add new entry


if __name__ == "__main__":
    scoreboard = Scoreboard()
    for i in range(10):
        scoreboard.add(GameEntry("john", i))
    print(scoreboard)
    print("Adding another score that should knock out another score")
    scoreboard.add(GameEntry("justin", 5))
    print(scoreboard)
    print("adding score that should not be included")
    scoreboard.add(GameEntry("mike", -10))
    print(scoreboard)

