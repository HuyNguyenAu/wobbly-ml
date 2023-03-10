import numpy as np

from .accuracy import Accuracy


class Regression(Accuracy):
    '''
    The regression accuracy class.
    '''

    def __init__(self, y: np.ndarray) -> None:
        '''
        '''
        super().__init__()

        # Calculate the precision value based on the passed-in ground truth values.
        self.precision: np.number = np.std(y) / 250

    def compare(self, predictions: np.ndarray, y: np.ndarray) -> bool:
        return np.absolute(predictions - y) < self.precision
