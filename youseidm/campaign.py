import youseidm.game


class GameCampaign(object):
    """Define the information of a campaign being played"""

    def __init__(self, gamedata):
        """Summary

        Args:
            gamefile (string): Path of gamedata json file
        """
        super(GameCampaign, self).__init__()
        self.game = gamedata
