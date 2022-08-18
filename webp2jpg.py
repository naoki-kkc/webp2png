import glob
import os
from concurrent.futures import ThreadPoolExecutor
from pickletools import optimize
import time
import math
import shutil
import sys

from PIL import Image

def rename_files_by_regex(thread_cnt, parent_path, target_dir, target_file_regex):

    start_time = time.time()

    target_files = glob.glob(target_file_regex)

    if len(target_files) == 0:
        print(f'[{thread_cnt}] skipped (no target).')    

    print('['+thread_cnt+'] ' + target_dir + ' (file_count = ' + str(len(target_files)) + ')')

    for target_file in target_files:
    
        filename      = os.path.split(target_file)[1]
        mod_filename  = filename.split('.')[0] + '.jpg'
        mod_file_path = os.path.join(parent_path, os.path.join(target_dir, mod_filename))

        im = Image.open(target_file).convert("RGB")
        im.save(mod_file_path, "jpeg", quality=90, optimize=True) # optimize=90が画質とサイズのバランスが良さげだった(個人の主観)

        # os.remove(target_file)

    # shutil.make_archive(os.path.join(parent_path, target_dir), format='zip', root_dir=os.path.join(parent_path, target_dir))

    end_time     = time.time()
    elapsed_time = math.floor(end_time - start_time)

    print(f'[{thread_cnt}] done. file_count:{str(len(target_files))} elapsed_time:{elapsed_time}')    

def execute_parallel(parent_path):
    target_dirs = os.listdir(parent_path)

    tpe = ThreadPoolExecutor(max_workers=5)
    thread_cnt = 1
    for target_dir in target_dirs:

        if target_dir == '.DS_Store':
            # print('continue by dsstore')
            continue
        
        target_file_regex = os.path.join(parent_path, os.path.join(target_dir, '*.webp'))

        tpe.submit(rename_files_by_regex, str(thread_cnt), parent_path, target_dir, target_file_regex)
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