import numpy as np

from .types import FileSizeUnit


def bytes_to_human_readable(bytesize: int) -> tuple[float, FileSizeUnit]:
    """
    Convert a filesize given in bytes to a human readable size
    with the corresponding unit (Byte, Megabyte, ...)

    Parameters
    ----------
    bytesize : int
        The amount of bytes to convert to human readable format

    Returns
    -------
    tuple[float, FileSizeUnit]
        A tuple with the first element being the human readable
        amount and the second the corresponding unit
    """
    if bytesize == 0:
        return 0, FileSizeUnit.BYTE
    units = list(FileSizeUnit)
    idx = min(len(units) - 1, int(np.log10(bytesize) / 3))
    return bytesize / 10 ** (idx * 3), units[idx]
