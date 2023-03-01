


import os

foo = '\\'
print("Enter directory:")
my_dir = str(input())
my_dir = my_dir.replace(foo, foo*2)

def parse(filename:str):
    if filename.count(".") == 0:
        for fname in os.listdir(str(filename)):
            parse(str(filename) + str(foo) + str(foo) + fname)
    else:
        if "thumb" in filename:
            os.remove(os.path.join(my_dir, filename))
        else:
            if "sticker" in filename:
                os.remove(os.path.join(my_dir, filename))



parse(my_dir)

"""
foo = '\\'
import os
print("Enter directory:")
my_dir = str(input())
my_dir = my_dir.replace(foo, foo*2)
for fname in os.listdir(str(my_dir) + str(foo) + (str(foo) + str("photos"))):
    if "thumb" in fname:
        print(fname)
        newdir = str(my_dir) + str(foo) + str(foo) + str("photos")
        os.remove(os.path.join(newdir, fname))
for fname in os.listdir(str(my_dir) + str(foo) + (str(foo) + str("round_video_messages"))):
    if "thumb" in fname:
        print(fname)
        newdir = str(my_dir) + str(foo) + str(foo) + str("round_video_messages")
        os.remove(os.path.join(newdir, fname))
for fname in os.listdir(str(my_dir) + str(foo) + (str(foo) + str("video_files"))):
    if "sticker" in fname:
        print(fname)
        newdir = str(my_dir) + str(foo) + str(foo) + str("video_files")
        os.remove(os.path.join(newdir, fname))

"""