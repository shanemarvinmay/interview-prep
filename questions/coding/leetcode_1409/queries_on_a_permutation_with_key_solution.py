class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = next
    
    def __init__(self, m=1):
        self.head = self.Node(1)
        itr = self.head
        for i in range(2, m+1):
            itr.next = self.Node(i)
            itr = itr.next

    def process_query(self, query):
        '''return idx, move query node to head'''
        if self.head.value == query:
            return 0
        
        # Finding idx of query
        idx = 1
        itr = self.head
        while itr.next.value != query:
            itr = itr.next
            idx += 1

        # Moving query to the head.
        new_head = itr.next
        itr.next = itr.next.next
        new_head.next = self.head
        self.head = new_head

        return idx

class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        '''
        loop through queries
            get idx of query
                move node at query to top
            append idx to output
        return output
        '''
        output = []
        # Create linked list from 1 to m. Time O(m)
        linked_list = LinkedList(m)
        # Processing Queries. Time(num queries * m)
        for query in queries:
            output.append(linked_list.process_query(query))
        
        return output