def number_needed(a, b):
    a_cntr = {}
    b_cntr = {}
    deletions = 0

    for char in a:
        if char in a_cntr:
            a_cntr[char] += 1
        else:
            a_cntr[char] = 1

    for char in b:
        if char in b_cntr:
            b_cntr[char] += 1
        else:
            b_cntr[char] = 1

    for key in a_cntr:
        if key in b_cntr:
            deletions += abs(a_cntr[key] - b_cntr[key])
        else:
            deletions += a_cntr[key]

    for key in b_cntr:
        if key in a_cntr:
            deletions += abs(a_cntr[key] - b_cntr[key])
        else:
            deletions += b_cntr[key]

    return deletions

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print(number_needed(a, b))