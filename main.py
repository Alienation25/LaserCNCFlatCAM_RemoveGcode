
import os
from os import path


def chengWord(filename: str, wordsearch: str, wordcheng: str):
    try:
        filetochend = open(filename, 'r', encoding="UTF-8")
    except IOError as identifier:
        print("Error", identifier)
        filetochend.close()
        exit
    else:
        text = filetochend.read()
        filetochend.close()
        filetochend = open(filename, 'w', encoding="UTF-8")
        filetochend.write(text.replace(wordsearch, wordcheng))
        filetochend.close()


def readFileAndCreateFile(filename: str, nameNewFile: str):
    try:
        filetochend = open(filename, 'r', encoding="UTF-8")
    except IOError as identifier:
        print("Error", identifier)
        filetochend.close()
        exit
    else:
        text = filetochend.read()
        filetochend.close()
        filetochend = open(nameNewFile, 'w', encoding="UTF-8")
        filetochend.write(text)
        filetochend.close()
        return nameNewFile


def deleteSpace(namefile: str):
    string = open(namefile).readlines()
    ints = []
    for i in string:
        if not i.isspace():
            ints.append(i.replace('\n', ''))
    filetochend = open(namefile, 'w', encoding="UTF-8")
    for a in ints:
        filetochend.writelines(a+'\n')
    filetochend.close()


def main():
    namefiletocheng: str = input()
    if namefiletocheng == "":
        namefiletocheng = "laser.gcode"

    namefile = readFileAndCreateFile(
        namefiletocheng, "laser_good_to_print.gcode")
    chengWord(namefile, "M03", "")
    chengWord(namefile, "M05", "")
    chengWord(namefile, "Y", " Y")
    chengWord(namefile, "F3.00", "G92 X0 Y0 Z0\nG1 F200.0")
    chengWord(namefile, "G00 Z3.0000", "G4 P0\nM42 P57 S0\nG4 P5")
    chengWord(namefile, "G01 Z-2.0000", "G4 P0\nM42 P57 S255\nG4 P5")
    deleteSpace(namefile)


if __name__ == '__main__':
    main()
