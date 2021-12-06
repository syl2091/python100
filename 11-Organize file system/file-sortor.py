import os
import shutil

# 整理文件系统
os.chdir(r"D:\Installed")

files = os.listdir()

extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]
}


# 文件分类
def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            # print(ext)
            if file.endswith(ext):
                return key


for file in files:
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, "../download-sorting/" + dist)
        except:
            print(file + " is already exist")
    else:
        try:
            shutil.move(file, "../download-sorting/others")
        except:
            print(file + " is already exist")
