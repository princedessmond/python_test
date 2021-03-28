import json


with open('/home/cyberguy/Documents/AI_ML_DL/deeper_test/source_file_2.json', 'r') as f:
    data = json.load(f)
    sorted_data = sorted(data, key=lambda project: project.get('priority'))

    watchers = managers = {}
    for project in sorted_data:
        project_name = project.get('name')
        for manager in project.get('managers'):
            if not managers.get(manager):
                managers[manager] = []
            managers[manager].append(project_name)
        for watcher in project.get('watchers'):
            if not watchers.get(watcher):
                watchers[watcher] = []
            watchers[watcher].append(project_name)

with open("managers.json", "w") as managers_file:
    json.dump(managers, managers_file)

with open("watchers.json", "w") as watchers_file:
    json.dump(watchers, watchers_file)
