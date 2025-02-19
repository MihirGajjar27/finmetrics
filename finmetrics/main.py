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
    :type annual_returns: list[float] || numpy ndarray

    :return: Holding Period Return for a wide range of periods
    :rtype: float
    """
    accumulator = 1
    for i in annual_returns:
        accumulator *= (1 + i)
    return accumulator - 1
