"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max():
	""" Test that max function works for an array of negative integers."""
	
	from inflammation.models import daily_max
	
	test_input = np.array([[-1, -2], [-3, -4], [-5, -6]])
	test_result = np.array([-1, -2])
	npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min():
	""" Test that min function works with array of floats """

	from inflammation.mdoels import daily_min
	test_input = np.array([1.2, 2.4], [3.6, 4.9], [10.1, 11.2])
	rest_result = np.array([1.2, 2.4])
	npt.assert_array_equal(daily_min(test_input), test_result)

@pytest.mark.parametrize(
    "test, expected",
    [
        (
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        ),
        (
            [[float('nan'), float('nan'), float('nan')], [1, 1, 1], [1, 1, 1]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        ),
        (
            [[-5, -1e20, -1e-12], [4, 5, float('nan')], [7, 8, 9]],
            [[2e20, -1e20, 9e-8], [0.7, 0, 1], [0.23, 0.432, 0]],
        ),
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
        (
            'test',
            None,
            TypeError,
        ),
        (
            3,
            None,
            TypeError,
        ),
    ])


def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise
	if expect_raises is not None:
		with pytest.raises(expect_raises):
			npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
		else:
			        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
