import statistics
import unittest

def calculate_statistics(data):
    """
    Calculate the mean, median, and standard deviation of the given numerical data.

    Args:
        data (list): A list of numerical data.

    Returns:
        tuple: A tuple containing the mean, median, and standard deviation of the data.
    """
    if not data:
        raise ValueError("Input list cannot be empty")

    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)

    return mean, median, std_dev


class TestStatisticsCalculations(unittest.TestCase):
    """Test cases for statistical calculations."""
    
    def test_valid_data(self):
        """Test valid input data."""
        data = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_statistics(data), (3, 3, 1.5811388300841898))
        
    def test_empty_data(self):
        """Test empty input data."""
        with self.assertRaises(ValueError):
            calculate_statistics([])
        
    def test_single_element_data(self):
        """Test input data with a single element."""
        data = [5]
        self.assertEqual(calculate_statistics(data), (5, 5, 0))
        
    def test_negative_data(self):
        """Test input data with negative numbers."""
        data = [-1, -2, -3, -4, -5]
        self.assertEqual(calculate_statistics(data), (-3, -3, 1.5811388300841898))

if __name__ == '__main__':
    unittest.main()
