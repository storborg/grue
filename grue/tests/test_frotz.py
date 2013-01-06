import os.path

from unittest import TestCase

from grue.frotz import Frotz

here = os.path.dirname(os.path.abspath(__file__))
games_dir = os.path.join(os.path.dirname(here), 'games')
game_path = os.path.join(games_dir, 'zork1.z5')


class TestFrotz(TestCase):

    def test_sequence(self):
        frotz = Frotz(game_path)
        resp = frotz.listen()
        self.assertIn('There is a small mailbox here.', resp)
        self.assertEqual(frotz.score, 0)
        self.assertEqual(frotz.moves, 0)
        self.assertEqual(frotz.location, 'West of House')

        frotz.tell('open mailbox')
        resp = frotz.listen()
        self.assertIn('reveals a leaflet', resp)
        self.assertEqual(frotz.score, 0)
        self.assertEqual(frotz.moves, 1)
        self.assertEqual(frotz.location, 'West of House')

        frotz.tell('move north')
        # this should be an unrecognized instruction
        resp = frotz.listen()
        self.assertIn("don't understand", resp)
        self.assertEqual(frotz.score, 0)
        self.assertEqual(frotz.moves, 1)
        self.assertEqual(frotz.location, 'West of House')

        frotz.tell('go north')
        resp = frotz.listen()
        self.assertIn('narrow path winds', resp)
        self.assertEqual(frotz.score, 0)
        self.assertEqual(frotz.moves, 2)
        self.assertEqual(frotz.location, 'North of House')
