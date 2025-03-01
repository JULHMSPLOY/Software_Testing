from algorithm_codes.grid_challenge import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_grid_challenge_case1(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case2(self):
        grid = ['zxywv', 'ponml', 'kjihg', 'fedcb', 'aabcd']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case3(self):
        grid = ['abc', 'def', 'ghi']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case4(self):
        grid = ['zyx', 'wvu', 'tsr']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case5(self):
        grid = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case6(self):
        grid = ['a', 'b', 'c', 'd', 'e']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case7(self):
        grid = ['ab', 'bc', 'cd']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case8(self):
        grid = ['ba', 'dc', 'fe']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case9(self):
        grid = ['acbd', 'dfeg', 'hijk', 'lmno']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case10(self):
        grid = ['ab', 'ab', 'ab']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case11(self):
        grid = ['abc', 'cde', 'efg']
        result = gridChallenge(grid)
        self.assertEqual(result)

    def test_grid_challenge_case12(self):
        grid = ['zyx', 'abc', 'def']
        result = gridChallenge(grid)
        self.assertEqual(result)
