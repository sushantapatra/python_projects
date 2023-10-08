"""
how to know builtin module list in python
"""
import sys
# Get a dictionary of all loaded modules
built_in_modules = sys.modules

# Extract the module names
module_names = list(built_in_modules.keys())

# Print the list of built-in module names
for module_name in module_names:
    print(module_name)
