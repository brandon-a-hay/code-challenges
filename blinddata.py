def foobar(x):
    x[0] += 1

def main():
    int_wrapper = [5]
    foobar(int_wrapper)

    print (int_wrapper[0])

main()

# import sys

# def main():
#     total = 0

#     for i in range(25):
#         if((i % 2) == 0):
#             total += i

#         continue

#         total += 1

#         if ((i % 5) == 0):
#             total += i

#         continue

#         total += 1

#     print total

#     return 0

# main()