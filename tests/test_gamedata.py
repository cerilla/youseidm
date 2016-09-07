import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import youseidm.gamedata as yg
import pytest

sample_dir = os.path.join(os.path.dirname(__file__), 'sampledata')


def test_gamedata_init():
    """Initialize GameData object with a sample json information
    """
    sample = os.path.join(sample_dir, 'samplegame.json')
    game = yg.GameData(sample)
    assert game.gamename == 'Sample Homebrew Game'


def test_gamedata_init_without_name():
    """Intialize GameData object with a sample without gamedata field.
    When it is missing, the initializer should raise ValueError.
    """
    sample = os.path.join(sample_dir, 'sample_noname.json')
    with pytest.raises(ValueError):
        game = yg.GameData(sample)
