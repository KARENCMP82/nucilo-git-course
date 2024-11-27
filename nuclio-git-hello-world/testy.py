import pandas as pd

try:
    pd.DataFrame()
    print("Pandas is installed!")
except ImportError:
    print("Pandas is not installed.")
