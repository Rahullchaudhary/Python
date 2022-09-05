import numbers


numbers=list(range(1,11))
nums=[ i for i in numbers if i%2==0]
print(nums)
nums2=[i for i in range(1,11) if i%2==0]
print(nums2)
nums1=[i for i in range(1,11) if i%2]
print(nums1)