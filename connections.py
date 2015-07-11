# coding: utf-8
"""
question:
1,2,3,4,5,6,7,8

union(1, 2)
union(2, 4)
union(3, 8)
union(2, 6)

is_connect(1, 6)  # True

"""

class Connect(object):
    def __init__(self):
        self.connected_components = []

    def union(self, a, b):
        new_set = {a, b}
        if not self.connected_components:
            self.connected_components.append(new_set)
        else:
            index_list = []
            # get all repeated item's index
            for idx, component in enumerate(
                    self.connected_components):

                if new_set & component:
                    index_list.append(idx)

            # if has repeated item
            if index_list:
                target = self.connected_components[index_list[0]]

                # merge to the first one, and merge the new comer
                for idx in index_list[1:]:
                    target |= self.connected_components[idx]
                target |= new_set

                # get rid of merged items, leave the first one
                self.connected_components = [
                    item for idx, item in enumerate(
                        self.connected_components) 
                    # index_list[0] is reserved
                    if idx not in index_list[1:]]

                # give it back 
                self.connected_components[index_list[0]] = target 

            # add new member at end
            else:
                self.connected_components.append(new_set)

        # see it        
        print self.connected_components

    def is_connect(self, a, b):
        test_set = {a, b}
        # check subset
        return any(
            [test_set.issubset(c) 
                for c in self.connected_components])

con = Connect()
con.union(1,2)
con.union(4,3)
con.union(1,3)
con.union(6,8)
print con.is_connect(1,8)
con.union(6,1)
print con.is_connect(1,8)




