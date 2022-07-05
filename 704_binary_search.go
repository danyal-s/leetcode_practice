# https://leetcode.com/problems/binary-search/

func search(nums []int, target int) int {

    if len(nums) == 0 {
        return -1
    }

    start_index := 0
    end_index := len(nums) - 1
    mid_index := ((end_index - start_index) / 2) + start_index
    
    for start_index != end_index && start_index < len(nums) && end_index >= 0 {
        if target == nums[mid_index] {
            return mid_index
        }
        if target < nums[mid_index]{
            end_index = mid_index - 1
        } else {
            start_index = mid_index + 1
        }
        mid_index = ((end_index - start_index) / 2) + start_index
    }
    
    if start_index < len(nums) && end_index >= 0 && target == nums[mid_index] {
        return start_index
    }
    
    return -1
    
    
}
