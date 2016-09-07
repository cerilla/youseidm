import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import youseidm

sample_dir = os.path.join(os.path.dirname(__file__), 'sampledata')

def test_campaign_init():
    """Initialize a new campaign with sample game json file.
    """
    sample = os.path.join(sample_dir, 'samplegame.json')
    game = youseidm.GameCampaign(sample)
    assert game.currentgame.gamename == 'Sample Homebrew Game'
