import os
import shutil

path = None


def main():
    global path
    print( 'streamline directories' )
    print( 'input: ' )
    inpDir = input()
    path = inpDir

    searchForDirectories()
    pass


def searchForDirectories():
    global path
    arr = os.listdir( path )

    for x in arr:
        newPath = path + '\\' + x.split('-')[2]

        outputOld = path + '\\' + x
        print(outputOld)
        print(newPath)
        shutil.move(outputOld, newPath)


if (__name__ == '__main__'):
    main()