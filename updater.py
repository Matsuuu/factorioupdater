import wget
import tarfile
import os
import shutil

def updateFactorio(versionnum):

    url = "https://www.factorio.com/get-download/"+versionnum+"/headless/linux64"

    cwd = os.getcwd()
    print("Starting download of version " + versionnum + " from url " + url)
    filename = wget.download(url)

    if filename:
        if os.path.isdir(cwd + "/factorio_old"):
            shutil.rmtree(cwd + "/factorio_old")

        if os.path.isdir(cwd + "/factorio"):
            os.rename(cwd + "/factorio", cwd + "/factorio_old")

        print("Unpacking files to " + cwd + "/factorio")
        tar = tarfile.open(filename)
        tar.extractall()
        tar.close()

        os.remove(cwd + "/" + filename)

        print("Updating version.txt to " + versionnum)

        version = open("version.txt", "w")
        version.write(versionnum)