"""
Write a Javascript, Python, or OCaml program that:
-accepts a list of integers
-emits an error message if the list is not a multiple of 10 in length
-returns or prints a list of integers based on the input list,
  but with items at positions which are a multiple of 2 or 3 removed
"""


def main():
    print("Enter a list of integers separated by space")
    inp = input()
    inp = list(inp.split())

    if len(inp) % 10 != 0:
        print("Error: List is not a multiple of 10")
        return 1
    inp = list(map(int, inp))
    result = []

    for i in range(len(inp)):
        # skip positions that are multiples of 2 or 3
        if i % 2 == 0 or i % 3 == 0:
            continue
        result.append(inp[i])

    print(result)


if __name__ == "__main__":
    main()
