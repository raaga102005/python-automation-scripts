import numpy as np
import pandas as pd

def demonstrate_numpy():
    """
    NumPy is the foundation of all data science in Python.
    pandas, scikit-learn, TensorFlow — all built on NumPy.
    This script shows the core concepts with real examples.
    """
    
    print("=== NumPy Basics ===\n")
    
    # 1. Creating arrays
    sales = np.array([45000, 52000, 38000, 61000, 55000, 47000])
    print(f"Sales data: {sales}")
    print(f"Shape: {sales.shape}")
    print(f"Data type: {sales.dtype}\n")
    
    # 2. Basic statistics — this is why data scientists use NumPy
    print("=== Sales Statistics ===")
    print(f"Total: ₹{np.sum(sales):,}")
    print(f"Average: ₹{np.mean(sales):,.0f}")
    print(f"Median: ₹{np.median(sales):,.0f}")
    print(f"Std deviation: ₹{np.std(sales):,.0f}")
    print(f"Highest month: ₹{np.max(sales):,}")
    print(f"Lowest month: ₹{np.min(sales):,}\n")
    
    # 3. Array operations — much faster than Python loops
    # Apply 10% growth to all months at once
    projected = sales * 1.10
    print(f"Projected sales (10% growth): {projected.astype(int)}\n")
    
    # 4. Boolean indexing — filter without loops
    high_months = sales[sales > 50000]
    print(f"Months above ₹50,000: {high_months}\n")
    
    # 5. 2D arrays — like a spreadsheet in memory
    monthly_data = np.array([
        [45000, 120, 375],  # Jan: revenue, orders, avg_order
        [52000, 138, 377],  # Feb
        [38000, 102, 373],  # Mar
        [61000, 160, 381],  # Apr
        [55000, 145, 379],  # May
        [47000, 125, 376],  # Jun
    ])
    
    print("=== 2D Array (monthly data) ===")
    print(f"Shape: {monthly_data.shape} (6 months, 3 metrics)")
    print(f"Total revenue: ₹{monthly_data[:, 0].sum():,}")
    print(f"Total orders: {monthly_data[:, 1].sum()}")
    print(f"Average order value: ₹{monthly_data[:, 2].mean():.0f}\n")
    
    # 6. Reshape — change dimensions
    flat = np.arange(12)
    matrix = flat.reshape(3, 4)
    print(f"Reshaped 12 numbers into 3x4 matrix:\n{matrix}\n")
    
    # 7. Where — conditional replacement
    # Flag months where revenue dropped below average
    avg = np.mean(sales)
    performance = np.where(sales >= avg, "Good", "Below average")
    for month, perf in zip(['Jan','Feb','Mar','Apr','May','Jun'], performance):
        print(f"{month}: {perf}")
    
    return monthly_data


def numpy_vs_loops():
    """
    Shows why NumPy is faster than Python loops.
    This is why ML libraries use NumPy under the hood.
    """
    import time
    
    size = 1_000_000
    data = list(range(size))
    np_data = np.array(data)
    
    # Python loop
    start = time.time()
    total = sum(x * 2 for x in data)
    loop_time = time.time() - start
    
    # NumPy
    start = time.time()
    total_np = np.sum(np_data * 2)
    numpy_time = time.time() - start
    
    print(f"\n=== Speed Comparison (1 million items) ===")
    print(f"Python loop: {loop_time:.4f} seconds")
    print(f"NumPy: {numpy_time:.4f} seconds")
    print(f"NumPy is {loop_time/numpy_time:.0f}x faster")


if __name__ == "__main__":
    demonstrate_numpy()
    numpy_vs_loops()
