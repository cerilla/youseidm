import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import youseidm.gamedata as yg
import pytest

sample_dir = os.path.join(os.path.dirname(__file__), 'sampledata')


def test_gamedata_init():
    # Read the gamefile.json and populate it in
    sample = os.path.join(sample_dir, 'samplegame.json')
    game = yg.GameData(sample)
    assert game.gamename == 'Sample Homebrew Game'


def test_gamedata_init_without_name():
    sample = os.path.join(sample_dir, 'sample_noname.json')
    with pytest.raises(ValueError):
        game = yg.GameData(sample)
