import unittest
import numpy as np
from MatrixGame import nash_equilibrium

M_0 = np.array(
    [[4, 0, 6, 2, 2, 1],
     [3, 8, 4, 10, 4, 4],
     [1, 2, 6, 5, 0, 0],
     [6, 6, 4, 4, 10, 3],
     [10, 4, 6, 4, 0, 9],
     [10, 7, 0, 7, 9, 8]]
)


class TestMatrixGame(unittest.TestCase):
    # def setUp(self):
    #     self.calculator = Calculator()

    def test_gameValue(self):
        self.assertAlmostEqual(nash_equilibrium(M_0)[0], 4.870967741935485)

    def test_strategy_first(self):
        self.assertTrue(np.allclose(
            nash_equilibrium(M_0)[1], np.array([0, 4 / 31, 3 / 31, 27 / 62, 21 / 62, 0]))
        )

    def test_strategy_second(self):
        self.assertTrue(np.allclose(
            nash_equilibrium(M_0)[2], np.array([0, 0, 257/372, 9/62, 55/372, 1/62]))
        )


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
