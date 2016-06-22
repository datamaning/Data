#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import jieba
reload(sys)
sys.setdefaultencoding('utf-8')
seg_list=jieba.cut("小明1995年毕业于北京清华大学",cut_all=False)
print "Default Mode:"," ".join(seg_list)
seg_list=jieba.cut("小明1995年毕业于北京清华大学")
print " ".join(seg_list)
seg_list=jieba.cut("小明1995年毕业于清华大学",cut_all=True)
print "Full Mode:"," ".join(seg_list)
seg_list=jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学身照")
print "/ ".join(seg_list)
for i in ra(20):

