import unittest
from unittest.mock import patch
from source.player import player_pon


# テストクラス
class TestPlayerPon(unittest.TestCase):
    
    @patch('builtins.input',return_value='1')
    def test_playerG(self,mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")

    @patch('builtins.input',return_value='2')
    def test_playerT(self,mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

    @patch('builtins.input',return_value='3')
    def test_playerP(self,mock_input):
        result = player_pon()
        self.assertEqual(result, "パー")
    
if __name__ == '__main__':
    unittest.main()