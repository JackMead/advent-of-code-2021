package lib

import "testing"

func TestFileLoads(t *testing.T) {
	wants := make([]string, 4)
	wants[0] = "a"
	wants[1] = "sentence"
	wants[2] = "of"
	wants[3] = "words"
	lines := ReadFileLineByLine("./fake_input.txt")

	for index, line := range lines {
		if line != wants[index] {
			t.Errorf("ReadFileLineByLine() = %s, want %s", line, wants[index])
		}
	}
}
