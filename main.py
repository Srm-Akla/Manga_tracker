#!/usr/bin/python3
#
# TODO:
# - [-] Progress bar
# - [ ] Open links when clicked on name
# - [X] Save missed manga to file
# - [ ] Argparse
#Manga_tracker - Checks if new chapter is out.

try:
    from bs4 import BeautifulSoup 
    import requests
    import time
    import manga
    from rich.console import Console
    from rich.table import Table
    from rich import box
    from rich.progress import Progress
    import argparse
except ImportError:
    print("Import Error, Did you install it?")
    exit(1)

console = Console(soft_wrap=True)
table = Table(title="Manga", box=box.MINIMAL_DOUBLE_HEAD)
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"}

class Manga:
    def __init__(self, console, table, header):
        console.print("[bold yellow] Starting... [/]")
        self.console = console
        self.table = table
        self.header = header

    def get_page(self, args):
        self.page = requests.get(args, headers=self.header).text
        self.soup = BeautifulSoup(self.page, "lxml")
        self.manga_name = self.soup.title.text
        self.chapter_date = self.soup.find('div', class_='update_time').text
        try:
            self.status = self.soup.find('span', class_='new').text
        except:
            self.status=''
    
        return self.manga_name, self.chapter_date, self.status
    
    #def progress_bar(self):
    #    task1 = Progress().add_task("[red]printing", total=1000)
    #    while not Progress().finished:
    #        Progress().update(task1, advanced=0.3)
    #    print("Hello")

    def draw_table(self):
        self.table.add_column("Status", justify="center", style="bold orange_red1", no_wrap=False)
        self.table.add_column("Date", justify="center", style="magenta")
        self.table.add_column("Link", justify="left", style="green", no_wrap=False)
    
        for i in manga.mangakatana:
            self.manga_name, self.chapter_date, self.status = self.get_page(i)
            self.table.add_row(self.status, self.chapter_date, i)
    
        self.console.print(self.table)

    def write_to_file(self):
        with open('ToRead.txt', 'a') as f:
            self.current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            f.write("{}\n".format(self.current_time))
            for i in manga.mangakatana:
                self.manga_name, self.chapter_date, self.status = self.get_page(i)
                if self.status == "New":
                    f.write("{}\n".format(i))

    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--table", help="Draw table", action="store_true")
    parser.add_argument("-w", "--write", help="Write to file", action="store_true")
    args = parser.parse_args()

    if args.write:
        Manga(console, table, header).write_to_file()
    elif args.table:
        Manga(console, table, header).draw_table()
