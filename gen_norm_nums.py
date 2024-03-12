import random
from statistics import *



def gen_norm_nums(fileName, size, mu, sd):
    
    vs = [random.gauss(mu = mu, sigma = sd) for i in range(size)]
    dictvs = {"size": size, "Mean": [mu, mean(vs)], "Stddev": [sd, stdev(vs)]}
    with open (file= fileName, mode="w") as f:
        f.write(str(dictvs))
    print(dictvs)


if __name__ == "__main__": 
    import sys
    gen_norm_nums(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))