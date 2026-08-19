

import time
from functools import lru_cache


# =========================================================
# UNOPTIMIZED ALGORITHM
# =========================================================

def fibonacci_unoptimized(n):
    """
    Recursive Fibonacci implementation.

    This implementation recalculates the same subproblems
    repeatedly.

    Example:
        fib(5)
        -> fib(4) + fib(3)

    fib(3) is calculated multiple times.

    Approximate complexity: O(2^n)
    """

    if n <= 1:
        return n

    return (
        fibonacci_unoptimized(n - 1)
        + fibonacci_unoptimized(n - 2)
    )


# =========================================================
# OPTIMIZED ALGORITHM
# =========================================================

@lru_cache(maxsize=None)
def fibonacci_optimized(n):
    """
    Optimized implementation using memoization.

    Each Fibonacci number is calculated once and stored.
    Future requests retrieve the result from the cache.

    Approximate complexity: O(n)
    """

    if n <= 1:
        return n

    return (
        fibonacci_optimized(n - 1)
        + fibonacci_optimized(n - 2)
    )


# =========================================================
# TIMER FUNCTIONS
# =========================================================

def measure_unoptimized(n):

    start = time.perf_counter()

    result = fibonacci_unoptimized(n)

    end = time.perf_counter()

    return result, end - start


def measure_optimized(n):

    # Remove results from previous experiments
    fibonacci_optimized.cache_clear()

    start = time.perf_counter()

    result = fibonacci_optimized(n)

    end = time.perf_counter()

    return result, end - start


# =========================================================
# EXPERIMENT
# =========================================================

def run_experiment():

    # Different workload sizes
    test_values = [25, 30, 32, 34, 36, 38]

    print("=" * 78)

    print(
        "HPC OPTIMIZATION EXPERIMENT:"
        " REDUNDANT COMPUTATION VS MEMOIZATION"
    )

    print("=" * 78)

    print(
        f"{'N':<8}"
        f"{'Result':<15}"
        f"{'Normal Time':<18}"
        f"{'Optimized Time':<20}"
        f"{'Speedup':<12}"
    )

    print("-" * 78)

    for n in test_values:

        normal_result, normal_time = measure_unoptimized(n)

        optimized_result, optimized_time = measure_optimized(n)

        # Ensure both algorithms return the same answer
        assert normal_result == optimized_result

        if optimized_time != 0:
            speedup = normal_time / optimized_time
        else:
            speedup = 0

        print(
            f"{n:<8}"
            f"{normal_result:<15}"
            f"{normal_time:<18.8f}"
            f"{optimized_time:<20.8f}"
            f"{speedup:<12.2f}"
        )

    print("-" * 78)

    print("\nExperiment completed successfully.")


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":
    run_experiment()