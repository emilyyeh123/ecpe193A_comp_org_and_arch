'''
PROJECT 5: PYTHON CACHE SIMULATOR
Write a Python program cache.py to simulate reading a direct-mapped cache or an n-way set associative cache.
In this simulator, we are only interested in hits and misses, not in the word values being read.
This program simulates the cache behavior (using the cache scheme selected by the user) for a sequence of memory accesses of 4-byte words, using 32-bit memory addresses.

COMMAND TO RUN THIS PROGRAM: 
python3 cache.py --type=d --cache_size=256 --block_size=64 --memfile=mem1.txt

*Valid Types:
> "d" for direct-mapped cache
> "s" for set associative cache
    > must have additional "--nway" parameter specifying number of ways

*Cache size is total cache size in bytes and MUST be a power of 2 (size does not include valid & tag bits)

*Block size is size of a block in bytes and MUST be a power of 2 (size does not include valid and tag bits)

*memfile is the input text file containing the sequence of memory accesses where each line is a memory address in hexadecimal
'''

import argparse

def main():
    parser = argparse.ArgumentParser(description = "Project 5: Python Cache Simulator")
    parser.add_argument("--type", required = True, help = "Valid Cache Types: d for direct-mapped and s for set associative")
    parser.add_argument("--nway", required = False, help = "specify number of ways if set associative cache")
    parser.add_argument("--cache_size", required = True, help = "cache size in bytes, must be power of 2 (does not include valid & tag bits)")
    parser.add_argument("--block_size", required = True, help = "block size in bytes, must be power of 2 (does not include valid & tag bits)")
    parser.add_argument("--memfile", required = True, help = "txt file containing sequence of memory accesses where each line is a memory address in hexadecimal")
    args = parser.parse_args()

    # program must first verify if an input configuration is possible based on cache type
    # return an error and exit program if invalid input arguments
    if args.type == "d" and args.nway is not None:
        print("INVALID ARGUMENTS! Direct-Mapped cache should not have nway argument.")
        exit()
    elif args.type == "s":
        try:
            # if nway argument can convert to int, argument is valid
            int(args.nway)
        except:
            print("INVALID ARGUMENTS! Set Associative cache should have an integer-type nway argument.")
            exit()

    # test if number is power of 2:
    # power of 2 if binary value has only one 1

if __name__ == "__main__":
    main()