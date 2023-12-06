import re


# phis: output from chatgpt

# return labels array [file_name , start_index , end_index , label , content , time]
def label_generator(file , file_name , gpt_res):
    now_index = 0
    res = []
    for line in gpt_res.split('\n'):
        #IDNUM: 00Y42304
        cilon_index = line.find(':')
        if cilon_index != -1:
            label = line[:cilon_index]
            content = line[cilon_index+2:]
            time = None
            if content.find('=>')!=-1:
                time = content[content.find('=>')+2:]
                content = content[:content.find('=>')]
            
            # search content in file
            pattern = re.compile(content)
            match = pattern.search(file , pos=now_index)
            if match!=None:
                start_index = match.start()
                end_index = match.end()
                now_index = end_index
                res.append([file_name , start_index , end_index , label , content , time])
    return res
                