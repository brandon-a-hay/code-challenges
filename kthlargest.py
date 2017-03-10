def findKthLargest(nums, k):
    # sort the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp

    if k >= len(nums):
        'index out of bounds'
        return None

    return nums[-k]

print findKthLargest([5, 6, 7, 2, 4], 2)