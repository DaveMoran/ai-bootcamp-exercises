import numpy as np

np.set_printoptions(legacy="1.25")


def create_sample_array() -> np.ndarray:
    """
    Create a NumPy array of integers 0-99.

    Returns:
        1D NumPy array of shape (100,)
    """
    # TODO: Use np.arange()
    return np.arange(100)


def array_statistics(arr: np.ndarray) -> dict:
    """
    Calculate basic statistics on array.

    Args:
        arr: NumPy array

    Returns:
        Dictionary with mean, std, min, max
    """
    # TODO: Use arr.mean(), arr.std(), etc.
    np_mean = np.mean(arr)
    np_std = round(np.std(arr), 2)
    np_min = np.min(arr)
    np_max = np.max(arr)

    return {"mean": np_mean, "std": np_std, "min": np_min, "max": np_max}


def filter_array(arr: np.ndarray, threshold: float) -> np.ndarray:
    """
    Return elements greater than threshold.

    Args:
        arr: Input array
        threshold: Value threshold

    Returns:
        Filtered array
    """
    # TODO: Use boolean indexing
    mask = arr > threshold
    filtered_arr = arr[mask]

    return filtered_arr


def count_above_threshold(arr: np.ndarray, threshold: float) -> int:
    """
    Count elements above threshold.

    Args:
        arr: Input array
        threshold: Value threshold

    Returns:
        Count of elements
    """
    # TODO: Use boolean indexing and .sum()
    mask = arr > threshold
    filtered_arr = arr[mask]

    return filtered_arr.sum()


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """
    Normalize array to 0-1 range.

    Formula: (arr - min) / (max - min)

    Args:
        arr: Input array

    Returns:
        Normalized array
    """
    # TODO: Implement using vectorized operations
    mask = (arr - arr.min()) / (arr.max() - arr.min())
    normalized_arr = arr[mask]

    return normalized_arr


if __name__ == "__main__":
    arr = create_sample_array()
    stats = array_statistics(arr)

    print(f"Array stats: {stats}")

    filtered = filter_array(arr, 50)
    print(f"Filtered (>50): {filtered.size} elements")
