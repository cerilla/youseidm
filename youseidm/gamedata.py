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

        minimal_metadata = ['gamename']

        with open(gamefile) as f:
            info = json.loads(f.read())
            print(info)
            for k, v in info.items():
                setattr(self, k, v)

        for metadata in minimal_metadata:
            if not hasattr(self, metadata):
                raise NameError("{} is not defined".format(metadata))
