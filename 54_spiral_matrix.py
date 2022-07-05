# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        operations_order = None
        if len(matrix[0]) == 1:
            operations = [go_down, go_left, go_up, go_right]
            boundaries = [len(matrix), -1, -1, len(matrix[0])]
        else:
            operations = [go_right, go_down, go_left, go_up]
            boundaries = [len(matrix[0]), len(matrix), -1, -1]
            
        res = [matrix[0][0]]
        i = 0
        r, c = 0, 0
        while True:
            r, c, res_temp, boundary = operations[i](matrix, r, c, boundaries[i])
            if len(res_temp) == 0:
                break
            res += res_temp
            boundaries[(i-1)%len(boundaries)] = boundary
            i = (i+1)%len(operations)
        
        return res

    
def go_right(matrix, r, c, boundary_c_max):
    res = []
    while c+1 != boundary_c_max:
        c+=1
        res.append(matrix[r][c])

    boundary_r_min = r
    return r, c, res, boundary_r_min



def go_down(matrix, r, c, boundary_r_max):
    res = []
    while r+1 != boundary_r_max:
        r+=1
        res.append(matrix[r][c])

    boundary_c_max = c
    return r, c, res, boundary_c_max


def go_left(matrix, r, c, boundary_c_min):
    res = []
    while c-1 != boundary_c_min:
        c-=1
        res.append(matrix[r][c])

    boundary_r_max = r 
    return r, c, res, boundary_r_max


def go_up(matrix, r, c, boundary_r_min):
    res = []
    while r-1 != boundary_r_min:
        r-=1
        res.append(matrix[r][c])

    boundary_c_min = c
    return r, c, res, boundary_c_min


