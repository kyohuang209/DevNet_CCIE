import os
import re

#[银魂][05][BDRIP][1080][H264_FLAC].chs.ass  wrong
#[银魂][05][1080P][BDRip][HEVC-10bit][FLAC].mkv  right


filelist = os.listdir("E:\\11")

os.chdir(r"E:\11")
#print(filelist)

for filename in filelist:
    pattern1 = "\[.+\]\[.+\]\[.+\]\[1080P\]\[BDRip\]\[HEVC-10bit\]\[FLAC\]"
    pattern2 = "\.chs\.ass"
    #print(filename)
    matchstring1 = re.findall(pattern1, filename)
    matchstring2 = re.findall(pattern2, filename)
    print("前半段=",matchstring1," 后半段=", matchstring2)
    if len(matchstring1) != 0:
        #print(filename)
        print(matchstring1)
        #print(matchstring[0])
        #print("文件结束")
        os.rename(filename, matchstring1[0]+".ass")