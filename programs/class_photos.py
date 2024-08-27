"""
A class has even number of students: half wearing red and half wearing blue.
Arrange the students in two rows and see if the following three conditions
can be met:
    * All students in red must be in the same row
    * All students in blue must be in the same row
    * Each student in the back row must be strictly taller than the student
    directly in the front row.

Example:
Input:
    red_heights = [5, 8, 1, 3, 4]
    blue_heights = [6, 9, 2, 4, 5]
Output:
    True

Created on Mon Aug 08, 2022
"""

from typing import List


def class_photos(red_heights: List[int], blue_heights: List[int]) -> bool:
    # The tallest of all students, be in red or blue, must be in the back row,
    # which can tell the back row should be red or blue.

    assert len(red_heights) == len(blue_heights)

    red_heights.sort(reverse=True)
    blue_heights.sort(reverse=True)
    red_max = red_heights[0]
    blue_max = blue_heights[0]

    if red_max < blue_max:
        row1, row2 = red_heights, blue_heights
    elif red_max > blue_max:
        row1, row2 = blue_heights, red_heights
    else:  # red_max == blue_max
        return False

    for i in range(len(row1)):
        if row1[i] >= row2[i]:
            return False

    return True


def main():
    red_heights = [5, 8, 1, 3, 6]
    blue_heights = [5, 9, 2, 4, 7]
    print("Red:", red_heights)
    print("Blue:", blue_heights)
    print(class_photos(red_heights=red_heights, blue_heights=blue_heights))


if __name__ == "__main__":
    main()
