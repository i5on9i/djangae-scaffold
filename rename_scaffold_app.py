# coding=utf-8

# Import the os module, for the os.walk function
import os
import sys


POSTFIX = '.bak'


def removeAllPys(dirName, fileList):
    for fname in fileList:
        os.remove(os.path.join(dirName, fname))


def renameBak2Py(dirName, fileList):
    for fname in fileList:
        os.rename(os.path.join(dirName, fname + POSTFIX),
                  os.path.join(dirName, fname))


def main(argv):

    projName = argv[1]

    defaultName = 'scaffold'
    # Set the directory you want to start from
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if dirName == os.path.join(rootDir, defaultName):
            for fname in fileList:
                print('\t%s' % fname)
                with open(os.path.join(dirName, fname), 'r') as f:
                    with open(os.path.join(dirName, fname + POSTFIX), 'w') as wf:
                        for l in f:
                            wf.write(l.replace(defaultName, projName))

            removeAllPys(dirName, fileList)
            renameBak2Py(dirName, fileList)
            os.rename(os.path.join(rootDir, defaultName),
                      os.path.join(rootDir, projName))
            break


if __name__ == '__main__':
    main(sys.argv)
