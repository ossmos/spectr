import asyncio

from qass.tools.analyzer.buffer_metadata_cache import BufferMetadata
from textual import work
from textual.binding import Binding
from textual.widgets import DataTable

from spectr.types import BufferMetadataProperty


class FileTable(DataTable):
    BINDINGS = [
        Binding("j", "cursor_down", "Scroll Down", show=False),
        Binding("k", "cursor_up", "Scroll Up", show=False),
        Binding("J", "page_down", "Scroll Down", show=False),
        Binding("K", "page_up", "Scroll Up", show=False),
        Binding("$", "scroll_end", "Scroll last column", show=False),
        Binding("0", "scroll_home", "Scroll first column", show=False),
        Binding("h", "cursor_left", "Scroll Left", show=False),
        Binding("l", "cursor_right", "Scroll Right", show=False),
        Binding("G", "scroll_bottom", "Scroll Bottom", show=False),
        # TODO: implement the possibility to use `gg` as in vim
        Binding("g", "scroll_top", "Scroll Top", show=False),
    ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._unloaded_table_rows = 0

    def update_border_title(self):
        border_title = f"{self.cursor_row + 1}/{self.row_count}"
        if self._unloaded_table_rows > 0:
            border_title += f" - Loading ({self._unloaded_table_rows})"
        self.border_title = border_title

    def on_data_table_row_highlighted(self, _: DataTable.RowHighlighted):
        self.update_border_title()

    @work(exclusive=True)
    async def create_rows(
        self,
        bms: list[BufferMetadata],
        columns: list[BufferMetadataProperty],
        batch_size: int,
    ) -> None:
        self.clear()
        await asyncio.sleep(0.1)
        self._unloaded_table_rows = len(bms)
        for i, bm in enumerate(bms):
            self.add_row(
                # TODO: I do not like this very much...
                *(getattr(bm, col) for col in columns),
                key=str(bm.id),
            )
            if i % batch_size == 0:
                await asyncio.sleep(0.1)
                self._unloaded_table_rows = len(bms) - i
                self.update_border_title()
        self._unloaded_table_rows = 0
        self.update_border_title()
