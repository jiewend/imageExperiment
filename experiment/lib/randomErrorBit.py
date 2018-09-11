import codecs
import binascii
import os
import numpy as np
from tqdm import tqdm

PROJECT_PATH = "/home/ucc/WorkPlace/imageCompress/experiment"
LIB_PATH = os.path.join(PROJECT_PATH, 'lib')
DOC_PATH = os.path.join(PROJECT_PATH, 'doc')

def loadImageHex(inFileName):
    filePath = os.path.join(DOC_PATH, inFileName)
    with open(filePath, 'rb') as f:
        hexdata = binascii.hexlify(f.read())
    print "image size:", len(hexdata)
    return hexdata        
def writeImageHex(hexdata, outFileName):
    filePath = os.path.join(DOC_PATH, outFileName)
    with open(filePath, 'wb') as fout:
        fout.write(binascii.a2b_hex(hexdata))

def addRandError(hexdata, errorRate):
    errorStream = np.random.choice([0, 1], len(hexdata), p=[1-errorRate, errorRate])
    hexdataError = bytearray(hexdata)
    hexMeta = list('0123456789abcdef')

    print("adding error")
    for i in tqdm(range(5000, len(hexdata) - 5000)):
        if errorStream[i] == 1:
            hexdataError[i] = str(np.random.choice(hexMeta))
    hexdataError = str(hexdataError)            
    return hexdataError
            


    



if __name__ == '__main__':
    hexdata = loadImageHex('bb.jp2')
    writeImageHex(hexdata, 'fout.jp2')
    #  print(hexdata)
    hexdata = addRandError(hexdata, 0.00001)
    #  print(hexdata)
    writeImageHex(hexdata, 'broken.jp2')


    #  writeImageHex(hexdata, 'fout.jp2')




