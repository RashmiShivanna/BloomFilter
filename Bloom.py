from bitarray import bitarray
import math
import mmh3

fin = open('listed_username_30.txt')
members = fin.readlines()
# Number of members in the set
m = len(members)

# Size of the array chosen
n = 12110731
#n = 5752403

# Number of hash functions
k = round(math.log(2.0) * n / m)

# Initialize all the bits in the array to zero
bitArray = bitarray(n)
bitArray.setall(0)

# Hash all the members in the set and set the bit in the array correspondint to the obtained hash to 1
def mapMem(mem):
    for i in range(int(k)):
        bitArray[mmh3.hash(mem,i)%n] = 1

for mem in members:
    mapMem(mem)

# Read the stream
f = open('listed_username_365.txt')
stream = f.readlines()

SpamCount = 0
FP = 0

# Function to check if the username in the stream is in the array or not
def checkSpam(usr):
        for i in range(int(k)):
            hsh = mmh3.hash(usr,i)%n
            if bitArray[hsh] != 1:
                print (usr+" not present")
                return 0
        return 1

for usr in stream:
    if checkSpam(usr):
        FP = FP+1
    else:
        SpamCount = SpamCount+1

print("Number of members in the set: "+str(m))
print("Number of bits in the filter array: "+str(n))
print("Number of has functions used: "+str(k))
print("Number of items in the stream: "+str(len(stream)))
print("SpamCount: "+str(SpamCount))
print("False poisitve count: "+str(FP))
print("Percentage of false positives: "+str((float(FP)/float(len(stream))*100)))
print("False Positive probability: "+ str( pow((1- math.exp(-k*m/n)),k )))
