package day1

import (
	"aoc-2024/src/lib"
	"fmt"
	"log"
	"sort"
	"strconv"
	"strings"
)

func SolveDay1() {
	day1Input := lib.ReadFileLineByLine("src/days/1/input.txt")
	arr1, arr2 := convertInputToUsefulStructure(day1Input)

	answerP1 := sortAndSumDistances(arr1, arr2)

	fmt.Printf("Solved day 1 Part 1: %d", answerP1)

	answerP2 := scoreSimilarity(arr1, arr2)

	fmt.Printf("Solved day 1 Part 1: %d", answerP2)
}

func convertInputToUsefulStructure(day1Input []string) (arr1 []int, arr2 []int) {
	for _, row := range day1Input {
		words := strings.Fields(row)
		v1, err := strconv.Atoi(words[0])
		if err != nil {
			log.Fatalf("Failed to convert %s to int", words[0])
		}
		v2, err := strconv.Atoi(words[1])
		if err != nil {
			log.Fatalf("Failed to convert %s to int", words[1])
		}
		arr1 = append(arr1, v1)
		arr2 = append(arr2, v2)
	}
	return arr1, arr2
}

func sortAndSumDistances(arr1 []int, arr2 []int) int {
	sort.Ints(arr1)
	sort.Ints(arr2)
	sum := 0
	for idx, _ := range arr1 {
		v1 := arr1[idx]
		v2 := arr2[idx]
		sum += lib.AbsDifference(v1, v2)
	}
	return sum
}

func scoreSimilarity(arr1, arr2 []int) int {
	totalScore := 0
	// Nothing clever, just rely on the fact they were previously sorted so we can
	// exit early
	for _, v1 := range arr1 {
		for _, v2 := range arr2 {
			// fmt.Printf("Comparing %d to %d", v1, v2)
			if v1 == v2 {
				totalScore += v1
				// fmt.Printf("Adding %d since %d = %d", v1, v1, v2)
			}
			if v1 < v2 {
				break
			}
		}
	}
	return totalScore
}
