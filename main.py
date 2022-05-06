#!/usr/bin/python3
#
#Manga_tracker - Checks if new chapter is out.

try:
    from bs4 import BeautifulSoup 
    import requests
    import time
    from rich.console import Console
    from rich.table import Table
    from rich import box
    from rich.progress import Progress
except ImportError:
    print("Import Error, Did you install it?")
    exit(1)

console = Console(soft_wrap=True)
table = Table(title="Manga", box=box.MINIMAL_DOUBLE_HEAD)
global manga_name, chapter_date, status

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"}

mangakatana = (
        "https://mangakatana.com/manga/legend-of-the-northern-blade.24729",
)

class Manga:
    def __init__(self):
        self.text = "Hello world"
        print(self.text)

    def get_page(self, args):
        self.page = requests.get(self.args, headers=header).text
        self.soup = BeautifulSoup(self.page, "lxml")
        self.manga_name = self.soup.title.text
        self.chapter_date = self.soup.find('div', class_='update_time').text
        try:
            self.status = self.soup.find('span', class_='new').text
        except:
            self.status='[dark_cyan]NaN[/]'
    
        #return self.manga_name, self.chapter_date, self.status
        console.print("{} -- {} -- {}".format(self.manga_name, self.args, self.status))
    
    #def draw_table(self):
    #    table.add_column("Status", justify="center", style="bold orange_red1", no_wrap=False)
    #    table.add_column("Date", justify="center", style="magenta")
    #    table.add_column("Link", justify="left", style="green", no_wrap=False)
    #
    #    for i in mangakatana:
    #        manga_name, chapter_date, status = get_page(i)
    #        #console.print(f" [bold orange_red1]{status}[/] -- [bold magenta]{chapter_date}[/] -- [yellow]{i}[/]")
    #        table.add_row(status, chapter_date, manga_name)
    #
    #    console.print(table)
    #
    #def progress_bar(self):
    #    task1 = Progress().add_task("[red]printing", total=1000)
    #    while not Progress().finished:
    #        Progress().update(task1, advanced=0.3)
    #    print("Hello")

if __name__ == "__main__":
    Manga().get_page()
