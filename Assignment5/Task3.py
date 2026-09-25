"""Examples of Python operators, precedence, and associativity."""


if __name__ == "__main__":
	print("Arithmetic operators")
	print("10 + 3 =", 10 + 3)
	print("10 - 3 =", 10 - 3)
	print("10 * 3 =", 10 * 3)
	print("10 / 3 =", 10 / 3)
	print("10 // 3 =", 10 // 3)
	print("10 % 3 =", 10 % 3)
	print("10 ** 3 =", 10 ** 3)

	print("\nComparison operators")
	print("10 > 3 =", 10 > 3)
	print("10 == 3 =", 10 == 3)
	print("10 != 3 =", 10 != 3)
	print("10 >= 10 =", 10 >= 10)

	print("\nLogical operators")
	age = 20
	has_id = True
	print("age >= 18 and does has id =", age >= 18 and has_id)
	print("age < 18 or does has id =", age < 18 or has_id)
	print("not of has id =", not has_id)

	print("\nAssignment operators")
	score = 10
	print("score =", score)
	score += 5
	print("score += 5 ->", score)
	score *= 2
	print("score *= 2 ->", score)
	score -= 4
	print("score -= 4 ->", score)
	score //= 2
	print("score //= 2 ->", score)