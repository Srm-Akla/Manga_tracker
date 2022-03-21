from time import sleep

from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

sometuple = (1,2,3,4,5,"jfjf",7,8,9)

n = len(sometuple)

text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
progress = Progress(text_column, bar_column, expand=True)

with progress:
    for n in progress.track(sometuple):
        sleep(0.1)

