#Functions Go Here
def make_statement(statement, decoration):
   """Emphasizes headings by adding decoration
      at the start and the end"""
   
   print(f"{decoration * 3} {statement} {decoration * 3}")

#Main Routine Goes Here
statement = 'Instructions'
decoration = ' ℹ️ '

make_statement(statement, decoration)
#This Program Was Created 3/10/2025