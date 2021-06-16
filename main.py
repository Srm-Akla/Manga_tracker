#!/usr/bin/python3
#
#Manga_tracker - Checks if new chapter is out.

from bs4 import BeautifulSoup 
import requests
import time

header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}

mangaread = [
        "https://www.mangaread.org/manga/my-death-flags-show-no-sign-of-ending/",
        "https://www.mangaread.org/manga/the-irregular-of-the-royal-academy-of-magic/",
        "https://www.mangaread.org/manga/rebuild-world",
        "https://www.mangaread.org/manga/the-beginning-after-the-end/",
        "https://www.mangaread.org/manga/the-executed-sage-is-reincarnated-as-a-lich-and-starts-an-all-out-war/",
        "https://www.mangaread.org/manga/return-of-the-frozen-player/",
        "https://www.mangaread.org/manga/the-most-notorious-talker-runs-the-worlds-greatest-clan/",
        "https://www.mangaread.org/manga/the-hero-who-has-no-class-i-dont-need-any-skills-its-okay/",
        "https://www.mangaread.org/manga/regarding-reincarnated-to-slime-manga/",
        "https://www.mangaread.org/manga/mushoku-tensei-isekai-ittara-honki-dasu-mangi/",
        "https://www.mangaread.org/manga/former-general-is-undead-knight/",
        "https://www.mangaread.org/manga/the-worlds-best-assassin-reincarnated-in-a-different-world-as-an-aristocratu",
        "https://www.mangaread.org/manga/maou-gun-saikyou-no-majutsushi-wa-ningen-datta/",
        "https://www.mangaread.org/manga/a-breakthrough-brought-by-forbidden-master-and-disciple/",
        "https://www.mangaread.org/manga/juujika-no-rokunin/",
        "https://www.mangaread.org/manga/mission-yozakura-family/",
        "https://www.mangaread.org/manga/senmetsumadou-no-saikyou-kenja-musai-no-kenja-madou-wo-kiwame-saikyou-e-itaru/",
        "https://www.mangaread.org/manga/a-stepmothers-marchen/"
    ]

mangakatana = [
        "https://mangakatana.com/manga/trash-of-the-counts-family.25137",
        "https://mangakatana.com/manga/the-beginning-after-the-end.16210",
        "https://mangakatana.com/manga/a-breakthrough-brought-by-forbidden-master-and-disciple.24731",
        "https://mangakatana.com/manga/kengan-omega.22093",
        "https://mangakatana.com/manga/the-worlds-best-assassin-reincarnated-in-a-different-world-as-an-aristocrat.22170",
        "https://mangakatana.com/manga/reincarnated-as-an-aristocrat-with-an-appraisal-skill.24873",
        "https://mangakatana.com/manga/slave-b.24525",
        "https://mangakatana.com/manga/lonely-attack-on-a-different-world.22195",
        "https://mangakatana.com/manga/lv999-no-murabito.19065",
        "https://mangakatana.com/manga/fff-class-trashero.24073",
        "https://mangakatana.com/manga/spy-x-family.22629",
        "https://mangakatana.com/manga/mercenary-enrollment.25375",
        "https://mangakatana.com/manga/sss-class-suicide-hunter.25513",
        "https://mangakatana.com/manga/kumo-desu-ga-nani-ka.18944",
        "https://mangakatana.com/manga/my-death-flags-show-no-sign-of-ending.24788",
        "https://mangakatana.com/manga/ill-be-the-matriarch-in-this-life.25771",
        "https://mangakatana.com/manga/the-irregular-of-the-royal-academy-of-magic-the-strongest-sorcerer-from-the-slums-is-unrivaled-in-the-school-of-royals.25659",
        "https://mangakatana.com/manga/the-max-level-hero-has-returned.25329",
        "https://mangakatana.com/manga/skeleton-soldier-couldnt-protect-the-dungeon.20826",
        "http://mangakatana.com/manga/the-hero-who-has-no-class-i-dont-need-any-skills-its-okay.22853",
        "http://mangakatana.com/manga/juujika-no-rokunin.25073",
        "http://mangakatana.com/manga/karakai-jouzu-no-moto-takagi-san.19332",
        "https://mangakatana.com/manga/the-eminence-in-shadow.22020",
        "https://mangakatana.com/manga/mashle.24506",
        "https://mangakatana.com/manga/a-returners-magic-should-be-special.21724",
        "https://mangakatana.com/manga/poison-dragon-the-legend-of-an-asura.25738",
        "https://mangakatana.com/manga/blue-lock.22750",
        "https://mangakatana.com/manga/memorize.25262"
    ]

other = [
        "https://www.mangaread.org/manga/the-eminence-in-shadow/"
    ]


def mangaread_func():
    for i in other:
        page = requests.get(i, headers=header).text
        soup = BeautifulSoup(page, "lxml")
        manga_name = soup.title.text
        chapter_date = soup.find('div', class_='manga-chapters-holder')
        print(manga_name, chapter_date)

def mangakatana_func():
    for i in mangakatana:
        page = requests.get(i, headers=header).text
        soup = BeautifulSoup(page, "lxml")
        manga_name = soup.title.text
        chapter_date = soup.find('div', class_='update_time').text
        try:
            status = soup.find('span', class_='new').text
        except:
            status='\033[32mNaN'
            #status=""
        print('- \033[1;31m', status, '\033[00m -- \033[33m', chapter_date, '\033[00m -- \033[4;37m', i, '\033[00m')

if __name__ == "__main__":
    #mangaread_func()
    mangakatana_func()
