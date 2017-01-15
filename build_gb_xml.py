import requests
import sqlite3

api_key = '5c87b9da32a2c634c32aff7f191f27e8e1068e05'


def pull_page(page_number, page_size):
    platforms = 84
    field_list = 'id,name,aliases,original_release_date'
    offset = page_number * page_size
    print "Pulling games from {} to {}".format(offset, offset + page_size)
    url = 'http://www.giantbomb.com/api/games/?format=json&limit={}&offset={}&field_list={}&platforms={}&api_key={}'.format(page_size, offset, field_list, platforms, api_key)
    # print url
    response = requests.get(url)

    games = {'results': []}
    if response.status_code == 200:
        games = response.json()
    return games.get('results')


total_results = 1951
page_size = 100
pages = (total_results / page_size) + 1

games = []
for page in range(0, pages):
    games += pull_page(page, page_size)

print 'Found {} games.'.format(len(games))
# import ipdb; ipdb.set_trace()

# game = {'original_release_date': '1999-03-18 00:00:00', 'id': 18, 'name': 'Metal Slug X: Super Vehicle - 001', 'aliases': None}
# games = [game]

conn = sqlite3.connect('games_db.sqlite')
with conn:
    for game in games:
        aliases = game.get('aliases') if game.get('aliases') is not None else ''
        conn.execute("insert into games (gb_id, release_date, name, aliases) values(?, ?, ?, ?)",
                     (game.get('id'), game.get('original_release_date'), game.get('name'), aliases))
