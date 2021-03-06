import requests
import logging
from lxml import etree, html

league_id = "293889"
season_length = 12

total = {}

for week in range(season_length):
    page = requests.get("http://games.espn.com/ffl/scoreboard?leagueId="+league_id+"&matchupPeriodId="+str(week+1))
    tree = html.fromstring(page.content)
    abbr = tree.xpath("//span[@class='abbrev']/text()")
    score = tree.xpath("//td[contains(@class, 'score')]/text()")

    week_array = []
    for i in range(len(abbr)):
        team = [abbr[i], float(score[i])]
        week_array.append(team)
    week_array.sort(key=lambda tup: tup[1])

    for i in range(len(week_array)):
        if not week_array[i][0] in total:
            total[week_array[i][0]] = 0
        total[week_array[i][0]] += i

sorted_total = sorted(total, key=total.get, reverse=True)

for key in sorted_total:
    print "Team: {0} Wins: {1}".format(key, total[key])