import string
import random


def main():

    """# dictionary to store mapping pairs
    # column1 will be the key and column2 will be values
    dic = {}
    with open('mapping.txt', 'r') as map_file:
        maps = map_file.readlines()
    for i in maps:
        each_map = i.split(',')
        if each_map[0] in dic:
            dic[each_map[0]].append(each_map[1].strip())
        else:
            dic[each_map[0]] = [each_map[1].strip()]

    # read column1 file, separate them by comma and store into a list
    with open('column1.txt', 'r') as input_file:
        text = input_file.read()
    seqs = text.split(',')

    # replace the column1 sequences names by column2 sequence names
    used = {}  # dictionary to keep track of duplicated items
    for i, seq in enumerate(seqs):
        original_seq = seq.strip(string.punctuation)
        if original_seq in dic:
            while True:
                replace_seq = random.choice(dic[original_seq])
                dic[original_seq].remove(replace_seq)
                if replace_seq not in used:
                    used[replace_seq] = 1
                    break
                if not dic[original_seq]:
                    used[replace_seq] += 1
                    replace_seq += f'_{used[replace_seq]}'
                    break
            seqs[i] = seq.replace(original_seq, replace_seq)
        else:
            print(f'{original_seq} Not exist')

    return ','.join(seqs)"""

    # dictionary to store mapping pairs
    # column1 will be the key and column2 will be values
    dic = {}
    with open('mapping.txt', 'r') as map_file:
        maps = map_file.readlines()
    for i in maps:
        each_map = i.split(',')
        if each_map[1].strip() in dic:
            dic[each_map[1].strip()].append(each_map[0])
        else:
            dic[each_map[1].strip()] = [each_map[0]]

    # read column1 file, separate them by comma and store into a list
    with open('column2.txt', 'r') as input_file:
        text = input_file.read()
    seqs = text.split(',')

    # replace the column1 sequences names by column2 sequence names
    used = {}  # dictionary to keep track of duplicated items
    for i, seq in enumerate(seqs):
        original_seq = seq.strip(string.punctuation)
        if original_seq in dic:
            while True:
                replace_seq = random.choice(dic[original_seq])
                dic[original_seq].remove(replace_seq)
                if replace_seq not in used:
                    used[replace_seq] = 1
                    break
                if not dic[original_seq]:
                    used[replace_seq] += 1
                    replace_seq += f'_{used[replace_seq]}'
                    break
            seqs[i] = seq.replace(original_seq, replace_seq)
        else:
            print(f'{original_seq} Not exist')

    return ','.join(seqs)


if __name__ == '__main__':
    with open('../../Desktop/CS180_research/column2_renamed_tree.nwk', 'w', encoding='utf-8') as new_file:
        new_file.write(main())
