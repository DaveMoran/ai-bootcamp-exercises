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
    return int((arr > threshold).sum())


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
    data_norm = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

    return data_norm


def apply_threshold(arr: np.ndarray, low: float, high: float) -> np.ndarray:
    """
    Clip array values to [low, high] range.

    Args:
        arr: Input array
        low: Minimum value
        high: Maximum value

    Returns:
        Clipped array
    """
    # TODO: Use np.clip()
    clipped_arr = np.clip(arr, low, high)

    return clipped_arr


def compare_vectorized_vs_loop(size: int = 1000000):
    """Compare vectorized operation vs Python loop."""
    arr = np.random.rand(size)

    # Vectorized
    import time

    start = time.time()
    result_vec = arr * 2 + 1
    vec_time = time.time() - start

    # Python loop
    start = time.time()
    result_loop = np.array([x * 2 + 1 for x in arr])
    loop_time = time.time() - start

    print(f"Vectorized: {vec_time:.4f}s")
    print(f"Loop: {loop_time:.4f}s")
    print(f"Speedup: {loop_time/vec_time:.1f}x")


if __name__ == "__main__":
    arr = create_sample_array()
    stats = array_statistics(arr)

    print(f"Array stats: {stats}")

    filtered = filter_array(arr, 50)
    print(f"Filtered (>50): {filtered.size} elements")

    normalized_arr = normalize_array(arr)
    print(f"Normalized range: {normalized_arr}")

    clipped_arr = apply_threshold(arr, 10, 50)
    print(f"Clipped array: {clipped_arr}")
