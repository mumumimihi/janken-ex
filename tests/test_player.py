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
    
    @patch('builtins.input', side_effect=['0'])
    def test_player0(self, mock_input):
        result = player_pon()
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['4'])
    def test_player4(self, mock_input):
        result = player_pon()
        self.assertIsNone(result)  # 何も返さない場合
    
if __name__ == '__main__':
    unittest.main()