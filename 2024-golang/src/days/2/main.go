package day2

import (
	"aoc-2024/src/lib"
	"fmt"
	"log"
	"strconv"
	"strings"
)

func SolveDay2() {
	day1Input := lib.ReadFileLineByLine("src/days/2/input.txt")
	reports := convertInputToUsefulStructure(day1Input)

	answerP1 := part1(reports)

	fmt.Printf("Solved day 2 Part 1: %d", answerP1)

	answerP2 := part2(reports)

	fmt.Printf("Solved day 2 Part 2: %d", answerP2)
}

func convertInputToUsefulStructure(day1Input []string) [][]int {
	reports := make([][]int, len(day1Input))
	for i, row := range day1Input {
		report := make([]int, 0)
		words := strings.Fields(row)
		for _, word := range words {
			v1, err := strconv.Atoi(word)
			if err != nil {
				log.Fatalf("Failed to convert %s to int", words[0])
			}
			report = append(report, v1)
		}
		reports[i] = report
	}
	return reports
}

func part1(reports [][]int) int {
	count := 0
	for _, report := range reports {
		if isReportValid(report) {
			count++
		}
	}
	return count
}

func isReportValid(report []int) bool {
	if len(report) < 2 {
		return true
	}

	asc := (report[0] < report[1])

	for i := 0; i < len(report)-1; i++ {
		diff := report[i+1] - report[i]
		if diff > 3 || diff < -3 || diff == 0 {
			return false
		}
		if (diff > 0) != asc {
			return false
		}
	}
	return true
}

func isReportValidWithDampening(report []int) bool {
	if len(report) < 2 {
		return true
	}

	asc := (report[0] < report[1])

	for i := 0; i < len(report)-1; i++ {
		diff := report[i+1] - report[i]
		if diff > 3 || diff < -3 || diff == 0 {
			removeFirst := getCopyOfSliceWithoutElement(report, i)
			removeSecond := getCopyOfSliceWithoutElement(report, i+1)
			return isReportValid(removeFirst) || isReportValid(removeSecond)
		}
		if (diff > 0) != asc {
			if i == 1 {
				// has to match for i == 0, by definition
				// if we've got past i == 1, then we know three elements follow the same pattern
				// so we can only continue in that direction
				removeFirst := getCopyOfSliceWithoutElement(report, 0)
				removeSecond := getCopyOfSliceWithoutElement(report, i+1)
				return isReportValid(removeFirst) || isReportValid(removeSecond)
			}
			removeSecond := getCopyOfSliceWithoutElement(report, i+1)
			return isReportValid(removeSecond)
		}
	}
	return true
}

func getCopyOfSliceWithoutElement(s []int, i int) []int {
	result := make([]int, len(s)-1)
	for j := 0; j < len(result); j++ {
		if j < i {
			result[j] = s[j]
		}
		if j >= i {
			result[j] = s[j+1]
		}
	}
	return result
}

func part2(reports [][]int) int {
	count := 0
	for _, report := range reports {
		if isReportValidWithDampening(report) {
			count++
		}

	}
	return count
}
