#coding=utf-8
import xlrd
import xlwt
def readExcel(path):
    workbook = xlrd.open_workbook(path)
    sheet=workbook.sheet_by_index(0)
    nrows=sheet.nrows
    ncols=sheet.ncols
    list=[]
    for i in range(1,nrows):
        row=sheet.row_values(i)
        list.append(row)
#         print row
    return list

def writeExcel(path,list):    
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet1')
    for i,row in enumerate(list):
        for j,cell in enumerate(row):
            sheet.write(i,j,cell)
#     sheet.write(0,1,'test text')#第0行第一列写入内容
    wbk.save(path)
    print '=====写入{path}成功====='.format(path=path)

if __name__=='__main__':
    print 1
#     list=readExcel('f:/autocode/11.xlsx')
#     print list
#     print list[1][2]
    writeExcel('f:/kkk.xlsx', [[1,2,3],['asdfsdf','asdasd']])
