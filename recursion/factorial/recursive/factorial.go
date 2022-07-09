func factorial(n int) (value int) {
	if n == 2 {
		return 2
	} else {
		return factorial(n - 1) * n
	}
}



