from sklearn.datasets.base import Bunch
bunch=Bunch(target_name=[],label=[],filenames=[],contents=[])
words_path='train_word_bag/train_set.dat'
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


    

