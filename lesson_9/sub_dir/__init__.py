print(">> EXECUTE __INIT__ FROM SUB_DIR")
from .sub_2_dir.some_module import get_value
from .file_3 import CONST_1, CONST_2


def main_func(a):
    return CONST_1 * CONST_2 / a

__all__ = (
    "main_func",
    # "get_value"
)

