with open("history.txt", "r") as file:
    commands = file.readlines()

counts = {}

for i in commands:
    parts = i.strip().split()

    if not parts:
        continue

    cmd = parts[1]

    if cmd in counts:
        counts[cmd] += 1
    else:
        counts[cmd] = 1

if counts:
    max_count = max(counts.values())

    for i in counts:
        if counts[i] == max_count:
            most_used_command = i
            break

    print("The most used command is:", most_used_command)
    print("Number of uses:", max_count)
else:
    print("No commands found.")

print("Total number of commands:", len(commands))

for i in counts:
    print(i,":" , counts[i])