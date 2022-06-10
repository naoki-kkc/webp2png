import glob
import re
import os

from PIL import Image

parent_path = "/Users/parent_dir_path"

# parent_path直下の対象フォルダ
dirs_list = [
    "dir_1",
    "dir_2",
    "dir_3"
]

for p in dirs_list:
    target_dir_path = parent_path + p
    print(target_dir_path)

    file_list = glob.glob(os.path.join(target_dir_path,"*.webp"))

    cnt = 1
    for f in file_list:
        # print("[" + str(cnt) + "/" + str(len(file_list)) + "]" +f)
        filename     = os.path.split(f)[1]
        mod_filename = os.path.join(target_dir_path, filename.split(".")[0] + ".png")

        im = Image.open(f).convert("RGB")
        im.save(mod_filename, "png")
        cnt += 1