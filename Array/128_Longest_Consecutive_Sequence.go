// n = len(nums)
// time: O(n)
// space: O(n)

func longestConsecutive(nums []int) int {
	numMap := make(map[int]bool)
	for _, num := range nums {
			numMap[num] = true
	}
	maxLen := 0
	for num := range numMap {
			if _, exists := numMap[num-1]; !exists {  
					currentNum := num
					currentLen := 1
					for {
							if _, preNum := numMap[currentNum+1]; preNum {
									currentNum++
									currentLen++
							} else {
									break
							}
					}
					if currentLen > maxLen {
							maxLen = currentLen
					}
			}
	}
	return maxLen
}
