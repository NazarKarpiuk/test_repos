with open('proj_logs.log', 'r') as fin:
    print("[LAST FIVE LOG RECORDS]")
    for line in (fin.readlines()[-5:]):
        print(line, end='')