
filename = "output.txt"

text = input("Dosyaya yazılacak metni girin: ")
with open(filename, 'w') as file:
    file.write(text)


with open(filename, 'r') as file:
    content = file.read()
    print("\nDosya içeriği:")
    print(content)

with open(filename, 'w') as file:
    for i in range(5):
        line = input(f"{i + 1}. satırı girin: ")
        file.write(line + '\n')

with open(filename, 'r') as file:
    print("\nDosyadaki 5 satır veri:")
    for line in file:
        print(line.strip())
