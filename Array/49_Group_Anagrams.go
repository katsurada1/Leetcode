// k = len(str)
// n = len(strs)
// time: O(n*klogk)
// space: O(n)

func sortStrings(s string) string {
	split_chars := strings.Split(s, "")
	sort.Strings(split_chars)
	return strings.Join(split_chars, "")
}

func groupAnagrams(strs []string) [][]string {
	anagramMap := make(map[string][]string)
	for _, str := range strs {
			sortedStr := sortStrings(str)
			anagramMap[sortedStr] = append(anagramMap[sortedStr], str)
	}
	result := [][]string{}
	for _, group := range anagramMap{
			result = append(result, group)
	}
	return result
}