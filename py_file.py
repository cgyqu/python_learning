import pickle, pprint


def read(path, model, data):
    f = open(path, model, encoding='utf-8')
    f.write(data)
    for line in f.readlines():
        print(line)
    f.close()


with open("./data/stopword.txt", "r+", encoding="utf-8") as outfile:
    print(outfile.readlines())

# read('./data/stopword.txt',"a+",'\ntest')
# print("=============================")
# read('./data/stopword.txt',"r+",'test1')

data = {"name": "cgymy", "age": 18, "remark": ('180', '1990')}

out = open('data.bat', "wb")
pickle.dump(data, out)
out.close()

d_file = open('data.bat', "rb")
data1 = pickle.load(d_file)
d_file.close()

print(data1)
pprint.pprint(data1)
