import unittest
from CodingPractice.PythonAssignments.excercises.RockPaperScissors import player_1_rock, player_1_paper, player_1_scissors, \
    is_valid_input


class RockPaperScissors(unittest.TestCase):

    def test_rock_rock_draw(self):
        player_2 = 'rock'
        self.assertEqual(None, player_1_rock(player_2))

    def test_paper_paper_draw(self):
        player_2 = 'paper'
        self.assertEqual(None, player_1_paper(player_2))

    def test_scissor_scissor_draw(self):
        player_2 = 'scissors'
        self.assertEqual(None, player_1_scissors(player_2))

    def test_player_1_wins_rock(self):
        player_2 = 'scissors'
        self.assertEqual(True, player_1_rock(player_2))

    def test_player_1_loses_rock(self):
        player_2 = 'paper'
        self.assertEqual(False, player_1_rock(player_2))

    def test_player_1_wins_paper(self):
        player_2 = 'rock'
        self.assertEqual(True, player_1_paper(player_2))

    def test_player_1_loses_paper(self):
        player_2 = 'scissors'
        self.assertEqual(False, player_1_paper(player_2))

    def test_player_1_wins_scissors(self):
        player_2 = 'paper'
        self.assertEqual(True, player_1_scissors(player_2))

    def test_player_1_loses_scissors(self):
        player_2 = 'rock'
        self.assertEqual(False, player_1_scissors(player_2))

    def test_caps(self):
        player_2 = 'Rock'
        self.assertEqual(True, player_1_paper(player_2))

    def test_invalid_input_player_1(self):
        player_1 = 'banana'
        player_2 = 'rock'
        self.assertFalse(is_valid_input(player_1, player_2))

    def test_invalid_input_player_2(self):
        player_1 = 'paper'
        player_2 = 'banana'
        self.assertFalse(is_valid_input(player_1, player_2))


if __name__ == '__main__':
    unittest.main()
