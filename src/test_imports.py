#!/usr/bin/env python3
import os
import sys
import tempfile
from pathlib import Path

cache_dir = Path(tempfile.gettempdir()) / "text_presentation_study_cache"
cache_dir.mkdir(parents=True, exist_ok=True)
matplotlib_cache_dir = cache_dir / "matplotlib"
xdg_cache_dir = cache_dir / "xdg"
matplotlib_cache_dir.mkdir(parents=True, exist_ok=True)
xdg_cache_dir.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(matplotlib_cache_dir))
os.environ.setdefault("XDG_CACHE_HOME", str(xdg_cache_dir))

print("Python version:", sys.version)
print("Testing imports...")

try:
    import pandas as pd
    print("OK: pandas imported successfully")
except ImportError as e:
    print("FAIL: pandas import failed:", e)

try:
    import matplotlib.pyplot as plt
    print("OK: matplotlib imported successfully")
except ImportError as e:
    print("FAIL: matplotlib import failed:", e)

try:
    import seaborn as sns
    print("OK: seaborn imported successfully")
except ImportError as e:
    print("FAIL: seaborn import failed:", e)

try:
    import scipy
    print("OK: scipy imported successfully")
except ImportError as e:
    print("FAIL: scipy import failed:", e)

try:
    from study_analysis import load_dataset

    data = load_dataset(Path(__file__).with_name("data_all.csv"))
    print(f"OK: CSV loaded successfully: {len(data)} rows")
    print("Groups:", data['group'].unique())
except Exception as e:
    print("FAIL: CSV loading failed:", e)

print("Test completed")
