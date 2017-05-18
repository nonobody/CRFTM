import numpy as np

def compute_pzd(ModelName, ShortTextPath):
    wordmap = {}
    f=open(ModelName + ".vocabulary","r")
    j = 0
    for line in f:
        word,idx = line.split()
        wordmap[word] = int(idx)
    f.close()

    phi = np.zeros((len(wordmap), k))

    f=open(ModelName + ".phi","r")
    j = 0
    for line in f:
        rs = line.split()
        for i in xrange(len(rs)):
            phi[i][j] = rs[i]
        j += 1
    f.close()

    for i in xrange(len(phi)):
         phi[i] /= np.sum(phi[i])

    tassign = []
    f=open(ModelName + ".topicAssignments","r")
    j = 0
    for line in f:
        tassign.append(line.split())
    f.close()

    pz = np.zeros((k))

    for i in xrange(len(tassign)):
        for j in xrange(len(tassign[i])):
            pz[int(tassign[i][j])] += 1
    pz /= np.sum(pz)

    pwz = np.zeros((len(wordmap), k))
    for i in xrange(len(wordmap)):
        pwz[i] = pz * phi[i]

    for i in xrange(len(pwz)):
        pwz[i] /= np.sum(pwz[i])

    strevs = []
    f=open(ShortTextPath,"r")
    j = 0
    for line in f:
        word = line.split()
        strevs.append(word)
    f.close()

    pzd = np.zeros((len(strevs), k))

    for i in xrange(len(strevs)):
        v = 0
        for word in strevs[i]:
            v += pwz[wordmap[word]]
        v /= np.sum(v)
        pzd[i] = v
    return pzd

def write_pzd(ModelName, pzd):
    f=open(ModelName + ".pzd","w")
    for i in xrange(len(pzd)):
        for j in xrange(k):
            f.write(str(pzd[i][j]) + " ")
        f.write('\n')
    f.close()

if __name__=="__main__":
    k =40
    ModelName = "1_40_sample"
    ShortTextPath = "sample.txt"
    pzd = compute_pzd(ModelName, ShortTextPath)
    write_pzd(ModelName, pzd)