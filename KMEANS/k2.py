# Get user input for the dataset list
dataset_str = input("Enter the dataset as a list of numbers separated by commas: ")
dataset = []

# Split the input string by commas and convert to integers
for item in dataset_str.split(','):
    dataset.append(int(item))

# Enter the values of m1 and m2
m1 = int(input("Enter the initial m1: "))
m2 = int(input("Enter the initial m2: "))

avg1 = 0
avg2 = 0

p1 = 0
p2 = 0

while m1 != p2 and m2 != p2:
    j = 1
    k1 = []
    k2 = []
    for i in dataset:
        if abs(i - m1) < abs(i - m2):
            k1.append(i)
        else:
            k2.append(i)

    avg1 = sum(k1) / len(k1)
    avg2 = sum(k2) / len(k2)
    print("k{}    k{}".format(j, j + 1))
    print(k1, k2)
    p1 = m1
    p2 = m2
    m1 = avg1
    m2 = avg2

print("m1={}, m2={}".format(m1, m2))
