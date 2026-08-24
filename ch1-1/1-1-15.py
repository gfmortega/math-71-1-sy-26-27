n = int(input())

boxes = n // 12
individual = n % 12 
total_cost = boxes*8 + individual*1

print(f"boxes: {boxes}")
print(f"individual donuts: {individual}")
print(f"total cost: ${total_cost}")