app_list = []
with open("app_list_env.txt", 'r') as f:
    for line in f:
        app = line.split()
        app_list.append(app)
print(app_list)

for app in app_list:
    print(app[0])
    print(app[1])

