# Name: Nathan Vo
# Date: 11/15/23
# Function: Holds all the functions for the robot

import threading
import time
import json

def get_inventory():
    f = open('inventory.dat', 'r')
    data = json.load(f)
    return data

def bot_clerk(list):
    cart = []
    lock = threading.Lock()
    inv = get_inventory()

    bot_fetcher_lists = [[], [], []]
    
    for i, item in enumerate(list):
        bot_fetcher_lists[i % 3].append(item)

    threads = []
    for i, bot_fetcher_lists in enumerate(bot_fetcher_lists):
        thread = threading.Thread(target=bot_fetcher, args=(bot_fetcher_lists, cart, lock, inv))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    return cart

def bot_fetcher(i_list, c_list, lock, inv):

    for i in i_list:
        time.sleep(inv.get(i)[1])
        with lock:
            c_list.append([i, inv.get(i)[0]])