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
        grid = ['z']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case27(self):
        grid = ['m' * 5] * 5
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case28(self):
        grid = ['abab', 'baba', 'abab', 'baba']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case29(self):
        grid = ['a' * 99 + 'z'] + ['b' * 100] + ['c' * 100]
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case30(self):
        grid = ['abcd', 'bcde', 'zdef', 'efgh']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case31(self):
        grid = ['abc', 'acd', 'bbd']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case32(self):
        grid = [''.join(chr(97 + (i + j) % 26) for i in range(100)) for j in range(100)]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case33(self):
        grid = [''.join(sorted(chr(97 + (i + j) % 26) for i in range(100))) for j in range(100)]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case34(self):
        grid = [''.join(sorted(chr(97 + (i + j) % 26) for i in range(99)) + 'z') for j in range(100)]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case35(self):
        grid = ['abcde']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case36(self):
        grid = ['ac', 'bd']
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case37(self):
        grid = ['bd', 'ac']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case38(self):
        grid = ['abcd', 'bcde', 'cdef', 'dzgh']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case39(self):
        grid = ['Abc', 'Def', 'Ghi']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case40(self):
        grid = None
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case41(self):
        grid = ['abc', 'defg']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case42(self):
        grid = ['']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case43(self):
        grid = ['abc', '123', 'xyz']
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case44(self):
        grid = ['abc', 'def', 'ghi', 'jkl']  
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case45(self):
        grid = ['abc!', 'def*', 'ghi&']  
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case46(self):
        grid = []  
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_grid_challenge_case47(self):
        grid = ['a' * 1000, 'b' * 1000]  
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)
    
    def test_grid_challenge_case48(self):

if __name__ == '__main__':
    unittest.main()