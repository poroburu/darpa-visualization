import sys


def main(i):
    with open('Data/train.txt', 'a') as trainFile:
        f = open('Data/trainset/graph_' + str(i), 'r')
        trainFile.write(f.read())


# for line in f:
#	print(line)
# for i in range(0,31):
# print()
if __name__ == '__main__':
    main(sys.argv[1])