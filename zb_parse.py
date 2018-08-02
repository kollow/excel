#coding=utf-8
import xlrd
import os
def parse(basepath,excelfile):
    # basepath = 'C:/Users/kollow/Desktop/2017/'
    # excelfile = '2017-1.xls'
    filepath = basepath+excelfile
    print(filepath)
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    # print(data.sheet_names())
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    rfilename = os.path.splitext(excelfile)[0].replace('-','')
    print(rfilename)
    # print(nrows)
    # colnames = table.row_values(3)  # 某一行数据
    txt = rfilename + ' 0\n'
    jzdh = -1
    for rownum in range(1, nrows):
        row = table.row_values(rownum)

        if(rownum > 4):#判断要取的数据从第6行开始

            jzdh = jzdh +1
            x = row[3]
            y = row[2]
            z = '1.#QNAN 1.#QNAN'
            txt = txt + str(jzdh) + ' ' + str(x) + ' ' + str(y) + ' ' + z +'\n'
    # print(txt)
    return txt
# 最终生成样式如下：
# 1 0
# 0 40466794.57 3474342.341 1.#QNAN 1.#QNAN
# 1 40466984.22 3474321.522 1.#QNAN 1.#QNAN
# 2 40466966.32 3474164.48 1.#QNAN 1.#QNAN
# 3 40466776.43 3474185.616 1.#QNAN 1.#QNAN
# 4 40466794.57 3474342.341 1.#QNAN 1.#QNAN




def file(file_dir):
    all_txt = 'Polygon\n'
    whitelist = ['xls','XLS','XLSX','xlsx']
    log_txt = ''
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        filepath = file_dir + '\\'
        for file in files:
            ext = file.split('.')[-1]
            try:
                if ext in whitelist:
                    single_txt = parse(file_dir+ '\\',file)
                    all_txt = all_txt + single_txt
            except AssertionError as e:
                log_txt = log_txt + file + ' 失败！\n'

    if log_txt == '':
        log_txt = '全部执行成功！'
    txt = all_txt + 'END'
    filename = file_dir + '\write_data.txt'
    errorfile = file_dir + '\error.txt'
    re = (txt,log_txt)
    with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write(txt)
    with open(errorfile, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write(log_txt)
    return re

if __name__ == "__main__":
    file(r'C:\Users\kollow\Desktop\2017')