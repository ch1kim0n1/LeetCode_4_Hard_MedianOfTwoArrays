class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    left = B[j-1]
                elif j == 0:
                    left = A[i-1]
                else:
                    left = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1:
                    return float(left)
                if i == m:
                    right = B[j]
                elif j == n:
                    right = A[i]
                else:
                    right = min(A[i], B[j])
                return (left + right) / 2.0
