# 8-15. Printing Models: Put the functions for the example printing_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.
import printing_functions

unprinted_designs = ['car', 'plane', 'train']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
