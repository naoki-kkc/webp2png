import glob
import os
from concurrent.futures import ThreadPoolExecutor
import time
import math
import sys

def delete_files_by_regex(thread_cnt, target_dir, target_file_regex):

    start_time = time.time()

    target_files = glob.glob(target_file_regex)

    if len(target_files) == 0:
        print(f'[{thread_cnt}] skipped (no target).')    

    print('['+thread_cnt+'] ' + target_dir + ' (file_count = ' + str(len(target_files)) + ')')

    for target_file in target_files:

        os.remove(target_file)

    end_time     = time.time()
    elapsed_time = math.floor(end_time - start_time)

    print(f'[{thread_cnt}] done. file_count:{str(len(target_files))} elapsed_time:{elapsed_time}')    

def execute_parallel(parent_path):
    target_dirs = os.listdir(parent_path)

    tpe = ThreadPoolExecutor(max_workers=4)
    thread_cnt = 1
    for target_dir in target_dirs:

        if target_dir == '.DS_Store':
            # print('continue by dsstore')
            continue
        
        target_file_regex = os.path.join(parent_path, os.path.join(target_dir, '*.webp'))

        tpe.submit(delete_files_by_regex, str(thread_cnt), target_dir, target_file_regex)
        thread_cnt += 1

    tpe.shutdown()

def main():

    args = sys.argv
    if len(args) != 2:
        print('parent_path is not specified.')
        exit()
    elif not os.path.exists(args[1]):
        print('parent_path is not found')
        exit()

    parent_path = args[1]   
    execute_parallel(parent_path)
    
if __name__ == '__main__':
    main()