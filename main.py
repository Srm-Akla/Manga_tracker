#!/usr/bin/python3
#
#Manga_tracker - Checks if new chapter is out.

from bs4 import BeautifulSoup 
import requests
import time
from rich.console import Console
from rich.table import Table
from rich import box

console = Console(soft_wrap=True)
table = Table(title="Manga", box=box.MINIMAL_DOUBLE_HEAD)

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"}

mangakatana = [
        "https://mangakatana.com/manga/legend-of-the-northern-blade.24729",
        "https://mangakatana.com/manga/duke-pendragon.26081",
        "https://mangakatana.com/manga/arcane-sniper.25672",
        "https://mangakatana.com/manga/the-world-after-the-fall.26154",
        "https://mangakatana.com/manga/a-stepmothers-fairy-tale.23902",
        "https://mangakatana.com/manga/the-executed-sage-is-reincarnated-as-a-lich-and-starts-an-all-out-war.24836",
        "https://mangakatana.com/manga/ryuu-kusari-no-ori-kokoro-no-uchi-no-kokoro.25821",
        "https://mangakatana.com/manga/saikyou-yuusha-wa-oharai-hako-maou-ni-nattara-zutto-ore-no-musou-return.22825",
        "https://mangakatana.com/manga/murim-login.24856",
        "https://mangakatana.com/manga/im-really-not-the-evil-gods-lackey.25952",
        "https://mangakatana.com/manga/send-my-regards-to-kenshiro.24571",
        "https://mangakatana.com/manga/seoul-station-druid.25869",
        "https://mangakatana.com/manga/survival-story-of-a-sword-king-in-a-fantasy-world.24146",
        "https://mangakatana.com/manga/leveling-with-the-gods.25898",
        "https://mangakatana.com/manga/real-man.25641",
        "https://mangakatana.com/manga/mushoku-tensei-isekai-ittara-honki-dasu.145",
        "https://mangakatana.com/manga/heroic-chronicles-of-the-three-continents.25442",
        "https://mangakatana.com/manga/mathematics-golden.25754",
        "https://mangakatana.com/manga/the-beginning-after-the-end.16210",
        "https://mangakatana.com/manga/a-breakthrough-brought-by-forbidden-master-and-disciple.24731",
        "https://mangakatana.com/manga/kengan-omega.22093",
        "https://mangakatana.com/manga/the-worlds-best-assassin-reincarnated-in-a-different-world-as-an-aristocrat.22170",
        "https://mangakatana.com/manga/the-most-notorious-talker-runs-the-worlds-greatest-clan.24837",
        "https://mangakatana.com/manga/tensei-shitara-slime-datta-ken.1780",
        "https://mangakatana.com/manga/reincarnated-as-an-aristocrat-with-an-appraisal-skill.24873",
        "https://mangakatana.com/manga/hero-has-returned.25839",
        "https://mangakatana.com/manga/fff-class-trashero.24073",
        "https://mangakatana.com/manga/spy-x-family.22629",
        "https://mangakatana.com/manga/mercenary-enrollment.25375",
        "https://mangakatana.com/manga/sss-class-suicide-hunter.25513",
        "https://mangakatana.com/manga/kumo-desu-ga-nani-ka.18944",
        "https://mangakatana.com/manga/my-death-flags-show-no-sign-of-ending.24788",
        "https://mangakatana.com/manga/ill-be-the-matriarch-in-this-life.25771",
        "https://mangakatana.com/manga/the-irregular-of-the-royal-academy-of-magic-the-strongest-sorcerer-from-the-slums-is-unrivaled-in-the-school-of-royals.25659",
        "https://mangakatana.com/manga/skeleton-soldier-couldnt-protect-the-dungeon.20826",
        "https://mangakatana.com/manga/the-hero-who-has-no-class-i-dont-need-any-skills-its-okay.22853",
        "https://mangakatana.com/manga/baki-dou-2018.21422",
        "https://mangakatana.com/manga/hell-mode-yarikomi-suki-no-gamer-wa-hai-settei-no-isekai-de-musou-suru.25325",
        "https://mangakatana.com/manga/tokyo-babel.25284",
        "https://mangakatana.com/manga/her-majestys-swarm.25067",
        "https://mangakatana.com/manga/tenkaichi-nihon-saikyou-bugeisha-ketteisen.26075",
        "https://mangakatana.com/manga/record-of-ragnarok.22096",
        "https://mangakatana.com/manga/the-tutorial-is-too-hard.25633",
        "https://mangakatana.com/manga/juujika-no-rokunin.25073",
        "https://mangakatana.com/manga/karakai-jouzu-no-moto-takagi-san.19332",
        "https://mangakatana.com/manga/reformation-of-the-deadbeat-noble.25854",
        "https://mangakatana.com/manga/the-eminence-in-shadow.22020",
        "https://mangakatana.com/manga/mashle.24506",
        "https://mangakatana.com/manga/a-returners-magic-should-be-special.21724",
        "https://mangakatana.com/manga/poison-dragon-the-legend-of-an-asura.25738",
        "https://mangakatana.com/manga/blue-lock.22750",
    ]

def mangakatana_func():

    table.add_column("Status", justify="center", style="bold orange_red1", no_wrap=False)
    table.add_column("Date", justify="center", style="magenta")
    table.add_column("Link", justify="left", style="green", no_wrap=False)

    for i in mangakatana:
        page = requests.get(i, headers=header).text
        soup = BeautifulSoup(page, "lxml")
        manga_name = soup.title.text
        chapter_date = soup.find('div', class_='update_time').text
        try:
            status = soup.find('span', class_='new').text
        except:
            status='[dark_cyan]NaN[/]'
            #status=""
        #console.print(f" [bold orange_red1]{status}[/] -- [bold magenta]{chapter_date}[/] -- [yellow]{i}[/]")
        table.add_row(status, chapter_date, i)

    console.print(table)

if __name__ == "__main__":
    #mangaread_func()
    mangakatana_func()
