from typing import List
from game import TicTocGame, BoardValue
from redis import Redis


class GameRegistry(object):
    """
    Interface for game store
    """

    def __init__(self):
        self.redis = Redis(host="redis", port=6379)

    def is_game_exist(self, id: str) -> bool:
        """
        check if a game id exists
        """
        board_str = self.redis.get(id)
        return board_str is not None

    def get_game(self, id: str) -> List[BoardValue]:
        """
        get game board from game registry table
        """
        if not self.is_game_exist():
            raise ValueError("Game {} does not exist in the registry".format(id))
        board_str = self.redis.get(id)
        board = self._deserialize_board(board_str)
        return board

    def load_game(self, id: str) -> TicTocGame:
        """
        load the game from game registry
        """
        board_str = self.redis.get(id)
        board = self._deserialize_board(board_str)
        return TicTocGame(id, board)

    def save_game(self, game: TicTocGame) -> None:
        """
        save the board to game registry table
        """
        board_str = self._serialize_board(game.board)
        self.redis.set(game.id, board_str)

    def _serialize_board(self, board: List[BoardValue]) -> str:
        chars = ['-' if v == BoardValue.EMPTY else v.value for v in board]
        return ''.join(chars).encode()

    def _deserialize_board(self, s: str) -> List[BoardValue]:
        s = s.decode()
        return [BoardValue.EMPTY if c == '-' else BoardValue(c) for c in s]
