import math

# Nhập bán kính
r = float(input("Nhập bán kính r: "))

# Tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r**2

print(f"Chu vi hình tròn: {cv:.2f}")
print(f"Diện tích hình tròn: {dt:.2f}")
