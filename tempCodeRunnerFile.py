
def main():
    for i in range(2):
            for j in range(2):
                yield (i, j)

print((main()))
