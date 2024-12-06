package day4

import (
	"aoc-2024/src/lib"
	"fmt"
	"strconv"
	"strings"
)

const dayNumber = 4 // CHANGE ME

func SolveDay() {
	dayInput := lib.ReadFileLineByLine("src/days/" + strconv.Itoa(dayNumber) + "/input.txt")
	inputs := convertInputToUsefulStructure(dayInput)

	answerP1 := part1(inputs)

	fmt.Printf("Solved day %d Part 1: %d", dayNumber, answerP1)

	answerP2 := part2(inputs)

	fmt.Printf("Solved day %d Part 2: %d", dayNumber, answerP2)
}

func convertInputToUsefulStructure(dayInput []string) [][]string {
	result := make([][]string, len(dayInput))
	for i, row := range dayInput {
		result[i] = strings.Split(row, "")
	}
	return result
}

type direction struct{ x, y int }

func part1(input [][]string) int {
	// plan
	// don't optimise
	// look for every x
	// check if any of the surrounding directions could make xmas
	count := 0
	rowUpper := len(input)
	colUpper := len(input[0])
	for rowIndex, row := range input {
		for colIndex, letter := range row {
			if letter != "X" {
				continue
			}
			directions := [8]direction{
				{1, 1},
				{1, 0},
				{1, -1},
				{0, 1},
				{0, -1},
				{-1, 1},
				{-1, 0},
				{-1, -1}}
			for _, direction := range directions {
				endRow := rowIndex + direction.y*3
				endCol := colIndex + direction.x*3
				if endRow >= 0 && endRow < rowUpper && endCol >= 0 && endCol < colUpper {
					s := "MAS"
					valid := true
					for i := 1; i <= 3; i++ {
						expected := string(s[i-1])
						if input[rowIndex+direction.y*i][colIndex+direction.x*i] != expected {
							valid = false
							break
						}
					}
					if valid {
						count++
					}
				}
			}
		}
	}
	return count
}

func part2(input [][]string) int {
	count := 0
	rowUpper := len(input)
	colUpper := len(input[0])
	for rowIndex, row := range input {
		for colIndex, letter := range row {
			if letter != "A" {
				continue
			}
			if rowIndex > 0 && rowIndex < rowUpper-1 && colIndex > 0 && colIndex < colUpper-1 {
				topLeft := input[rowIndex-1][colIndex-1]
				bottomRight := input[rowIndex+1][colIndex+1]

				topRight := input[rowIndex-1][colIndex+1]
				bottomLeft := input[rowIndex+1][colIndex-1]

				if (topLeft == "M" && bottomRight == "S") ||
					(topLeft == "S" && bottomRight == "M") {
					if (topRight == "M" && bottomLeft == "S") ||
						(topRight == "S" && bottomLeft == "M") {
						count++
					}
				}

			}
		}
	}
	return count
}
