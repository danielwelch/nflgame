import unittest

import nflgame


class TestGame(unittest.TestCase):

    def test_games(self):
        expected = ["L.McCoy", "T.Pryor", "S.Vereen", "A.Peterson", "R.Bush"]
        games = nflgame.games(2013, week=1)
        players = nflgame.combine_game_stats(games)
        for i, p in enumerate(players.rushing().sort('rushing_yds').limit(5)):
            self.assertEqual(p.name, expected[i])
