import sys

def main(args):
    count = False
    sort = False
    num = False
    while args:
        arg = args.pop(0)
        if arg == "--count":
            count = True
        elif arg == "--num":
            num = True
        elif arg == "--sort":
            sort = True
        else:
            try:
                f = open(arg,"r")
            except:
                print("ERROR")
                return
    return f, count, num, sort


file, count, num, sort = main(sys.argv[1:])
res = file.readlines()
res[-1] = res[-1] + "\n"
#res = list(map(lambda x:x.replace("\n",""),res))
#print(res)
if sort:
    res.sort()
if num:
    for i in range(len(res)):
        res[i] = f"{i} {res[i]}"

print(*res)
if count:
    print(f"rows count: {len(res)}")