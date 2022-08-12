import os
from pickletools import optimize
import shutil
import sys

from PIL import Image

def main():

    args = sys.argv
    if len(args) != 2:
        print('parent_path is not specified.')
        exit()
    elif not os.path.exists(args[1]):
        print('parent_path is not found')
        exit()

    parent_path = args[1]
    target_dirs = os.listdir(parent_path)    

    for target_dir in target_dirs:

        if target_dir == '.DS_Store':
            # print('continue by dsstore')
            continue
        
        shutil.make_archive(os.path.join(parent_path, target_dir), format='zip', root_dir=os.path.join(parent_path, target_dir))

if __name__ == '__main__':
    main()