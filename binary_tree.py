class BTree:
    def __init__(self, value, label=None, left_ch=None, right_ch=None):
        self.label = label
        self.value = value
        self.left_ch = left_ch
        self.right_ch = right_ch

    def isLeaf(self):
        return self.left_ch == None and self.right_ch == None
    
        
        
        
