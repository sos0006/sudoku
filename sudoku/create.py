def _create(parms):
    #result = {'status': 'create stub'}
    if (not ("level" in parms)):
        result = {'status': 'create stub'}
    else:
        result = parms["level"]      
        
        if (result == '1'):
            levelReturn = "This is level one"
        elif (result == '2'):
            levelReturn = "This is level two"
        elif (result == '3' or result == ""):
            levelReturn = "This is level three"
        elif (result == '4'):
            levelReturn = "This is level four"
        elif (result == '5'):
            levelReturn = "This is level five"
        else:
            levelReturn = "{'status':'error: invalid level'}"


        
    return levelReturn
