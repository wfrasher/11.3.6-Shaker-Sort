

def shakerSort(thelist):
    length = len(thelist)
                                               
    for passes in range(0, length):
        for i in range(0, length-1):
            if thelist[i] > thelist[i+1]:
                thelist[i],thelist[i+1] = thelist[i+1],thelist[i]
            ###                                                            ### OTHER WAY
        for y in range(length -1, 0, -1): 
               if thelist[y-1] > thelist[y]:
                thelist[y],thelist[y-1] = thelist[y-1],thelist[y]
       
    return thelist


inputFile = open('finalData01.txt', 'r')
data = inputFile.read()
inputFile.close()


list = data.split( '\n')
newFile = open('shakednums.txt', 'w')
finallist = shakerSort(list)

for num in finallist:
    newFile.writelines(num + '\n')

newFile.close()