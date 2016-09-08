import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import pytest
import youseidm.game
import youseidm.campaign

sample_dir = os.path.join(os.path.dirname(__file__), 'sampledata')
valid_sample = os.path.join(sample_dir, 'sample_valid.json')
valid_game = youseidm.game.GameData(valid_sample)


def test_campaign_init():
    """Initialize a new campaign with sample game json file.
    """
    current_campaign = youseidm.campaign.GameCampaign(valid_game)
    assert current_campaign.game.game_name == 'homebrew'
