# import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import time
import random


def study(fname, lname):
  for i in range(10):
    print(f'{fname} {lname} is studying {i}...')
    time.sleep(random.random())
  
def listen_to_music(fname, lname):
  for i in range(10):
    print(f'{fname} {lname} is listening to music {i}...')
    time.sleep(random.random())

if __name__ == '__main__':
  args = [["A", "C"], ["B", "D"]]
  
  with ThreadPoolExecutor(max_workers=2) as executor:
    # Usage 1: 2 threads, 2 tasks, 1 'person'
    # executor.submit(study, *args)
    # executor.submit(listen_to_music, "A", "B")
    
    # Usage 2: 2 threads, 1 task, 2 'people'
    executor.map(study, *args)
