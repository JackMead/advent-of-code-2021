package day2

import (
	"aoc-2024/src/lib"
	"testing"
)

func TestPart1(t *testing.T) {
	input := lib.ReadFileLineByLine("test_input.txt")

	reports := convertInputToUsefulStructure(input)

	expectedResult := 2
	result := part1(reports)

	if result != expectedResult {
		t.Errorf("Day 1 Part 1 Answer = %d, want %d", result, expectedResult)
	}
}

func TestPart2(t *testing.T) {
	input := lib.ReadFileLineByLine("test_input.txt")

	reports := convertInputToUsefulStructure(input)

	expectedResult := 5
	result := part2(reports)

	if result != expectedResult {
		t.Errorf("Day 1 Part 2 Answer = %d, want %d", result, expectedResult)
	}
}
