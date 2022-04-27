class BTree:
    def __init__(self, value, label=None, left_ch=None, right_ch=None):
        """
        input: value, label, left_ch, right_ch
        output: nothing
        constructor of the class
        """
        self.label = label
        self.value = value
        self.left_ch = left_ch
        self.right_ch = right_ch

    def isLeaf(self):
        """
        input: object BTree (self)
        output: boolean
        return true if the object passed in parameter is a leaf false otherwise
        """
        return self.left_ch == None and self.right_ch == None
    
        
        
        
