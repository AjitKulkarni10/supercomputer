import memory
import processor
import loader
import sys
from loguru import logger

def main():
    # Create a new memory
    mem = memory.LinearMemory(16)

    # Load instructions to memory
    if len(sys.argv) > 1:
        logger.info(f"Loading {sys.argv[1]} into memory")
        loader.SimpleLoader(sys.argv[1], mem, offset=0)
    else:
        logger.info("No machine code specified to be loaded")

    # Show memory state before execution
    mem.show()

    # Start executing instructions using the processor
    processor.SuperSimpleComputer(mem)

    # Show memory state after execution
    mem.show()



if __name__ == "__main__":
    main()

    #  s             s            s            s           s           s           s            s         
    #  [1, 29, 3, 3, 1, 30, 2, 3, 2, 31, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, -2]
    #   0  1   2  3  4   5  6  7  8  9   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31