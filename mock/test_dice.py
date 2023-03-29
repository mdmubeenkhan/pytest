from unittest import mock
import pytest

import dice

mock_roll_dice = mock.Mock(name="mock_roll_dice", return_value=3)
dice.roll_dice = mock_roll_dice()

def test_roll_dice():
    assert dice.roll_dice == 3
