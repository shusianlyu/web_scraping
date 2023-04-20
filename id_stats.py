from collections import Counter
import string
COG = 'COG'
PFAM = 'pfam'


def main():
    file = '/Users/jessielu/Desktop/CS180_research/pruned_column2_renamed.tsv'
    file2 = '/Users/jessielu/Desktop/CS180_research/pruned_column1.tsv'
    with open(file) as input_file:
        lines = input_file.readlines()
        #print(lines)

    cog_cluster = {}
    pfam_cluster = {}
    cog_overall = {}
    pfam_overall = {}
    more_than_one_cog = {}
    more_than_one_pfam = {}

    for line in lines:
        columns = line.split('\t')
        for column in columns:
            if column.startswith(COG):
                cog_cluster[column] = cog_cluster.get(column, 0) + 1
            if column.startswith(PFAM):
                pfam_cluster[column] = pfam_cluster.get(column, 0) + 1
        cog_overall = Counter(cog_overall) + Counter(cog_cluster)
        pfam_overall = Counter(pfam_overall) + Counter(pfam_cluster)

        for key, value in cog_cluster.items():
            if value > 1:
                print(f"{key}: {value}")
                more_than_one_cog[key] = value

        for key, value in pfam_cluster.items():
            if value > 1:
                print(f"{key}: {value}")
                more_than_one_pfam[key] = value

        #print(cog_cluster)
        #print(pfam_cluster)
        cog_cluster.clear()
        pfam_cluster.clear()

    """print(cog_overall)
    print(pfam_overall)
    print(more_than_one_cog)
    print(more_than_one_pfam)"""

    print('{:<12}  {:<12}  {:<12}'.format("cog_id", "count_in_one_cluster",
                                          "count_over_all_clusters"))
    for cog in cog_overall.keys():
        if cog in more_than_one_cog.keys():
            print('{:20}  {:<20}  {:<12}'.format(cog[:7], more_than_one_cog[
                cog], cog_overall[cog]))
        else:
            print('{:<20}  {:<20}  {:<12}'.format(cog[:7], 1, cog_overall[
                cog]))

    print()
    print('{:<12}  {:<12}  {:<12}'.format("pfam_id", "count_in_one_cluster",
                                          "count_over_all_clusters"))
    for pfam in pfam_overall.keys():
        if pfam in more_than_one_pfam.keys():
            print('{:20}  {:<20}  {:<12}'.format(pfam[:7], more_than_one_pfam[
                pfam], pfam_overall[pfam]))
        else:
            print('{:<20}  {:<20}  {:<12}'.format(pfam[:7], 1, pfam_overall[
                pfam]))


if __name__ == '__main__':
    main()
