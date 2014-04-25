from collections import Counter
import math
def calcEntropy(ilist):
    entropy = 0
    cnt = Counter(ilist)
    length = len(dice)
    for k, v in cnt.items():
        entropy += (-math.log(v/length))
    return entropy/length

if __name__ == "__main__":
    dice = [1,1,1,2,3,4]
    print(calcEntropy(dice))





