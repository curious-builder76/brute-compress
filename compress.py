class Filter:
    def __init__(self,n,  hash1, hash2):
        self.hash1=hash1
        self.hash2=hash2
        self.filter=bytearray(n)
        self.n=n
    def add(self,data):
        h1=self.hash1(data)
        h2=self.hash2(data)
        
        
