import hashlib

def _create(parms):
    
    
    gridDict = {'1' : [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                '2' : [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8],
                '3' : [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0],
                '4' : [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0],
                '5' : [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
                }
    
    integrityDict = {}
    dictList = [None] * 81
    for key in gridDict:
        stringHash = ""
        
        counter = 0
        for index in gridDict[key]:
            if (counter == 0 or counter == 80):
                dictList[counter] = index
            else:
                dictList[(counter * 9) % 80] = index
            counter = counter + 1
        

            
        for index in range(len(dictList)):
            stringHash = stringHash + str(dictList[index])
    
        #integrityDict[key] = stringHash
        integrityDict[key] = hashlib.sha256(stringHash.encode('utf-8')).hexdigest()


    #result = {'status': 'create stub'}
    if (not ("level" in parms)):
        result = {'status': 'create stub'}
    else:
        result = parms["level"]      
        
        if (result == '1'):
            levelReturn = "This is level one"
            print(integrityDict['1'])
        elif (result == '2'):
            levelReturn = "This is level two"
        elif (result == '3' or result == ""):
            levelReturn = "This is level three"
        elif (result == '4'):
            levelReturn = "This is level four"
        elif (result == '5'):
            levelReturn = "This is level five"
        else:
            return {'status':'error: invalid level'}


        
    return levelReturn