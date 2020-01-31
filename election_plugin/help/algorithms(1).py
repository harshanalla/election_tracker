from operator import itemgetter
import random

class algorithms:


    def __init__(self):
        self.data=0
    #starts with the highest number of pop polygon and adds down
    def TopDown(self,dictlist,thresh,export=False):
        sortlist = sorted(dictlist, key=itemgetter('pop_weight'))
        count=0
        PolyWinCount=0
        result = False
        for i in range(len(sortlist)):
            currentDict = sortlist[len(sortlist)-(i+1)]
            if(currentDict['elec_result'] == 1):
                count += currentDict['pop_weight']
                PolyWinCount += 1
            elif(currentDict['elec_result'] == -1):
                if(count<thresh):
                    count += currentDict['pop_weight']
                    PolyWinCount += 1
                    currentDict['elec_result'] = 1
                else:
                    currentDict['elec_result'] = 0
        if(count>thresh):
            result = True
        if(export==True):
            ExportTxt(result,PolyWinCount,sortlist)
        return result, PolyWinCount, sortlist


    #goes through each dictionary and rolls a 50/50 dice
    def BottomUp(self,dictlist,thresh,export=False):
        sortlist = sorted(dictlist, key=itemgetter('pop_weight'))
        count=0
        PolyWinCount=0
        result = False
        for i in range(len(sortlist)):
            currentDict = sortlist[i]
            if(currentDict['elec_result'] == 1):
                count += currentDict['pop_weight']
                PolyWinCount += 1
            elif(currentDict['elec_result'] == -1):
                if(count<thresh):
                    count += currentDict['pop_weight']
                    PolyWinCount += 1
                    currentDict['elec_result'] = 1
                else:
                    currentDict['elec_result'] = 0
        if(count>thresh):
            result = True
        if(export==True):
            ExportTxt(result,PolyWinCount,sortlist)
        return result, PolyWinCount, sortlist

    #Decides randomly whether every polygon is won or lost
    def RandomElection(self,dictlist,thresh,export=False):
        count=0
        PolyWinCount=0
        result = False
        winlose = [0,1]
        for i in range(len(dictlist)):
            randChoice = random.choice(winlose)
            currentDict = dictlist[i]
            if(currentDict['elec_result'] == 1):
                count += currentDict['pop_weight']
                PolyWinCount += 1
            elif(currentDict['elec_result'] == -1):
                if(randChoice == 1):
                    count += currentDict['pop_weight']
                    PolyWinCount += 1
                    currentDict['elec_result'] = 1
                else:
                    currentDict['elec_result'] = 0
        if(count>thresh):
            result = True
        if(export==True):
            ExportTxt(result,PolyWinCount,dictlist)
        return result, PolyWinCount, dictlist

    #Decides randomly (with a bias) whether every polygon is won or lost
    def BiasRandomElection(self,dictlist,thresh,export=False):
        count=0
        PolyWinCount=0
        result = False
        for i in range(len(dictlist)):
            randChoice = random.randint(0,100)
            currentDict = dictlist[i]
            if(currentDict['elec_result'] == 1):
                count += currentDict['pop_weight']
                PolyWinCount += 1
            elif(currentDict['elec_result'] == -1):
                if(randChoice <= dictlist[i]['rad_bias']):
                    count += currentDict['pop_weight']
                    PolyWinCount += 1
                    currentDict['elec_result'] = 1
                else:
                    currentDict['elec_result'] = 0
        if(count>thresh):
            result = True
        if(export==True):
            ExportTxt(result,PolyWinCount,dictlist)
        return result, PolyWinCount, dictlist

    def SimulatedElection(dictlist,thresh,export=False):
            result = False
            totalWinCount = 0
            for i in range(len(dictlist)):
              winCount = 0
              whileCount = 0
              currentDict = dictlist[i]
              if(currentDict['elec_result']==-1):
                while(whileCount < 100):
                    roll = random.randint(0,100)
                    if(roll<currentDict['rad_bias']):
                        winCount+=1
                    whileCount += 1
                if(winCount >= 50):
                    currentDict['elec_result'] = 1
                    totalWinCount += 1
                else:
                    currentDict['elec_result'] = 0
              elif(currentDict['elec_result']==1):
                  totalWinCount += 1
            if(totalWinCount >= len(dictlist)/2):
                result = True
            return result, totalWinCount, dictlist

    #writes the results of the method to a .txt file
    #needs to print better (include names and what values acutally mean)
    def ExportTxt(self,result, dictlist,path):
        text_file = open("ElectionOutput.txt", "w")
        for i in range(len(dictlist)):
            text_file.write(str(dictlist[i])+'\n')
        text_file.close()
        return
