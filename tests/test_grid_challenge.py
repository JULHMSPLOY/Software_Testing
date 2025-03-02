from algorithm_codes.grid_challenge import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_grid_challenge_case1(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case2(self):
        grid = ['zxywv', 'ponml', 'kjihg', 'fedcb', 'aabcd']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case3(self):
        grid = ['abc', 'def', 'ghi']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case4(self):
        grid = ['zyx', 'wvu', 'tsr']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case5(self):
        grid = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case6(self):
        grid = ['a', 'b', 'c', 'd', 'e']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case7(self):
        grid = ['ab', 'bc', 'cd']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case8(self):
        grid = ['ba', 'dc', 'fe']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case9(self):
        grid = ['acbd', 'dfeg', 'hijk', 'lmno']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case10(self):
        grid = ['ab', 'ab', 'ab']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case11(self):
        grid = ['abc', 'cde', 'efg']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case12(self):
        grid = ['zyx', 'abc', 'def']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case13(self):
        grid = ['fgij', 'abcf', 'klmn', 'opqr']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case14(self):
        grid = ['abcd', 'efgh', 'ijkl', 'mnop']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case15(self):
        grid = ['abcd', 'bcde', 'cdef', 'defg']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case16(self):
        grid = ['lmno', 'mnop', 'opqr', 'pqrs']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case17(self):
        grid = ['abc', 'cba', 'bac']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case18(self):
        grid = ['mnpq', 'opqr', 'qrst', 'stuv']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case19(self):
        grid = ['rstuv', 'opqrs', 'ijklm', 'bcdef']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case20(self):
        grid = ['c', 'd', 'e', 'f']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case21(self):
        grid = ['abcdefg', 'hijklmn', 'opqrst', 'uvwxyz']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case22(self):
        grid = ['abc', 'def', 'xyz']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case23(self):
        grid = ['tuvw', 'abcd', 'ghij', 'mnop']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case24(self):
        grid = ['mnop', 'opqr', 'qrst', 'stuv']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case25(self):
        grid = ['pqrst', 'uvwxyz', 'ijklmn', 'abcdef']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case26(self):
        grid = ['abc$', 'd@e', 'fgh']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case27(self):

if __name__ == '__main__':
    unittest.main()