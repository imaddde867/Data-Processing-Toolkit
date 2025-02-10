import json
import os

def count_occurrences(data, target_name):
    """Recursively counts the occurrences of a target name in a nested JSON structure."""
    count = 0
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, dict):
                count += count_occurrences(value, target_name)
            elif isinstance(value, list):
                for item in value:
                    count += count_occurrences(item, target_name)
            elif value == target_name:
                count +=1
    elif isinstance(data, list):
        for item in data:
            count += count_occurrences(item, target_name)
    return count

# Get the absolute path to the weather data file
weather_data_file = os.path.abspath('data_sources/weather-data.json')

try:
    with open(weather_data_file) as fh:
        data = json.load(fh)
        target_name = "KUITUVASTE_SUURI_1"
        occurrences = count_occurrences(data, target_name)
        #Prints the number of times the target name appears in the weather data JSON file.
        print(f'\n\n{target_name} has been measured {occurrences} times')
except FileNotFoundError:
    print(f"Error: {weather_data_file} not found.")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in {weather_data_file}")


# Get the absolute path to the todos data file
todos_data_file = os.path.abspath('data_sources/todos.json')

try:
    with open(todos_data_file) as tds:
        data = json.load(tds)
        #Using a more descriptive variable name
        tasks = data

        #Using a dictionary to store results, improving readability and maintainability
        results = {}
        results['keys'] = set() #Using a set to automatically handle unique keys
        results['completed_tasks'] = 0
        results['tasks_with_delectus'] = 0

        for task in tasks:
            for key, value in task.items():
                results['keys'].add(key)
                if key == 'completed' and value: #Simplified boolean check
                    results['completed_tasks'] += 1
                elif key == 'title' and 'delectus' in value:
                    results['tasks_with_delectus'] += 1

        keys = ' - '.join(results['keys'])
        #Prints a summary of the todos data, including unique keys, completed tasks, and tasks with "delectus" in the title.
        print(f'\n\nThe keys used in the dictionary : {keys}\nThe number of completed tasks : {results["completed_tasks"]}\nThe number of tasks with the word "delectus" in their title : {results["tasks_with_delectus"]}')
except FileNotFoundError:
    print(f"Error: {todos_data_file} not found.")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in {todos_data_file}")
