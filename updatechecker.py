import requests
import updater

version = open("version.txt", 'r')
versionnum = version.read().split('\n')[0]

print("Current version is: " + versionnum)

splitversion = versionnum.split('.')
versionnum = splitversion[0] + "." + splitversion[1] + "." + str(int(splitversion[2]) + 1)


url = "https://www.factorio.com/get-download/" + versionnum + "/headless/linux64"

r = requests.head(url)
if r.status_code == 302:
    print("Update found! \n Starting update..")
    updater.updateFactorio(versionnum)
