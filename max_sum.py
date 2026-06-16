def kadane(arr):
    max_sum = arr[0]
    curr = arr[0]

    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        max_sum = max(max_sum, curr)

    return max_sum


def maxSumRectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = float('-inf')

    for left in range(cols):
        temp = [0] * rows

        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            result = max(result, kadane(temp))

    return result


M = [[1,2,-1,-4,-20],
     [-8,-3,4,2,1],
     [3,8,10,1,3],
     [-4,-1,1,7,-6]]

print(maxSumRectangle(M))