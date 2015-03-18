import read_post
file_name = "Rising10.txt"
tfile = open("Taylor/"+file_name)
jfile = open("Jeremy/"+file_name)
ofile = open("Out/"+file_name,'wt')
t_bt = 0
t_pos = 0
line = tfile.readline()
while line:
    last = line
    ofile.write(line)
    bt = read_post.read_post(line)["batch_time"]
    if bt > t_bt:
        t_bt = bt
        t_pos = tfile.tell()
        print(bt)
    line = tfile.readline()
#tfile.seek(t_pos)
tfile.seek(0)
list_id = []
for line in tfile:
    list_id.append(read_post.read_post(line)["id"])
#list_id = list_id[:100]
list_id = []
print("here")
for line in jfile:
    r = read_post.read_post(line)
    if r["batch_time"] < t_bt:
        continue
    if r["id"] in list_id:
        continue
    ofile.write(line)

tfile.close()
jfile.close()
ofile.close()
