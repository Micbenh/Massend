import json

with open("Massend\\data.json", mode="r+", encoding="utf-8") as j:
    json_file = json.load(j)
    print(json_file.keys())
    dist = json_file['groups']
    for i in dist:
        i = i.encode("utf-8").decode("UTF-8", errors="replace")
        print(i)


