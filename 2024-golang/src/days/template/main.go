package dayN

import (
	"aoc-2024/src/lib"
	"fmt"
	"strconv"
)

const dayNumber = 1 // CHANGE ME

func SolveDay() {
	dayInput := lib.ReadFileLineByLine("src/days/" + strconv.Itoa(dayNumber) + "/input.txt")
	inputs := convertInputToUsefulStructure(dayInput)

	answerP1 := part1(inputs)

	fmt.Printf("Solved day %d Part 1: %d", dayNumber, answerP1)

	answerP2 := part2(inputs)

	fmt.Printf("Solved day %d Part 2: %d", dayNumber, answerP2)
}

func convertInputToUsefulStructure(dayInput []string) interface{} {
	return nil
}

func part1(input interface{}) int {
	return 0
}

func part2(input interface{}) int {
	return 0
}
