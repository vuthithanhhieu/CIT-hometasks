package prime_number

import (
	"math"
)

func Find(quantity uint) []uint {
	var counter, i uint = 0, 2
	prime_numbers := make([]uint, quantity)
	for i = 2; counter < quantity; i++ {
		if isPrime(i) {
			prime_numbers[counter] = i
			counter++
		}
	}
	return prime_numbers
}

func isPrime(num uint) bool {
	var i uint
	for i = 2; i <= uint(math.Sqrt(float64(num))); i++ {
		if num % i == 0 {
			return false
		}
	}
	return true
}
