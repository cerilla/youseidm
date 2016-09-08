import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import pytest
import youseidm.game

sample_dir = os.path.join(os.path.dirname(__file__), 'sampledata')
valid_sample = os.path.join(sample_dir, 'sample_valid.json')
valid_game = youseidm.game.GameData(valid_sample)


def test_game_init():
    """Initialize GameData object with a sample json information
    """

    assert valid_game.game_name == 'homebrew'
    assert valid_game.game_longname == 'Sample Homebrew Game'
    assert valid_game.package_author == 'Cerilla'
    assert valid_game.package_version == '1.0'


def test_game_init_without_game_name():
    """Intialize GameData object with a sample without gamedata field.
    When it is missing, the initializer should raise ValueError.
    """
    sample = os.path.join(sample_dir, 'sample_no_gamename.json')
    with pytest.raises(NameError):
        faulty_game = youseidm.game.GameData(sample)


def test_game_init_without_game_longname():
    """Intialize GameData object with a sample without gamedata field.
    When it is missing, the initializer should raise ValueError.
    """
    sample = os.path.join(sample_dir, 'sample_no_longname.json')
    with pytest.raises(NameError):
        faulty_game = youseidm.game.GameData(sample)
