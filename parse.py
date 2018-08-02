#coding=utf-8
import xlrd

data = xlrd.open_workbook('tmp001.xlsx')
table = data.sheets()[0]
# print(data.sheet_names())
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
# print(nrows)
# colnames = table.row_values(3)  # 某一行数据
list = []
zd_guid = ''
txt = 'Polygon\n'
jzdh = 0
for rownum in range(1, nrows):
    row = table.row_values(rownum)

    if(zd_guid!=row[1]):#判断zd_guid是否与该行记录的第二列一致，如果不一致，说明是该地块的首行
        zd_guid = row[1]
        jzdh = rownum
        txt = txt + str(int(row[0]))+' 0'+'\n'
        rowdata = str(rownum-jzdh) + ' ' + row[2]#每个地块序号重0开始取
        txt = txt + rowdata +'\n'
    else:
        rowdata = str(rownum-jzdh) + ' ' + row[2]
        txt = txt + rowdata +'\n'
txt = txt + 'END'
filename = 'write_data.txt'
with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write(txt)










