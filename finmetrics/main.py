import numpy as np
from typing import Sequence, Union


# Basic Return Calculations
def holding_period_return(beginning_value: float, ending_value: float, total_income: float = 0.0) -> float:
    """
    :param beginning_value: starting value of an underlying asset
    :type beginning_value: float

    :param ending_value: ending value of an underlying asset
    :type ending_value: float

    :param total_income:
    :type total_income: float

    :return: holding period return for a period between: time @ ending value & time @ beginning value
    :rtype: float
    """
    if beginning_value == 0:
        raise ValueError("Beginning Value must be non zero")
    return (ending_value - beginning_value + total_income) / beginning_value


def holding_period_return_multi_period(annual_returns: Union[Sequence[float], np.ndarray]) -> float:
    """
    :param annual_returns: A list or numpy ndarray of annual returns for a series of periods
    :type annual_returns: list[float] or numpy ndarray

    :return: Holding Period Return for a wide range of periods
    :rtype: float
    """
    if not annual_returns:
        raise ValueError("annual_returns must contain at least 1 value")
    if not isinstance(annual_returns, (Sequence, np.ndarray)):
        raise ValueError("annual_returns must be a sequence of floats or numpy array")
    try:
        accumulator = 1
        for i in annual_returns:
            accumulator *= (1 + i)
        return accumulator - 1
    except Exception as e:
        raise Exception(f"Error with holding_period_return_multi_period: {e}")


def arithmetic_return(holding_period_returns: Union[Sequence[float], np.ndarray]) -> float:
    """
    :param holding_period_returns: a list or numpy ndarray of holding periods returns
    :type holding_period_returns:  list[float] or numpy ndarray

    :return: arithmetic (mean) return of array of holding period returns
    :rtype: float
    """
    if not holding_period_returns:
        raise ValueError("holding_period_returns must contain at least 1 value")
    if not isinstance(holding_period_returns, (Sequence, np.ndarray)):
        raise ValueError("holding_period_returns must be a sequence of floats or numpy array")
    try:
        return sum(holding_period_returns) / len(holding_period_returns)
    except Exception as e:
        raise Exception(f"Error with arithmetic_return: {e}")


