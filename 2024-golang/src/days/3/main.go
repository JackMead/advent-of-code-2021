package day3

import (
	"aoc-2024/src/lib"
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
)

const dayNumber = 3

func SolveDay() {
	dayInput := lib.ReadFileLineByLine("src/days/" + strconv.Itoa(dayNumber) + "/input.txt")
	inputs := convertInputToUsefulStructure(dayInput)

	answerP1 := part1(inputs)

	fmt.Printf("Solved day %d Part 1: %d", dayNumber, answerP1)

	answerP2 := part2(inputs)

	fmt.Printf("Solved day %d Part 2: %d", dayNumber, answerP2)
}

func convertInputToUsefulStructure(dayInput []string) []string {
	return dayInput
}

func part1(input []string) int {
	total := 0
	r, _ := regexp.Compile("mul\\([0-9]+,[0-9]+\\)")
	for _, line := range input {
		matches := r.FindAllString(line, -1)
		fmt.Println(matches)
		for _, match := range matches {
			split := strings.Split(match, ",")
			a := split[0][4:]
			b := split[1][:len(split[1])-1]
			aInt, err := strconv.Atoi(a)
			if err != nil {
				log.Fatalf("Expected %s to be int", a)
			}
			bInt, err := strconv.Atoi(b)
			if err != nil {
				log.Fatalf("Expected %s to be int", b)
			}
			total += aInt * bInt
		}
	}

	return total
}

func part2(input []string) int {

	total := 0
	r, _ := regexp.Compile("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)")
	count := true
	for _, line := range input {
		matches := r.FindAllString(line, -1)
		for _, match := range matches {
			if match == "don't()" {
				count = false
				continue
			}
			if match == "do()" {
				count = true
				continue
			}
			if !count {
				continue
			}
			split := strings.Split(match, ",")
			a := split[0][4:]
			b := split[1][:len(split[1])-1]
			aInt, err := strconv.Atoi(a)
			if err != nil {
				log.Fatalf("Expected %s to be int", a)
			}
			bInt, err := strconv.Atoi(b)
			if err != nil {
				log.Fatalf("Expected %s to be int", b)
			}
			total += aInt * bInt
		}
	}

	return total
}
