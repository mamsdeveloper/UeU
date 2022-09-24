import pygsheets
import config as c

def initSheets(name,authorizeCode):
    #Mandatory initialization and binding to the table. As authorizeCode, use the path to the file "client_secret_669931596690-pf5htcd4nv7735n1ocbbf41udi24r60g.apps.googleusercontent.com.json"
    c.gc = pygsheets.authorize(authorizeCode);
    c.sh = c.gc.open(name)
    c.wks = c.sh.sheet1;

def synchSheets(tabs):
    #Adding data from a table to an array. Return ["Name" , "telegram-id" , "countlab_prog","colorcell_prog","isFirstPos_prog" , "countlab_opd","colorcell_opd","isFirstPos_opd" , "countlab_inf","colorcell_inf","isFirstPos_inf"]
    #It's important to synchronize data often, because changing the background color of the cell removes you from queue
    rawData = c.wks.range(tabs)
    nrmData =[]
    for it in rawData:
        nrmData.append([it[0].value,it[7].value,  it[1].value,it[2].color,it[2].value,  it[3].value,it[4].color,it[4].value,  it[5].value,it[6].color,it[6].value])
    prog,opd,inf = False, False, False
    counter = 0 
    for i in nrmData:
        if(i[4]=="<" and not prog):
            prog=True
            c.progPos=counter
        else:
            i[4]=""
        if(i[7]=="<" and not opd):
            opd=True
            c.opdPos=counter
        else:
            i[7]=""
        if(i[10]=="<" and not inf):
            inf=True
            c.infPos=counter
        else:
            i[10]=""
        counter+=1

    if(not prog):
        nrmData[0][4]="<"
        c.progPos=0
    if(not opd):
        nrmData[0][7]="<"
        c.opdPos=0
    if(not inf):
        nrmData[0][10]="<"
        c.infPos=0
    c.tableData = nrmData

def whoIsNext(currpos, discipline):
    #Return the next ready person's iterator from tableData
    nextIs = 0
    if(discipline == "prog"):
        nextIs = (currpos+1) %  c.studentsCount
        while(not c.tableData[nextIs][3] in [(None,None,None,None),(1,1,1,0)]):
            nextIs = (nextIs+1) % c.studentsCount
    elif(discipline == "opd"):
        nextIs = (currpos+1) %  c.studentsCount
        while(not c.tableData[nextIs][6] in [(None,None,None,None),(1,1,1,0)]):
            nextIs = (nextIs+1) % c.studentsCount
    elif(discipline == "inf"):
        nextIs = (currpos+1) %  c.studentsCount
        while(not c.tableData[nextIs][9] in [(None,None,None,None),(1,1,1,0)]):
            nextIs = (nextIs+1) % c.studentsCount
    return nextIs

def nextPerson(discipline):
    #Return 3 next persons from tableData with full information about them(the first [] is about next person)
    #[ ["Name","telegram-id",...], ["Name","telegram-id",...], ["Name","telegram-id",...]]
    currpos = 0
    if(discipline == "prog"):
        currpos = c.progPos
        c.progPos = whoIsNext(currpos,"prog")
        c.tableData[currpos][4]=""
        c.tableData[c.progPos][4]="<"
        c.wks.update_value((3+currpos,4),"")
        c.wks.update_value((3+c.progPos,4),"<")
        return [c.tableData[c.progPos],c.tableData[whoIsNext(c.progPos,"prog")],c.tableData[whoIsNext(whoIsNext(c.progPos,"prog"),"prog")]]
    elif(discipline == "opd"):
        currpos = c.opdPos
        c.opdPos = whoIsNext(currpos,"opd")
        c.tableData[currpos][7]=""
        c.tableData[c.opdPos][7]="<"
        c.wks.update_value((3+currpos,6),"")
        c.wks.update_value((3+c.opdPos,6),"<")
        return [c.tableData[c.opdPos],c.tableData[whoIsNext(c.opdPos,"opd")],c.tableData[whoIsNext(whoIsNext(c.opdPos,"opd"),"opd")]]
    elif(discipline == "inf"):
        currpos = c.infPos
        c.infPos = whoIsNext(currpos,"inf")
        c.tableData[currpos][10]=""
        c.tableData[c.infPos][10]="<"
        c.wks.update_value((3+currpos,8),"")
        c.wks.update_value((3+c.infPos,8),"<")
        return [c.tableData[c.infPos],c.tableData[whoIsNext(c.infPos,"inf")],c.tableData[whoIsNext(whoIsNext(c.infPos,"inf"),"inf")]]
