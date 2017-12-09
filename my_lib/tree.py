class Node(object):
    def __init__(self, ip='', num=0, parent_node=None, child_dict={}):
        self.ip = ip
        self.count = num
        self.parent = parent_node
        self.node_link = None
        self.child_dict = child_dict

    def increase(self, num):
        """add count for the node
        :param num: the count num
        :return: none
        """
        self.count += num

    def show(self,dep=1):
        """show the node for coder debug
        :param dep:current node depth
        :return: none
        """
        print(' '*dep, self.ip, ' ', self.count)
        for child in self.child_list:
            child.show(dep+1)

