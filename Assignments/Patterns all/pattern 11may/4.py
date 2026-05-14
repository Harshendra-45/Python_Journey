# 4) Vertical Diamond
#        *
#       * *
#      *   *
#     *     *
#      *   *
#       * *
#        *

n = int(input("Enter a number: "))
for i in range(1,n+1):
    a=n
    for j in range(1,2*n):
        prev = n+i-1
        next = n-i+1