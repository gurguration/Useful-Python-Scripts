
from threading import Thread
from queue import Queue
import time
import requests

urls = ['https://google.com', 'https://google.com',
        'https://google.com', 'https://google.com',
        'https://google.com', 'https://google.com']


class Threader(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):

        while True:
            url_inqueue = self.queue.get()
            self.download_worker(url_inqueue)
            self.queue.task_done()

    def download_worker(self, url_inqueue):
        start = time.time()
        response = requests.get(url_inqueue)
        end = time.time()
        if response.status_code == 200:
            time_taken = start - end
            print('it took {} time to server your request'.format(time_taken))
            print(response.content)


class Download:
    def __init__(self, num_ofthreads=3):
        self.num_ofthreads = num_ofthreads

    def start_download(self, urls):

        queue = Queue()
        for _ in range(self.num_ofthreads):
            t = Threader(queue)
            t.setDaemon(True)
            t.start()
        for url in urls:
            queue.put(url)
        queue.join()
        return


def main():
    donwload_manager = Download()
    donwload_manager.start_download(urls)


if __name__ == '__main__':
    main()
