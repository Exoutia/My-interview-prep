import unittest
from solution import min_distance
from solution_using_dynamic import maxDist

class Integrated_test_min_distance(unittest.TestCase):

    matrix1 = [[0,1,0,1],[0,0,1,0],[0,1,1,1],[0,0,0,0]]
    matrix2 = [[1,1,0],[0,0,0],[1,0,0]]

    def test_mbsf(self):
        self.assertEqual(min_distance(self.matrix1), 2)
        self.assertEqual(min_distance(self.matrix2), 2)

    def test_maxDist_dynamic(self):
        self.assertEqual(maxDist(self.matrix1), 2)
        self.assertEqual(maxDist(self.matrix2), 2)




if __name__ == "__main__":
    unittest.main()