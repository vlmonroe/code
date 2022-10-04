import json
data_again = json.loads(input())
P_CH = {}
for i in data_again:
    P_CH[i.get("name")] = []
for i in data_again:
    for j in i.get("parents"):
        P_CH[j].append(i.get("name"))
def rec(k, v):
    for i in v:
        s = P_CH.get(i)
        if s != []:
            P_CH[k] = list(set(P_CH.get(k) + s))
            rec(k, s)
for k, v in P_CH.items():
    rec(k, v)
for k, v in sorted(P_CH.items()):
    print(k, ":", len(v)+1)