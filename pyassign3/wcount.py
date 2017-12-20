import sys
import string
from urllib.request import urlopen
sys.setrecursionlimit(100000)

def qs(lists,left,right):
    if left>=right:
        return lists
    key=lists[left]
    low=left
    high=right
    while left<right:
        while left<right and lists[right]<=key:
            right-=1
        lists[left]=lists[right]
        while left<right and lists[left]>=key:
            left+=1
        lists[right]=lists[left]
    lists[right]=key
    qs(lists,low,left-1)
    qs(lists,left+1,high)
    return lists

def wcount(lines, topn=10):
    t=lines.split()
    d={}
    for c in t:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1

    z=list(d.values())
    zt=qs(z,0,len(z)-1)
    for i in range(10):
        for key in d.keys():
            if d[key]==zt[i]:
                print(key,'\t',zt[i])
            
if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
