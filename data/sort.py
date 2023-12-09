import os, shutil
from pathlib import Path


print(os.getcwd())

#Copy files
def copy():
    src = Path("./raw_cards").absolute()
    dst = Path("./cards").absolute()
    shutil.copytree(src, dst)

#Rename images
def renimg(img_path, type):
    wd = os.getcwd()
    os.chdir(img_path)
    Path(type).mkdir(exist_ok=True)
    num = 0
    for dir in os.listdir():
        dir_name = dir.split(" ")
        if len(dir_name) > 1 and dir_name[2] == type:
            for file in os.listdir(dir):
                new_name = f"{type}_{num}.jpg"
                num += 1
                src = os.path.join(img_path, dir, file)
                dst = os.path.join(img_path, type, new_name)
                shutil.copy(src, dst)
            shutil.rmtree(dir)
    os.chdir(wd)
        

def main():
    copy()
    img_path = Path("./cards/test/").absolute()
    for type in ["clubs", "diamonds", "hearts", "spades"]:
        renimg(img_path, type)
    img_path = Path("./cards/train/").absolute()
    for type in ["clubs", "diamonds", "hearts", "spades"]:
        renimg(img_path, type)
    img_path = Path("./cards/valid/").absolute()
    for type in ["clubs", "diamonds", "hearts", "spades"]:
        renimg(img_path, type)

main()