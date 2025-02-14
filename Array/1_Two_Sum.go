// time: O(n)
//space: O(n)

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for i, num := range nums {
	 complement := target - num
	 index, exists := numMap[complement]
	 if exists {
			 return []int {i, index}
	 }
	 numMap[num] = i
	} 
	return nil
}