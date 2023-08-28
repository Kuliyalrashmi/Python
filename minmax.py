scores,taimport math
def minimax(currDepth,nodeIndex,maxTurn,scores,targetDepth):
    if currDepth==targetDepth:
        return scores[nodeIndex]
    if(maxTurn):
        return max(minimax((currDepth+1),(nodeIndex*2),False,scores,targetDepth),
        minimax((currDepth+1),(nodeIndex*2+1),False,scores,targetDepth))
    else:
        return min(minimax((currDepth+1),(nodeIndex*2),True,scores,targetDepth),
        minimax((currDepth+1),(nodeIndex*2+1),True,rgetDepth))

scores=[3,5,2,9,12,50,13,5]
targetDepth=math.log(len(scores),2)
print("The Optimal Value is:",end=" ")
print(minimax(0,0,True,scores,targetDepth))