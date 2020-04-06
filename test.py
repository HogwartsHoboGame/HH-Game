import unittest
import Game


class Tests(unittest.TestCase):

    # Test set_busy method of tracks
    def test1(self):
        game = Game.HH_Game(700, 700)
        game.set_game()
        game.tracks.set_busy(3)
        expected = [1, 1, 0, 1, 0, 0, 0, 0, 1, 1]
        actual = game.tracks.tracks
        self.assertEqual(expected, actual)

    # Test set_empty method of tracks
    def test2(self):
        game = Game.HH_Game(700, 700)
        game.set_game()
        game.tracks.set_empty(0)
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 1, 1]
        actual = game.tracks.tracks
        self.assertEqual(expected, actual)

    # Test is_empty method of tracks
    def test3(self):
        game = Game.HH_Game(700, 700)
        game.set_game()
        expected = True
        actual = game.tracks.is_empty(3)
        self.assertEqual(expected, actual)

    # Test get_current_tracks method of Game
    def test4(self):
        game = Game.HH_Game(700, 700)
        game.set_game()
        expected = [0, 1, 8, 9]
        actual = game.get_current_tracks()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
