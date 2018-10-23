
# _*_ coding:utf_8 _*_
import xml.etree.ElementTree as ET
import re
import os

# filePath ='d:/1/32028217250000000.xml'


# tree = ET.parse(filePath)

FROM_BPJ_NO = ''
def getOutPutFolder(path,fo):
    path = path + '/'+fo
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    return path


def takeSecond(elem):
    return elem[0]

def getcoord(pl_id,i,root,newpath,bj_no):
    txt = str(i)+' 0'+ '\n'
    for child in root:
        if child.attrib['DATANAME'] == 'PNT_COORD':
            for childone in child:
                if childone.tag == 'ROWDATA':
                    coord = []
                    for childtwo in childone:
                        tu = ()
                        if childtwo.attrib['PL_ID'] == pl_id:
                            jzdh = int(childtwo.attrib['PNT_SERIAL'])
                            X = childtwo.attrib['Y_COORD']
                            Y = childtwo.attrib['X_COORD']
                            tu =(jzdh,X,Y)
                            coord.append(tu)
                            # txt = txt + childtwo.attrib['PNT_SERIAL'] + ',' + childtwo.attrib['Y_COORD'] + ','+childtwo.attrib['X_COORD'] + '\n'
                    coord.sort(key=takeSecond)
                    # print(coord)
                    for c in coord:
                        txt1 = str(c[0])+' '+c[1]+' '+c[2]+ ' 1.#QNAN 1.#QNAN'+'\n'
                        txt = txt + txt1
    # return txt

        f = open(newpath + '/' + bj_no + '_zb.txt', 'a')
    f.write(txt)
    print(txt)
    f.close()

def bjb_parse(filePath):
    newpath = os.path.dirname(filePath)
    newpath = getOutPutFolder(newpath, 'outPut')
    print(newpath)
    text=open(filePath).read()
    text=re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+",u"",text)
    root=ET.fromstring(text)
    for child in root:
        if child.attrib['DATANAME'] == 'BL_PROJ_BUILD':
            # print(child.attrib)
            for childone in child:
                if childone.tag == 'ROWDATA':
                    for childtwo in childone:
                        FROM_BPJ_NO = childtwo.attrib['FROM_BPJ_NO']
                        txt = childtwo.attrib['FROM_BPJ_NO'] + ',' + childtwo.attrib['PROJ_NAME'] + ',' + childtwo.attrib['PROJECT_NO'] +'\n'
                        print(txt)
                        f = open(newpath+'/'+FROM_BPJ_NO+'_prj.txt', 'a')
                        f.write(txt)
                        f.close()
        if child.attrib['DATANAME'] == 'PLOT':
            for childone in child:
                if childone.tag == 'ROWDATA':
                    i = 0
                    for childtwo in childone:
                        i = i+1
                        txt = FROM_BPJ_NO + ',' + childtwo.attrib['PL_NAME'] + ',' + childtwo.attrib['PL_ID'] + ','+str(i)+'\n'
                        print(txt)
                        f = open(newpath + '/' + FROM_BPJ_NO + '_dk.txt', 'a')
                        f.write(txt)
                        f.close()
                        getcoord(childtwo.attrib['PL_ID'], i, root,newpath,FROM_BPJ_NO)
                    #     txt_zb_dk_s = getcoord(childtwo.attrib['PL_ID'],i,root)
                    #     txt_zb_dk = txt_zb_dk + txt_zb_dk_s
                    # txt_zb_pc = 'Polygon\n' + txt_zb_dk +'End'
                    # f = open(newpath + '/' + FROM_BPJ_NO + '_zb.txt', 'a')
                    # f.write(txt_zb_pc)
                    # f.close()








