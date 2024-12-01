n = int(input())
ds = []
ds = list(map(int, input().split()))
tong = 0
tbc = 0
for i in range(0,n):
    if ds[i] % 2 != 0:
        tong += ds[i]
        tbc += 1
print("{:.4f}".format(tong/tbc))