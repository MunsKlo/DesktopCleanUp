import glob
from shutil import move

path = "C:/Users/Christopher/Desktop/"
pic_path = "F:/BIlder/Bilder/"
docs_path = "F:/PDF-Dokumente/"


def CopyFiles(file_type, file_path):

    list_of_jpg = glob.glob(path + "*." + file_type)
    for item in list_of_jpg:
        new_path = file_path + GetNameOfFile(item)
        move(item, new_path)


def GetNameOfFile(path_of_file):
    length = len(path_of_file)
    j = length - 1
    newString = ""
    while range(length):
        if(path_of_file[j] != "\\"):
            newString += path_of_file[j]
            j -= 1
        else:
            break
    return "".join(reversed(newString))


CopyFiles("jpg", pic_path)
CopyFiles("jpeg", pic_path)
CopyFiles("png", pic_path)
CopyFiles("webp", pic_path)
CopyFiles("pdf", docs_path)
CopyFiles("docx", "F:/WPS Dokumente/Word/")
CopyFiles("exe", "F:/Programme/Verknüpfungen/")
CopyFiles("txt", "F:/Textdokumente/")
CopyFiles("mp4", "F:/Videos/")
CopyFiles("mkv", "F:/Videos/")
CopyFiles("mp3", "F:/Musik/")
CopyFiles("lnk", "F:/Programme/Verknüpfungen/")
CopyFiles("7z", "F:/Archive/")
#list_of_file = glob.glob(path + "*")
#print(list_of_file)