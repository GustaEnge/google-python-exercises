import sys
import re
import os
import shutil
import biblio_special as bs


class FileHandler:
  method = ""
  commands = ""
  current_path = ""
  def __init__(self,instruction):
    self.instruction = instruction
    self.splitInstruction(instruction)
    self.current_path,self.method,self.commands = self.splitInstruction(instruction)
    
    
  def splitInstruction(self,args):
    
    current_path = args[0]
    commands = args[1:]
    if len(commands) < 1:
      raise Exception("Error: must specify one or more dirs")
    else:
      method = args[1]
      path = args[2:]
      return (current_path,method,path)

  def action(self):
    bs.methodHandler(os.path.dirname(os.path.abspath(self.current_path))+"\\",self.method,self.commands)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv
  fileHandler = FileHandler(args)
  fileHandler.action()
  
if __name__ == "__main__":
  main()
