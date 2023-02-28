import os, platform

def readConf():
    if open("conf.txt", "r").readlines():
        with open("conf.txt", "r") as f:
            downloadPath = f.readline()
            imagePath = f.readline()
            documentPath = f.readline()
            videoPath = f.readline()
            musicPath = f.readline()
            f.close()
        paths = [downloadPath, imagePath, documentPath, videoPath, musicPath]
        for path in paths:
            paths[paths.index(path)] = path.strip("\n")
            return paths

    else:
        with open("conf.txt", "w") as f:
            # Please enter the whole path
            downloadPath = input("Enter the whole download path: ")
            f.write(f"{downloadPath}\n")
            # Now you can enter a path like ~/Pictures
            imagePath = input("Enter the image path: ")
            f.write(f"{imagePath}\n")
            documentPath = input("Enter the document path: ")
            f.write(f"{documentPath}\n")
            videoPath = input("Enter the video path: ")
            f.write(f"{videoPath}\n")
            musicPath = input("Enter the music path: ")
            f.write(f"{musicPath}\n")
            f.close()
            print("Done!")


def moveFiles(paths):
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
        elif platform.system() == "Windows":
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
    print(platform.system())
    while True:
        moveFiles(paths)

if __name__ == "__main__":
    main()