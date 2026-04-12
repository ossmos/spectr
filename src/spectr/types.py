from enum import StrEnum
from typing import Literal


class DecimalFileSize(StrEnum):
    BYTE = "B"
    KILO_BYTE = "KB"
    MEGA_BYTE = "MB"
    GIGA_BYTE = "GB"
    TERA_BYTE = "TB"
    PETA_BYTE = "PB"


class BinaryFileSize(StrEnum):
    BYTE = "B"
    KIBI_BYTE = "K"
    MEBI_BYTE = "M"
    GIBI_BYTE = "G"
    TEBI_BYTE = "T"
    PEBI_BYTE = "P"


BufferMetadataProperty = Literal[
    "id",
    "project_id",
    "directory_path",
    "filename",
    "header_size",
    "process",
    "channel",
    "datamode",
    "datakind",
    "datatype",
    "process_time",
    "process_date_time",
    "db_header_size",
    "bytes_per_sample",
    "db_count",
    "full_blocks",
    "db_size",
    "db_sample_count",
    "frq_bands",
    "db_spec_count",
    "compression_frq",
    "compression_time",
    "avg_time",
    "avg_frq",
    "spec_duration",
    "frq_start",
    "frq_end",
    "frq_per_band",
    "sample_count",
    "spec_count",
    "adc_type",
    "bit_resolution",
    "fft_log_shift",
    "streamno",
    "preamp_gain",
    "analyzer_version",
    "partnumber",
    "header_hash",
]

PlotextPlotMarker = Literal["braille", "fhd", "hd", "dot"]
DownsamplingAlgorithm = Literal["lttb", "max_bucket"]
FileSizeUnit = Literal["decimal", "binary"]
