def A000124(n):
    return n*(n+1)//2

def generate_sequence(length):
    sequence = []
    for i in range(1, length + 1):
        sequence.append(A000124(i))
    return sequence

def format_output(sequence):
    return '-'.join(map(str, sequence))

# Input panjang deret yang diinginkan
length = int(input("Masukkan panjang deret: "))

# Generate dan format output deret
result_sequence = generate_sequence(length)
output = format_output(result_sequence)

# Tampilkan hasil
print("Output:", output)