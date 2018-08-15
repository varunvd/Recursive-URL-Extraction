import constants
from Queue_Class import Queue
from bs4 import BeautifulSoup
import requests
import multiprocessing

q = Queue()
file = open('output.txt', 'a')
counter = 0


def extract_all_urls():
    global counter
    if counter >= constants.LIMIT:
        return
    url = q.dequeue()
    try:
        html = requests.get(url).content
    except:
        return
    soup = BeautifulSoup(html,features="html.parser")
    for a in soup.find_all('a', href=True):
        try:
            if 'http' in a['href']:
                if counter == constants.LIMIT:
                    file.close()
                q.enqueue(a['href'])
                file.write(a['href']+"\n")
                counter = counter+1
        except:
            continue

    if q.size() != 0:
        extract_all_urls()


if __name__ == '__main__':
    q.enqueue(constants.URL)

    jobs = []

    for thread_live in range(constants.NUMBER_OF_THREADS):
        thread_live = multiprocessing.Process(target=extract_all_urls())
        jobs.append(thread_live)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    file.close()


