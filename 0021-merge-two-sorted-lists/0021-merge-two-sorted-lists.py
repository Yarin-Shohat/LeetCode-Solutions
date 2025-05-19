# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = ListNode()
        new_list_pointer = new_list
        while list1 != None and list2 != None:
            # If list2 item is smaller
            if list1.val > list2.val:
                new_list_pointer.next = ListNode(val=list2.val)
                list2 = list2.next
            # If list1 item is smaller
            else:
                new_list_pointer.next = ListNode(val=list1.val)
                list1 = list1.next
            new_list_pointer = new_list_pointer.next
        
        ## If one of the list is empty
        # list1 is empty
        if list1 == None:
            while list2 != None:
                new_list_pointer.next = ListNode(val=list2.val)
                list2 = list2.next
                new_list_pointer = new_list_pointer.next
        # list2 is empty
        if list2 == None:
            while list1 != None:
                new_list_pointer.next = ListNode(val=list1.val)
                list1 = list1.next
                new_list_pointer = new_list_pointer.next
        return new_list.next