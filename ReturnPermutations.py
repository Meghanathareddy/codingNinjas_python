
def get_permutations(string):
    # Base case: if the string is empty, return an empty list
    if len(string) == 0:
        return []

    # Base case: if the string has only one character, return a list containing that character
    if len(string) == 1:
        return [string]

    # Recursive case: generate all permutations of the string by inserting the first character in all positions
    permutations = []
    for permutation in get_permutations(string[1:]):
        for i in range(len(permutation)+1):
            permutations.append(permutation[:i] + string[0] + permutation[i:])

    # Return the list of permutations
    return permutations

a = get_permutations(input())
print(*a)