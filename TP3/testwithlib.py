import bintrees, random, time, redblacktree

# Define arrays with random data
dataInsert = []
dataDelete = []

for i in range(0,100_000):
    n = random.randint(-100_000, 100_000)
    dataInsert.append(n)

count = 0

for n in dataInsert:
    probability = random.randint(0,100)
    if probability > 95:
        if n not in dataDelete:
            count +=1
            print(count)
            dataDelete.append(n)

# Create trees
treeAlgo = redblacktree.RedBlackTree()
treeLib = bintrees.RBTree()

# Insert Algo
timeA = time.time()
for n in dataInsert:
    redblacktree.insert(treeAlgo,n,n)
timeB = time.time()
print(f'INSERT ALGO: {timeB-timeA}')

# Insert Lib
timeA = time.time()
for n in dataInsert:
    treeLib.insert(n,n)
timeB = time.time()
print(f'INSERT LIB: {timeB-timeA}')

# Delete Algo
timeA = time.time()
for n in dataDelete:
    redblacktree.deleteKey(treeAlgo,n) #by key deberia ser
timeB = time.time()
print(f'DELETE ALGO: {timeB-timeA}')

# Delete Lib
timeA = time.time()
for n in dataDelete:
    treeLib.remove(n)
timeB = time.time()
print(f'DELETE LIB: {timeB-timeA}')

