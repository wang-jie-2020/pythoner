"""
    items = []
    for i in range(1, 100):
        if i % 3 == 0 or i % 5 == 0:
            items.append(i)
    print(items)
"""
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)