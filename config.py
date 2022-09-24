import pygsheets

#Authorize with Google Sheets
gc = 0

#Current Sheet(Table)
sh = 0

#Current Page of Sheet(Table)
wks = 0

#Full table information [ ["Name" , "telegram-id" , "countlab_prog","colorcell_prog","isFirstPos_prog" , "countlab_opd","colorcell_opd","isFirstPos_opd" , "countlab_inf","colorcell_inf","isFirstPos_inf"] ]
tableData = []

#Current queue position: Prog, OPD, Inf
progPos = 0
opdPos = 0
infPos = 0

#Real table name
tableName = "Журнал Р3130"

#Table borders to synchronize
tableBorders = "B3:I23"

#Current count of students
studentsCount = 21
