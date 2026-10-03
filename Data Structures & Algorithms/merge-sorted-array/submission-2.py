class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        first_end = m - 1
        second_end = n - 1
        total = len(nums1) - 1

        while first_end > -1 and second_end > -1:
            if nums1[first_end] > nums2[second_end]:
                nums1[total] = nums1[first_end]
                first_end -= 1
            elif nums1[first_end] <= nums2[second_end]:
                nums1[total] = nums2[second_end]
                second_end -= 1
            total -= 1
        if second_end > -1:
            while total > -1:
                nums1[total] = nums2[second_end]
                total -= 1
                second_end -= 1
                print(nums1)
        elif first_end > - 1:
            while total > -1:
                nums1[total] = nums1[first_end]
                total -= 1
                first_end -= 1
                print(nums1)

                