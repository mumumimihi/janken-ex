import unittest
from unittest.mock import patch
from source.janken_main import main

class TestJankenMain(unittest.TestCase):
    @patch('source.janken_main.get_player_hand', return_value='rock')
    @patch('source.janken_main.get_computer_hand', side_effect=['scissors', 'rock', 'paper'])
    def test_main(self, mock_computer_hand, mock_player_hand):
        with patch('builtins.print') as mocked_print:
            main()

            mocked_print.assert_any_call("あなたの手:rock")
            mocked_print.assert_any_call("コンピューターの手:scissors")
            mocked_print.assert_any_call("あなたの勝ちです！")
            mocked_print.assert_any_call("コンピューターの手:rock")
            mocked_print.assert_any_call("あいこです！ 再度対決！")
            mocked_print.assert_any_call("コンピューターの手:paper")
            mocked_print.assert_any_call("コンピューターの勝ちです！")

            mocked_print.assert_any_call("【最終結果】")
            mocked_print.assert_any_call("あなた:1勝")
            mocked_print.assert_any_call("コンピュータ:1勝")
            mocked_print.assert_any_call("引き分けです！")

if __name__ == '__main__':
    unittest.main()