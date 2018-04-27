from random import choice
import argparse

parser = argparse.ArgumentParser(description='random alignment')

parser.add_argument('-s', dest="lenSeq", type=int)
parser.add_argument('-n', dest="numSeq", type=int)

args = parser.parse_args()
w = open("pa2_2.txt", "w")

def rnd(length, number):
    a = 0
    g = 0
    t = 0
    c = 0
    for x in range(number):
        seq = ''

        #<---to check which number sequece it is-->
        #print("seq #:" + str(x+1))
        for i in range(length):
            output = choice(['G', 'C', 'T', 'A'])
            seq += output
            if(output == 'G'):
                g += 1
            if (output == 'C'):
                c += 1
            if (output == 'T'):
                t += 1
            if (output == 'A'):
                a += 1
        print(seq)
        w.write(seq + '\n')

    print('G= ' + str(g/len(seq)) + '\n'
        + 'C= ' + str(c/len(seq)) + '\n'
        + 'T= ' + str(t/len(seq)) + '\n'
        + 'A= ' + str(a / len(seq)) + '\n')
    w.write('G= ' + str(g / len(seq)) + '\n'
            + 'C= ' + str(c / len(seq)) + '\n'
            + 'T= ' + str(t / len(seq)) + '\n'
            + 'A= ' + str(a / len(seq)) + '\n')
            #print('C= ' + str(c/len(seq)))
            #print('T= ' + str(t/len(seq)))
            #print('A= ' + str(a/len(seq)))


    print('seq len = ' + str(len(seq)) + '\n')
'''
        w.write("seq #:" + str(x + 1) + '\n')
        w.write(seq + '\n')
        w.write('G= ' + str(g/len(seq)) + '\n'
                  + 'C= ' + str(c/len(seq)) + '\n'
                  + 'T= ' + str(t/len(seq)) + '\n'
                  + 'A= ' + str(a / len(seq)) + '\n')
        w.write('seq len = ' + str(len(seq)) +'\n' + '\n')
'''

rnd(args.lenSeq, args.numSeq)
#rnd(1000, 1000)
