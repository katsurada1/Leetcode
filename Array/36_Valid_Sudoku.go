// n = len(board)
// time: O(n^2)
// space: O(n^2)

func isValidSudoku(board [][]byte) bool {
	var rowCheck [9][9]bool
	var colCheck [9][9]bool
	var boxCheck [9][9]bool

	for i := 0; i < 9; i++ {
			for j := 0; j < 9; j++ {
					char := board[i][j]
					if char == '.' {
							continue 
					}

					digit := char - '1'
					if rowCheck[i][digit] {
							return false
					}

					rowCheck[i][digit] = true
					if colCheck[j][digit] {
							return false
					}

					colCheck[j][digit] = true
					boxIndex := (i/3)*3 + (j/3)
					if boxCheck[boxIndex][digit] {
							return false
					}

					boxCheck[boxIndex][digit] = true
			}
	}
	return true
}