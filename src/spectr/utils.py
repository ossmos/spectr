import numpy as np

from .types import BinaryFileSize, DecimalFileSize


def bytes_to_human_readable_decimal(bytesize: int) -> tuple[float, DecimalFileSize]:
    """
    Convert a filesize given in bytes to a human readable size
    with the corresponding unit (Byte, Megabyte, ...)

    Parameters
    ----------
    bytesize : int
        The amount of bytes to convert to human readable format

    Returns
    -------
    tuple[float, DecimalFileSize]
        A tuple with the first element being the human readable
        amount and the second the corresponding unit
    """
    if bytesize == 0:
        return 0, DecimalFileSize.BYTE
    units = list(DecimalFileSize)
    idx = min(len(units) - 1, int(np.log10(bytesize) / 3))
    return bytesize / 10 ** (idx * 3), units[idx]


def bytes_to_human_readable_binary(bytesize: int) -> tuple[float, BinaryFileSize]:
    """
    Convert a filesize given in bytes to a human readable size
    with the corresponding unit (Byte, Megabyte, ...)

    Parameters
    ----------
    bytesize : int
        The amount of bytes to convert to human readable format

    Returns
    -------
    tuple[float, BinaryFileSize]
        A tuple with the first element being the human readable
        amount and the second the corresponding unit
    """
    if bytesize == 0:
        return 0, BinaryFileSize.BYTE
    units = list(BinaryFileSize)
    idx = min(len(units) - 1, int(np.log10(bytesize) / 3))
    return bytesize / 10 ** (idx * 3), units[idx]
