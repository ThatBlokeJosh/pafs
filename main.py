import os, platform, json

def readConf():
    with open("conf.JSON", "r") as f:
        data = json.load(f)["paths"]
        paths = []
        for path in range(len(data)):
            paths.append(data[path]["path"])
        paths[0] = paths[0].replace("user", os.getlogin())
        return paths

def moveFiles(paths, extensions=[".jpg", ".png", ".jpeg", ".pdf", ".docx", ".txt", ".mp4", ".mkv", ".avi", ".mp3", ".wav", ".flac"]):
    for file in os.listdir(paths[0]):
        if platform.system() == "Linux":
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                os.system(f"mv {paths[0]}/{file} {paths[1]}/{file}")
            elif file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".txt"):
                os.system(f"mv {paths[0]}/{file} {paths[2]}/{file}")
            elif file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".avi"):
                os.system(f"mv {paths[0]}/{file} {paths[3]}/{file}")
            elif file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
                os.system(f"mv {paths[0]}/{file} {paths[4]}/{file}")
            else:
                print("No files to move")
        else:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                os.system(f"move {paths[0]}/{file} {paths[1]}/{file}")
            elif file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".txt"):
                os.system(f"move {paths[0]}/{file} {paths[2]}/{file}")
            elif file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".avi"):
                os.system(f"move {paths[0]}/{file} {paths[3]}/{file}")
            elif file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
                os.system(f"move {paths[0]}/{file} {paths[4]}/{file}")
            else:
                print("No files to move")

def main():
    paths = readConf()
    print(paths)
    while True:
        moveFiles(paths)

if __name__ == "__main__":
    main()