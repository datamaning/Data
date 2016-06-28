#!/usr/bin/env python
#coding=utf-8
import sys
import os
import jieba
import codecs
from sklearn.datasets.base import Bunch
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
def savefile(savepath,content):
    fp=open(savepath,"wb",)
    fp.write(content)
    fp.close()
def readfile(path):
    fp=open(path,'rb')
    content=fp.read()
    fp.close()
    return content
corpus_path="train_corpus_seg/"
seg_path="test_corputs/"
catelist=os.listdir(corpus_path)
for mydir in catelist:
    class_path=corpus_path+mydir+"/"
    seg_dir=seg_path+mydir+"/"
    if not os.path.exists(seg_dir):
        os.makedirs(seg_dir)
    file_list=os.listdir(class_path)
    for file_path in file_list:
        fullname=class_path+file_path
        content=readfile(fullname).strip()
        content=content.replace("\r\n","").strip()
        content_seg=jieba.cut(content)

        savefile(seg_dir+file_path,"".join(content_seg))
print "中文语料分词结束"
bunch=Bunch(target_name=[],label=[],filenames=[],contents=[])
wordbag_path='train_word_bag/train_set.dat'
seg_path='train_corpus_seg/'

catelist=os.listdir(seg_path)
bunch.target_name.extend(catelist)
for mydir in catelist:
        class_path=seg_path+mydir+"/"
        file_list=os.listdir(class_path)
        for file_path in file_list:
            fullname=class_path+file_path
            bunch.label.append(mydir)
            bunch.filenames.append(fullname)
            bunch.contents.append(readfile(fullname).strip())
file_obj=open(wordbag_path,'wb')
prickle.dump(bunch,file_obj)
file_obj.close
