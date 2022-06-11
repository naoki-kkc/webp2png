import glob
import re
import os

from PIL import Image

# parent_path直下の対象フォルダ
target_dirs_list = [
    "/Users/parent_dir_pathdir_1",
    "/Users/parent_dir_pathdir_2",
    "/Users/parent_dir_pathdir_3"
]

for target_dir in target_dirs_list:

    print(target_dir)

    file_list = glob.glob(os.path.join(target_dir,"*.webp"))

    cnt = 1
    for f in file_list:
        # print("[" + str(cnt) + "/" + str(len(file_list)) + "]" +f)
        filename     = os.path.split(f)[1]
        mod_filename = os.path.join(target_dir, filename.split(".")[0] + ".png")

        im = Image.open(f).convert("RGB")
        im.save(mod_filename, "png")
        cnt += 1