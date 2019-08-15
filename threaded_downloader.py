#!/usr/bin/python3
from threading import Thread
from queue import Queue
import time
import requests
from tqdm import tqdm
import math


urls = open('links.txt').read().splitlines()


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
        response = requests.get(url_inqueue, stream=True)
        if response.status_code == 200:
            total_filelen = int(response.headers.get('Content-Length', 0))
            block_size = 1024 * 3
            written_size = 0
            file_name = response.headers.get('X-File-Name')
            print(file_name)
            with open(file_name, 'wb') as file:
                for data in tqdm(response.iter_content(block_size),
                        total=(total_filelen//block_size), unit='KB',unit_scale=True):
                    written_size += len(data)
                    file.write(data)
           
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
