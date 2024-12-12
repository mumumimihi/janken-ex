import unittest
from unittest.mock import patch
from source.computer import computer_pon


# テストクラス
class TestComputer(unittest.TestCase):
    
    @patch('random.choice',return_value='グー')
    def test_handG(self,mock_input):
        result = computer_pon()
        self.assertEqual(result, "グー")

    @patch('random.choice',return_value='チョキ')
    def test_handT(self,mock_input):
        result = computer_pon()
        self.assertEqual(result, "チョキ")

    @patch('random.choice',return_value='パー')
    def test_handP(self,mock_input):
        result = computer_pon()
        self.assertEqual(result, "パー")
    
if __name__ == '__main__':
    unittest.main()