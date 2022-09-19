import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            except IndexError:
                print('이름, 나이, 성적을 정확히 입력하시오.')
            else:
                scdb += [record]
        # 명령어 add 뒤에 필요한 정보를 전부 입력하지 않았을 때 발생하는 IndexError 처리
        # 이름, 나이, 성적 중 일부 또는 전부가 공백인 경우를 허용함

        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
            

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        # Age, Score를 기준으로 정렬할 때 발생하는 TypeError 처리
        # 명령어 show 뒤에 올바르지 않은 정렬 기준을 입력할 때 발생하는 KeyError 처리

        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    for attr in sorted(p):
                        print(attr + "=" + str(p[attr]), end=' ')
                    print()

        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    try:
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')
            print()
    except TypeError:
        for p in sorted(scdb, key=lambda person: int(person[keyname])):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')
            print()
    except KeyError:
        print('정렬 기준을 정확히 입력하시오.')
    


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
