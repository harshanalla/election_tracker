class handler:
    # def __init__(self, shape_field, election_field, weight_field, bias_field):
    #     self.shape_field = shapefile_fied
    #     self.election_field = election_field
    #     self.weight_field = self.weight_field
    #     self.bias_field = bias_field



    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        ID = "ID"
        if self.data:
            if data[ID]<self.data[ID]:
                if self.left is None:
                    self.left = handler(data)
                    return True
                else:
                    self.left.insert(data)
            elif data[ID]>self.data[ID]:
                if self.right is None:
                    self.right = handler(data)
                    return True
                else:
                    self.right.insert(data)
            else:
                return False
        else:
            self.data = data


    def findDataWithID(self, ID):
        if ID < self.data["ID"]:
            if self.left is None:
                return False, None
            return self.left.findDataWithID(ID)
        elif ID > self.data["ID"]:
            if self.right is None:
                return False, None
            return self.right.findDataWithID(ID)
        else:
            return True, self.data

    def updateData(self, newData):
        ID = newData["ID"]
        if ID < self.data["ID"]:
            if self.left is None:
                return False
            return self.left.updateData(newData)
        elif ID > self.data["ID"]:
            if self.right is None:
                return False
            return self.right.updateData(newData)
        else:
            self.data = newData
            return True


    def sortedlistToBST(self, list):

        if not list:
            return None


        mid = int(len(list)/2)


        root = handler(list[mid])

        root.left = self.sortedlistToBST(list[:mid])


        root.right = self.sortedlistToBST(list[mid+1:])

        return root
