#Binary search algo

def bsearch(list,val):
    index0=0
    indexLast=len(list)-1

    while index0<=indexLast:
        indexMid= (index0+indexLast)//2
        mid_value=list[indexMid]
        if mid_value==val:
            return indexMid
        if val<mid_value:
            indexLast = indexMid-1
        elif val>mid_value:
            index0 = indexMid + 1
        elif index0>indexLast:
            return None
list = [2,7,19,34,53,72,84]

print(bsearch(list,84))
print(bsearch(list,11))
#
# def bsearch(list, val):
#    list_size = len(list) - 1
#    idx0 = 0
#    idxn = list_size
# # Find the middle most value
#    while idx0 <= idxn:
#         midval = (idx0 + idxn)// 2
#         if list[midval] == val:
#             return midval
# # Compare the value the middle most value
#         if val > list[midval]:
#             idx0 = midval + 1
#         else:
#             idxn = midval - 1
#         if idx0 > idxn:
#             return None
# # Initialize the sorted list


