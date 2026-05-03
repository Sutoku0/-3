# База разрешенных ID
base_line = "10 20 30"
incoming_line = "20 40 10 50"

base_ids = set(base_line.split())
incoming_ids = incoming_line.split()

for id in incoming_ids:
    if id in base_ids:
        print("OK")
    else:
        print("ADDED")
        base_ids.add(id)