fname = input('enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()

    # print(lin)
    wds = lin.split()

    # print(wrds)
    for w in wds:
        # oldcount = di.get(w, 0)
        # print(w, 'old', oldcount)

        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w,'new', newcount)

        # one liner
        di[w] = di.get(w, 0) + 1
        print(w, 'new', di[w])

        # if w in di:
        #    di[w] = di[w] + 1
        #    print('**Existing**')
        # else:
        #    di[w] = 1
        #    print('**new**')
        # print(w, di[w])

# print(di)

# find most common word
largest = -1
theword = None
for key, value in di.items():
    print(key, value)
    if value > largest:
        largest = value
        theword = key
print('Most common word was: ', theword, largest)
