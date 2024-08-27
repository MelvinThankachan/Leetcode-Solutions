# For testing problem: 49
def are_equal_arrays(arr1, arr2):
    # Helper function to sort each sub-array and the outer array
    def sort_nested_array(arr):
        return sorted([sorted(sub_array) for sub_array in arr])

    # Sort both arrays and compare
    return sort_nested_array(arr1) == sort_nested_array(arr2)
