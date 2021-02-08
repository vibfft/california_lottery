import random
import sys
from pprint import pprint


class Fantasy5(object):
    SIZE = 5

    def __init__(self):
        self.winning_number = set()

        # [{}]*Fantasy5.SIZE creates 5 hash elements with the same memory address
        # Hence you need to create the hashes (or lists) inside the list in the following manner
        self.list_of_hashes = [{} for h in range(Fantasy5.SIZE)]
        self.list_of_lists = [[] for lst in range(Fantasy5.SIZE)]

    def read_past_numbers(self, filename):
        f = None
        try:
            f = open(filename)
            for j, each_line in enumerate(f):
                num = each_line.split()
                for i in range(len(num)):
                    if num[i] not in self.list_of_hashes[i]:
                        self.list_of_hashes[i][num[i]] = 1
                    elif num[i] in self.list_of_hashes[i]:
                        self.list_of_hashes[i][num[i]] += 1

        except IOError as io:
            print(io)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def populate_each_list(self, number_hash, i):
        for each_tuple in number_hash.items():  # ('1',7)
            [self.list_of_lists[i].append(each_tuple[0]) for j in range(each_tuple[1])]

    def generate_random_number(self, frequency_list):
        pick = random.randint(0, len(frequency_list) - 1)
        while int(frequency_list[pick]) in self.winning_number:  # winning_numbers are integers
            pick = random.randint(0, len(frequency_list) - 1)

        self.winning_number.add(int(frequency_list[pick]))

    def print_winning_number(self):
        for i in sorted(self.winning_number):
            print(i, end=" ")
        print()


def main():
    if len(sys.argv) != 3:
        print("Usage: {0} winning_numbers.txt [avg|chance]")
        sys.exit(1)

    filename = sys.argv[1]
    strategy = sys.argv[2]

    f = Fantasy5()
    f.read_past_numbers(filename.strip())
    if strategy.strip() == 'avg':
        for i, each_hash in enumerate(f.list_of_hashes):
            f.populate_each_list(each_hash, i)

    elif strategy.strip() == 'chance':
        pass
    else:
        print("{0} is an invalid strategy type".format(strategy.strip()))
        sys.exit(1)
    for each_list in f.list_of_lists:
        f.generate_random_number(each_list)

    f.print_winning_number()


if __name__ == "__main__":
    main()
