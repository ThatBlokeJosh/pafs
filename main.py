import os, platform, json

def readConf():
    with open("conf.JSON", "r") as f:
        data = json.load(f)["paths"]
        paths = []
        for path in range(len(data)):
            paths.append(data[path]["path"])
        paths[0] = paths[0].replace("user", os.getlogin())
        return paths

def getExt():
    with open("conf.JSON", "r") as f:
        data = json.load(f)["extensions"]

        return data

def moveFiles(paths, extensions):
    for file in os.listdir(paths[0]):
        if platform.system() == "Linux":
            if extensions[0]["extensions"].__contains__(file.split(".")[-1]):
                os.system(f"mv {paths[0]}/{file} {paths[1]}/{file}")
            elif extensions[1]["extensions"].__contains__(file.split(".")[-1]):
                os.system(f"mv {paths[0]}/{file} {paths[2]}/{file}")
            elif extensions[2]["extensions"].__contains__(file.split(".")[-1]):
                os.system(f"mv {paths[0]}/{file} {paths[3]}/{file}")
            elif extensions[3]["extensions"].__contains__(file.split(".")[-1]):
                os.system(f"mv {paths[0]}/{file} {paths[4]}/{file}")
            elif extensions[4]["extensions"].__contains__(file.split(".")[-1]):
                os.system(f"mv {paths[0]}/{file} {paths[5]}/{file}")
def main():
    paths = readConf()
    extensions = getExt()
    print(extensions)
    print(paths)
    while True:
        moveFiles(paths, extensions)

if __name__ == "__main__":
    main()