import sys, os
# Add the project root directory to Python’s module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add

def test_add():
    """Test the add function."""
    assert add(2, 3) == 6
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
