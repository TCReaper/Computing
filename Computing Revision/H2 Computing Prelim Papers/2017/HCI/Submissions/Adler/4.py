class Node():
    def __init__(self, Name, Score, LeftP, RightP):
        self._Name = Name
        self._Score = Score
        self._LeftP = LeftP
        self._RightP = RightP

    def get_Name(self):
        return self._Name

    def set_Name(self, new_Name):
        self._Name = new_Name

    def get_Score(self):
        return self._Score

    def set_Score(self, new_Score):
        self._Score = new_Score

    def get_LeftP(self):
        return self._LeftP

    def set_LeftP(self, new_LeftP):
        self._LeftP = new_LeftP

    def get_RightP(self):
        return self._RightP

    def set_RightP(self, new_RightP):
        self._RightP = new_RightP

    def __str__(self):
        return "{0:<20}{1:<7}{2:<7}{3}"\
               .format(self._Name, self._Score, self._LeftP, self._RightP)

class BinaryTree():
    def __init__(self):
        self._ThisTree = [None]
        for i in range(2, 21):
            self._ThisTree.append(Node('', '', i, 0))
        self._ThisTree.append(Node('', '', 0, 0))
        #additional None at the start to account for 1-indexing
        self._Root = 0
        #self._Root = 0 means nothing is currently in the tree
        self._NextFreePosition = 1

    def AddNodeToTree(self, Name, Score):
        if self._NextFreePosition == 0:
            print("Tree is full. Unable to add to tree.")
            return
        self._ThisTree[self._NextFreePosition].set_Name(Name)
        self._ThisTree[self._NextFreePosition].set_Score(Score)
        temp = self._ThisTree[self._NextFreePosition].get_LeftP()
        self._ThisTree[self._NextFreePosition].set_LeftP(0)
        if self._Root == 0:
            self._Root = 1
        else:
            cur = self._Root
            while True:
                if cur == 0:
                    raise ValueError
                if Score > self._ThisTree[cur].get_Score():
                    if self._ThisTree[cur].get_RightP() == 0:
                        self._ThisTree[cur].set_RightP(\
                            self._NextFreePosition)
                        break
                    cur = self._ThisTree[cur].get_RightP()
                else:
                    if self._ThisTree[cur].get_LeftP() == 0:
                        self._ThisTree[cur].set_LeftP(\
                            self._NextFreePosition)
                        break
                    cur = self._ThisTree[cur].get_LeftP()
        self._NextFreePosition = temp

    def OutputData(self):
        print("Root: ", self._Root)
        print("NextFreePosition: ", self._NextFreePosition)
        if self._Root == 0:
            print("Tree is empty.")
        else:
            print("\n{0:<8}{1:<20}{2:<7}{3:<7}{4}"
                  .format("Index", "Name", "Score", "LeftP", "RightP"))
            for i in range(self._Root, len(self._ThisTree)):
                print("{0:<8}{1}".format(i, self._ThisTree[i]))

    def RankList(self):
        if self._Root == 0:
            print("Tree is empty.")
        else:
            print("\n{0:<20}{1}"
                  .format("Name", "Score"))
            self.InReverseOrderTraversal(self._Root)
                
    def InReverseOrderTraversal(self, cur_index):
        if cur_index != 0:
            self.InReverseOrderTraversal(\
                self._ThisTree[cur_index].get_RightP())
            print("{0:<20}{1}"\
                  .format(self._ThisTree[cur_index].get_Name(), \
                          self._ThisTree[cur_index].get_Score()))
            self.InReverseOrderTraversal(\
                self._ThisTree[cur_index].get_LeftP())


file_handle = open("SCORES.txt")
file_data = []
for line in file_handle:
    temp = line.strip().split("|")
    temp[1] = int(temp[1])
    file_data.append(temp)
file_handle.close()

#bst: binary search tree
bst = BinaryTree()
for data in file_data:
    bst.AddNodeToTree(data[0], data[1])
bst.OutputData()
bst.RankList()
