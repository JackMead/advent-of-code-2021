package dayN

import (
	"aoc-2024/src/lib"
	"testing"
)

func TestPart1(t *testing.T) {
	input := lib.ReadFileLineByLine("test_input.txt")

	structure := convertInputToUsefulStructure(input)

	expectedResult := 2
	result := part1(structure)

	if result != expectedResult {
		t.Errorf("Day %d Part 1 Answer = %d, want %d", dayNumber, result, expectedResult)
	}
}

func TestPart2(t *testing.T) {
	input := lib.ReadFileLineByLine("test_input.txt")

	structure := convertInputToUsefulStructure(input)

	expectedResult := 5
	result := part2(structure)

	if result != expectedResult {
		t.Errorf("Day %d Part 2 Answer = %d, want %d", dayNumber, result, expectedResult)
	}
}
