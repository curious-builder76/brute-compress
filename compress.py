import struct
class Filter:
    def __init__(self,n,  hash1, hash2):
        self.hash1=hash1
        self.hash2=hash2
        self.filter=bytearray((n+7)>>3)
        self.n=n
    def add(self,data):
        for hash in (self.hash1,hash2):
            h= hash(data)
            index= hash % self.n
            self.filter[index>>3]  |= (1<< (index & 7))
    def get(self,data):
        for hash in (self.hash1,hash2):
            h= hash(data)
            index= hash % self.n
            if not (self.filter[index>>3] & (1<<(index & 7)):
                return False
        return True
def compress(data):
    filter=Filter(len(data),hash1,hash2)
    for idx,data in enumerate(data):
        p=struct.pack(">Ic",idx,data)
        filter.add(p)
    return struct.pack(">I",len(data))+bytes(filter.filter)
def decompress(data):
    N=struct.unpack(">I",data[:4])[0]
    f=Filter(N,hash1,hash2)
    f.filter=bytearray(data[4:])
    for idx in range(N):
        for ch in range(256):
            p=struct.pack(">Ic",idx,ch)
            if filter.get(p):
                print(ch)
            
            
    
        
        
