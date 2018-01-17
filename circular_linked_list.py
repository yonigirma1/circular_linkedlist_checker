#Circular linked list checler

Class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

########################

def circular_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker1.nextnode.nextnode

        if marker1 == marker2:
            return True


    return False
