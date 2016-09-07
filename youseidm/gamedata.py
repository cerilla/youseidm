"""Summary
"""
import json


class GameData(object):
    """Define the structure of the game being played
    """

    def __init__(self, gamefile):
        """Summary

        Args:
            gamefile (string): Path of gamedata json file
        """
        super(GameData, self).__init__()
        with open(gamefile) as f:
            info = json.loads(f.read())
            print(info)
            for k, v in info.items():
                setattr(self, k, v)

        if not hasattr(self, 'gamename'):
            raise ValueError
