import sys

def sort (**kwargs):
    """
    SORT                         User Commands                        SORT
    NAME
        sort - sorts files
    SYNOPSIS
        sort [FILE]
    DESCRIPTION
        sort sorts FILEs by the given option. Default is alphebetically with blank
        lines followed by capital letters, then lowercase below them.

    EXAMPLE
        sort file.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']
    if 'tags' in kwargs:
        tags = kwargs['tags']

    try:
        fileOpen = open(path[0]+params[0])
        preCapSortList = []
        preLowSortList = []
        finalSort = []
        for line in fileOpen:
            tempCharList = list(line)
            ifEmptyLine = line.strip()
            if len(ifEmptyLine)==0:
                finalSort.append('\n')
            elif tempCharList[0].isupper():
                preCapSortList.append(line)
            else:
                preLowSortList.append(line)

        preCapSortList.sort()
        preLowSortList.sort()
        for item in preCapSortList:
            finalSort.append(item)
        for item in preLowSortList:
            finalSort.append(item)
        return finalSort
    except:
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    sortReturn = sort(params=['bacon.txt'], path=['./'])
    for line in sortReturn:
        sys.stdout.write(line)
    pass
