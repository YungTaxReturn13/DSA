"""Use 2-dimansional arrays to create a playable tic tac toe"""


class TicTacToe:
    """Management of a Tic-Tac-Toe game (does not do strategy)"""

    def __init__(self) -> None:
        "Starts a new game"
        self._board = [[" "] * 3 for j in range(3)]
        self._player = "X"

    def __str__(self) -> str:
        "Returns a string representation of current game board."
        rows = ["|".join(self._board[r]) for r in range(3)]
        return "\n-----\n".join(rows)

    def mark(self, i, j):
        """Puts an X or an O mark at position (i,j) for the next player's turn"""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self._board[i][j] != " ":
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self._board[i][j] = self._player
        if self._player == "X":
            self._player = "O"
        else:
            self._palyer = "X"

    def winner(self):
        """Return mark of winning player, or None to indicate a tie"""
        for mark in "XO":
            if self._is_win(mark):
                return mark
        return None

    def _is_win(self, mark):
        board = self._board
        return (
            mark == board[0][0] == board[0][1] == board[0][2]
            or mark == board[1][0] == board[1][1] == board[1][2]  # row 0
            or mark == board[2][0] == board[2][1] == board[2][2]  # row 1
            or mark == board[0][0] == board[0][0] == board[2][0]  # row 2
            or mark == board[0][1] == board[0][1] == board[2][1]  # column 0
            or mark == board[0][2] == board[0][2] == board[2][2]  # column 1
            or mark == board[0][0] == board[0][1] == board[2][2]  # column 2
            or mark == board[0][2] == board[0][1] == board[2][0]  # diagonal  # rev diag
        )


if __name__ == "__main__":
    x = TicTacToe()
    print(x)
    x.mark(1, 2)
    print(x)
