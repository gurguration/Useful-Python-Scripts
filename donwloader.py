

#!/usr/bin/python3
import threading
from queue import Queue
import time
import requests
from tqdm import tqdm
import math


urls = open('links.txt').read().splitlines()


class Threader(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):

        while True:
            url_inqueue = self.queue.get()
            self.download_worker(url_inqueue)
            self.queue.task_done()
            print(f'Number of videos left to download {self.queue.qsize()}\n')




    def download_worker(self, url_inqueue):
        response = requests.get(url_inqueue[0], stream=True)
        if response.status_code == 200:
            total_filelen = int(response.headers.get('Content-Length', 0))
            block_size = 1024 * 3
            written_size = 0
            file_name = response.headers.get('X-File-Name') 
            file_written_sizename = str(url_inqueue[1]) + '__' + file_name
            print(file_name)
            with open(file_written_sizename, 'wb') as file:
                for data in tqdm(response.iter_content(block_size),
                        total=(total_filelen//block_size), unit='KB',unit_scale=True):
                    written_size += len(data)
                    file.write(data)
           
class Download:
    def __init__(self, num_ofthreads=4):
        self.num_ofthreads = num_ofthreads

    def start_download(self, urls):

        queue = Queue()
        for _ in range(self.num_ofthreads):
            t = Threader(queue)
            t.setDaemon(True)
            t.start()
        for counter, url in enumerate(urls):
            queue.put((url, counter))
        queue.join()
        return


def main():
    donwload_manager = Download()
    donwload_manager.start_download(urls)


if __name__ == '__main__':
    print('starting downloader...')
    print(f'{len(urls)} to download')
    main()
    print('all done')

