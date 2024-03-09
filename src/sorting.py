
class IterableSort:
    def __init__(self, sequence: list):
        self.sequence = sequence

    # returns partially sorted list using binary sort
    def binary(self) -> list:
        """
        In the binary insertion sort mode, we divide the same members into two subarrays--filtered and unfiltered. The first element of the same members is in the organized subarray, and all other elements are unplanned.
        Then we iterate from the second element to the last. In the repetition of the i-th, we make the current object our “key”. This key is a feature that we should add to our existing list below.
        In order to do this, we first use a binary search on the sorted subarray below to find the location of an element larger than our key. Let's call this position “pos.” We then right shift all the elements from pos to 1 and created Array[pos] = key.
        We can note that in every i-th multiplication, the left part of the array till (i - 1) is already sorted.
        Source: https://www.geeksforgeeks.org/binary-insertion-sort/
        """
    # Czech to see whether or not self.sequence is sorted
    def isSorted(self) -> bool:
        for i in range(self.sequence.length):
            for j in range(i, self.sequence.length):
                if self.sequence[j] < self.sequence[i]:
                    return False
        return True