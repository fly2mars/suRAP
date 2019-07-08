# utils/class_utils.py

class Encoder(object):
    def encode(self, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))
    
class A(object):
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        super(B,self).__init__()
        print("B init")
class C(A):
    def __init__(self):
        super(C,self).__init__()
        print("C init")

class D(B,C):
    def __init__(self):
        super(D,self).__init__()
        print("D init")