import os
import sys


if __name__=='__main__':
    with open(sys.argv[1],'r') as f:
        lines = f.readlines()
        for line in lines:
            os.system("redis-cli lpush movie_links " + line)
