# syntactic parsing
import requests
import subprocess
import re
import os

def synparse(item, data_dir, neg_list, parser):
    # preparing sentence for parsing
    l = []
    sl = []
    l.append(item)
    sl.append(item)

    # remove before/after words!
    ll = []
    for ss in l:
        s = ''
        flag = ''
        for nw in sorted(neg_list['ITEM'].tolist(), key=len, reverse=True):
            if nw in neg_list[neg_list['EN (SV) ACTION'] == 'forward']['ITEM'].tolist():
                try:
                    s = ss[ss.index(nw):]
                    flag = 'f'
                    break
                except:
                    continue
            else:
                try:
                    s = ss[:(ss.index(nw)+len(nw))]
                    flag = 'b'
                    break
                except:
                    continue
        ll.append(s)

    tree_list = []

    while len(sl) != len(tree_list):
    # corenlp parsing the neg tree
        #print('\n--- parse negated part of the sentence ---\n')
        tree_list = []
        with open(data_dir + 'tmp_neg_tree', 'wb') as fw:
            #print(ll)       
            for i, s in enumerate(ll):
                if s != '':
                    t = (next(parser.raw_parse(s)))
                    #fw.write(str(t))
                    fw.write(str(t).encode('utf8'))
                    #fw.write(str(t.decode()))
                    fw.write(b'\n')
                    tree_list.append(t)
    # print(len(sl))
    # print(len(tree_list))

    return sl, tree_list, ll

def tregex_tsurgeon(f, pos, trts):
    cmd = trts[pos][0] + '\n\n' + trts[pos][1].replace(',', '\n')
    with open('C:/Users/SuresMal/Documents/GitHub/task-vt/negation_detection/data/stanford-tregex-2018-02-27/ts', 'w') as fw:     
        fw.write(cmd)
    tree = subprocess.check_output(["C:/Users/SuresMal/App/cygwin/bin/sh", "tsurgeon.sh", "-treeFile", "C:/Users/SuresMal/Documents/GitHub/task-vt/negation_detection/data/tmp_neg_tree", "ts"], cwd="C:/Users/SuresMal/Documents/GitHub/task-vt/negation_detection/data/stanford-tregex-2018-02-27")
    output = subprocess.check_output(["C:/Users/SuresMal/App/cygwin/bin/sh", "tsurgeon.sh", "-treeFile", "C:/Users/SuresMal/Documents/GitHub/task-vt/negation_detection/data/tmp_neg_tree", "ts", "-s"], cwd="C:/Users/SuresMal/Documents/GitHub/clneg/src/stanford-tregex-2018-02-27")
    #print('constituency tree: ' + str(output).replace('\n', ''))
    ts_out = re.sub('\([A-Z]*\$? |\(-[A-Z]+- |\)|\)|\(, |\(. |\n', '', str(output))
    ts_out = re.sub('-LRB-', '(', ts_out)
    ts_out = re.sub('-RRB-', ')', ts_out)
    os.system("rm stanford-tregex-2018-02-27/ts")
    return ts_out, str(tree)

