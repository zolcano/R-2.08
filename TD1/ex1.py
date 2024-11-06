import sys
if __name__ == '__main__':
    if len(sys.argv)==1:
        print(f"{sys.argv[0]} attend au moins un argument")
    else:
        for i in range(len(sys.argv)):
            print(sys.argv[i])