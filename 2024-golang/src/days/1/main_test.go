package day1

import (
	"aoc-2024/src/lib"
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	input := lib.ReadFileLineByLine("test_input.txt")

	arr1, arr2 := convertInputToUsefulStructure(input)

	expectedResult := 11
	fmt.Println(arr1)
	result := sortAndSumDistances(arr1, arr2)
	fmt.Println(arr1)

	if result != expectedResult {
		t.Errorf("Day 1 Part 1 Answer = %d, want %d", result, expectedResult)
	}
}

func TestPart2(t *testing.T) {
	input := lib.ReadFileLineByLine("test_input.txt")

	arr1, arr2 := convertInputToUsefulStructure(input)
	// Note that this is *bad* code
	// But part 2 relies on the fact we sorted as part of P1
	// so we just call the relevant part of P1 here
	sortAndSumDistances(arr1, arr2)

	expectedResult := 31
	result := scoreSimilarity(arr1, arr2)

	if result != expectedResult {
		t.Errorf("Day 1 Part 2 Answer = %d, want %d", result, expectedResult)
	}
}
