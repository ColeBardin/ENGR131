'''
D R E X E L   U N I V E R S I T Y
ENGR 131 -- Introductory Programming for Engineers

A PDB-file record counter

Written by Cole Bardin
Term:  Winter 2020-2021
'''

def get_record_counts(pbd_file):
    mylist = []
    count_dict = {}
    total_headers = ''
    with open(pbd_file, 'r') as f:
        lines = f.readlines()
        for ln in lines:
            total_headers += ln[0:6]
            if ln[:6] not in mylist:
                mylist.append(ln[:6])
        for n in mylist:
            count = total_headers.count(n)
            count_dict[n] = count
    return(count_dict)

if __name__ == '__main__':
    pdb_file = input()
    records_counts_dict = get_record_counts(pdb_file)
    print(pdb_file, 'has the following record counts:')
    for k, v in records_counts_dict.items():
        print('{:s}: {:d}'.format(k, v))
