import os

current_directory = os.getcwd()
print(f'#1\n\nCurrent working directory :\n{current_directory}')

try:
    os.chdir("data_sources")
    new_directory = os.getcwd() # Get the new directory after changing
    contents = os.listdir(new_directory) # List contents of the NEW directory
    print(f'\nThe contents of the new directory :\n{contents}\n')
except FileNotFoundError:
    print("\nError: 'data_sources' directory not found.")
except OSError as e:
    print(f"\nAn error occurred: {e}")
