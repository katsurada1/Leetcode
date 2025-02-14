// n = len(nums)
// time: O(n logn)
// space: O(n)

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int)
	for _, num := range nums {
			freqMap[num] ++
	}
	type freqNumber struct {
			num int
			count int
	}
	freqList := []freqNumber{}
	for num, count := range freqMap {
			freqList = append(freqList, freqNumber{num, count})
	}
	sort.Slice(freqList, func(i, j int) bool {
	return freqList[i].count > freqList[j].count
})

	result := make([]int, k)
	for i := 0; i < k; i++ {
		result[i] = freqList[i].num
	}
return result
}