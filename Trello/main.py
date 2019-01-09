import requests
import os
import json
import sys


def main(args):

    my_board = 'Newsela'  # Change this to your board name

    name = args[0]
    key = os.environ.get('TRELLO_API_KEY')
    token = os.environ.get('TRELLO_API_TOKEN')
    BASE_URL = "https://api.trello.com/1/"

    boards_url = f"{BASE_URL}members/me/boards?key={key}&token={token}"
    resp = requests.get(boards_url)

    boards = json.loads(resp.content)
    board_id = [b['id'] for b in boards if b['name'] == my_board]

    create_list_url = f"{BASE_URL}lists?name={name}&idBoard={board_id[0]}&key={key}&token={token}"
    resp = requests.post(create_list_url)

    lists_url = f"{BASE_URL}boards/{board_id[0]}/lists?key={key}&token={token}"
    resp = requests.get(lists_url)

    lists = json.loads(resp.content)
    list_id = [list['id'] for list in lists if list['name'] == name]
    pos_url = f"{BASE_URL}lists/{list_id[0]}/pos?value=top&key={key}&token={token}"
    resp = requests.put(pos_url)
    print(resp.content)


if (__name__ == '__main__'):
    if len(sys.argv) != 2:
        raise Exception("Example format: python3 main.py <ListName>")
    else:
        main(sys.argv[1:])
