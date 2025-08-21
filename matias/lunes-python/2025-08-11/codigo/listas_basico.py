# Listas: mutabilidad y operaciones básicas
nums = [1, 2, 3]
print("Inicial:", nums)

nums.append(4)                 # agrega al final
nums.insert(1, 99)             # inserta en índice 1
print("Después de append/insert:", nums)

ultimo = nums.pop()            # quita y devuelve el último
print("Pop ->", ultimo, "Quedó:", nums)

# slicing
print("Slice [1:3]:", nums[1:3])

# recorrer
for n in nums:
    print("n:", n)
