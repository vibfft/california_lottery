import random
import sys
from pprint import pprint


class Fantasy5(object):
    SIZE = 5
    ALL_NUMBERS = 39

    def __init__(self):
        self.winning_number = set()
        self.max_frequency = []

        # [{}]*Fantasy5.SIZE creates 5 hash elements with the same memory address
        # Hence you need to create the hashes (or lists) inside the list in the following manner
        self.list_of_hashes = [{} for hsh in range(Fantasy5.SIZE)]
        self.list_of_lists = [[] for lst in range(Fantasy5.SIZE)]

        # the final value of the range is always one less
        self.all_possible_list = [[i for i in range(1, Fantasy5.ALL_NUMBERS + 1, 1)]
                                  for lst in range(Fantasy5.SIZE)]

    def read_past_numbers(self, filename):
        f = None
        try:
            f = open(filename)
            for each_line in f:
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
            [self.list_of_lists[i].append(each_tuple[0])
                for j in range(each_tuple[1])]

    def populate_list_reverse_probability(self, number_hash, i):
        for each_tuple in number_hash.items():
            new_range = self.max_frequency[i] - each_tuple[1] + 1
            # frequency of each number occurrences are reversed
            # however you need to add 1 for the case of max frequency

            # add each unique number for number of numbers defined in new_range
            [self.list_of_lists[i].append(each_tuple[0])
                for j in range(new_range)]

            # remove from the all possible number values if it was already a winning
            # number previously
            self.all_possible_list[i].remove(int(each_tuple[0]))

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
        print("Usage: {0} winning_numbers.txt [average|chance]".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    strategy = sys.argv[2]

    f = Fantasy5()
    f.read_past_numbers(filename.strip())
    if strategy.strip() == 'average':
        for i, each_hash in enumerate(f.list_of_hashes):
            f.populate_each_list(each_hash, i)

    elif strategy.strip() == 'chance':
        for each_hash in f.list_of_hashes:
            f.max_frequency.append(max(each_hash.values()))
        for i, each_hash in enumerate(f.list_of_hashes):
            f.populate_list_reverse_probability(each_hash, i)

            # numbers which were not winning numbers previously are
            # added to the list pool where it can be randomly chosen
            # note that max_frequency number is added for those numbers which
            # were not previously winning numbers
            [f.list_of_lists[i].append(m)
             for n in range(f.max_frequency[i])
                for m in f.all_possible_list[i]]
    else:
        print("{0} is an invalid strategy type".format(strategy.strip()))
        sys.exit(1)

    for each_list in f.list_of_lists:
        f.generate_random_number(each_list)
    f.print_winning_number()


if __name__ == "__main__":
    main()
