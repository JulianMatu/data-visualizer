# sorting_algos.py

# generator using insertion sorting algo
def insertion_sort(sequence: list):

    # Traverse through 1 to len(sequence)
    for i in range(1, len(sequence)):

        key = sequence[i]

        # Move elements of self.sequence[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < sequence[j] :
                sequence[j + 1] = sequence[j]   
                j -= 1
        sequence[j + 1] = key
        yield sequence
    return

# generator using selection sorting algo
def selection_sort(sequence: list):
    for i in range(len(sequence)):
        min_index: int = i

        for j in range(i + 1, len(sequence)):
            
            # find min element
            if sequence[min_index] > sequence[j]:
                min_index = j

        # swap start index element with min element
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]

        yield sequence
    return

# generator using bubble sorting algo
def bubble_sort(sequence: list):

    # traverse through all array elements
    for i in range(len(sequence)):

        # keep track of whether or not we have swapped
        swapped = False

        for j in range(0, len(sequence) - i - 1):
            # check adjacent elements
            if sequence[j] > sequence[j+1]:

                # swap elements
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
                swapped = True
                yield sequence

        if (not swapped):
            break
    return

# generator using an iterative quick sort algo
def quick_sort(sequence: list):

    # partition helper function used to partition elements that are less than the pivot to the left
    # and elements that are greater than the pivot to the right
    def parition(sequence: list, low: int, high: int):
        start_index: int = low - 1
        high_element: int = sequence[high]

        for i in range(1, high):
            if sequence[start_index] <= high_element:
                start_index += 1
