nums1.reverse()
for i in range(n):
    nums1.pop(0)
nums1.reverse()

for i in range(len(nums1)):
    for j in nums2:
        if j<nums1[i]:
            nums1.insert(i,j)
            nums2.remove(j)
nums1.extend(nums2)

nums2.clear()
nums2 = sorted(nums1)
nums1.clear()
for i in nums2:
    nums1.append(i)
print(nums1)
