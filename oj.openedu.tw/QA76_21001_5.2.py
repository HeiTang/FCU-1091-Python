def checkSSN(ssn): # 此行勿改
    ENG = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','X','Y','W','Z','I','O']
    NUM = ['10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35']
    Index = ENG.index(ssn[0])
    ssn = ssn.replace(ssn[0],NUM[Index])
    SUM = int(ssn[0])*1 + int(ssn[1])*9 + int(ssn[2])*8 + int(ssn[3])*7 + int(ssn[4])*6 + int(ssn[5])*5 + int(ssn[6])*4 + int(ssn[7])*3 + int(ssn[8])*2 + int(ssn[9])*1 + int(ssn[10])*1
    if(SUM % 10 == 0): 
        return 'T'
    else: 
        return 'F'

ssn = input('')
r = checkSSN(ssn)
print(r)             # 此行勿改