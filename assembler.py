import sys
import json
from loguru import logger

OPCODE_LOOKUP_TABLE = {
    "add": 1,
    "sub": 2
}

class SimpleAssembler:

    def __init__(self, source_file):
        # Read all chars from source file
        self.source_file = source_file.read()
        
        # List of all the instructions in the source file
        self.instructions = self.source_file.split("\n")

        machine_code = []
        for instruction in self.instructions:
            result = self.parse(instruction)
            machine_code.extend(result)
        
        # if not present ,will create automatically
        with open("output.ssmc", "w") as output_file:
            json.dump(machine_code, output_file)
        
        logger.success("Machine code generated and saved in output.ssmc")
        
        
    
    def parse(self, instruction):
        instruction = instruction.strip()
        instruction_token = instruction.split(" ")
        
        operation = instruction_token[0]
        logger.info(f"Generating code for {operation} instruction")
        opcode = OPCODE_LOOKUP_TABLE[operation]

        dest = int(instruction_token[1])
        op1 = int(instruction_token[2])
        op2 = int(instruction_token[3])
        
        return [opcode, dest, op1, op2]
        


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        with open("prg1.ssa", "r") as source_file:
            SimpleAssembler(source_file)
    
    else:
        logger.error("Pass the name of the source file")
    