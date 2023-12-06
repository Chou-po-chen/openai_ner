from model import Model
import os
from Answer_file_generator import Answer_file_generator
import re

# DATA_DIR   = rf'First_Phase_Validation/data'
DATA_DIR   = rf'opendid_test'
OUPUT_PHI_DIR    = rf'./.output/phi'

# [DOCTOR,DATE,IDNUM,MEDICALRECORD,PATIENT,HOSPITAL,TIME,DEPARTMENT,CITY,ZIP,STREET,STATE,AGE,ORGANIZATION,DURATION,PHONE,URL,LOCATION-OTHER,SET,COUNTRY]
ALL_LABELS = ['DOCTOR','DATE','IDNUM','MEDICALRECORD','PATIENT','HOSPITAL','TIME','DEPARTMENT','CITY','ZIP','STREET','STATE','AGE','ORGANIZATION','DURATION','PHONE','URL','LOCATION-OTHER','SET','COUNTRY','ROOM']

# model = Model("ft:gpt-3.5-turbo-1106:personal::8NYtED1H")
model = Model("ft:gpt-3.5-turbo-1106:personal::8NhRGXcL")

file_gen = Answer_file_generator('./.output/answer.txt')


file_listdir = os.listdir(DATA_DIR)
all_file_names = []
for file_name in file_listdir:
    if file_name.endswith(".txt"):  # Filter files with a .txt extension
        all_file_names.append(file_name)

# all_file_names = all_file_names[:3]

print(all_file_names)

for file_name in all_file_names:
    file = ''
    with open(os.path.join(DATA_DIR , file_name) , 'r') as f:
        file = f.read()
    cnt = model.count_tokens(file)
    print(f'file: {file_name} , token_cnt: {cnt}')
    if cnt > 4000:
        print(f'file: {file_name} , token_cnt: {cnt} , too long')

if 1:
    # save phi from gpt 
    for file_name in all_file_names:
        # if _PHI.txt does not exist
        if os.path.exists(os.path.join(OUPUT_PHI_DIR , file_name.replace('.txt' , '_PHI.txt'))):
            continue
        file = ''
        with open(os.path.join(DATA_DIR , file_name) , 'r') as f:
            file = f.read()
        
        with open(os.path.join(OUPUT_PHI_DIR , file_name.replace('.txt' , '_PHI.txt'))  , 'w') as f:
            print('write file: ' , file_name.replace('.txt' , '_PHI.txt')  )
            phis = model.get_phi(file)
            f.write(phis)
    
# read phi file and add to file_gen
for file_name in all_file_names:
    file_id = file_name.replace('.txt' , '')
    file = ''
    gpt_res = ''
    
    with open(os.path.join(DATA_DIR , file_name) , 'r') as f:
        file = f.read()
    with open(os.path.join(OUPUT_PHI_DIR , file_name.replace('.txt' , '_PHI.txt'))  , 'r') as f:
        gpt_res = f.read()
    
    now_index = 0
    
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
            
            # print('file_id' , file_name)  
            # print('content' , content)
            try:
                pattern = re.compile(content)
            except:
                continue
            match = pattern.search(file , pos=now_index)
            if match!=None and len(content)>0:
                start_index = match.start()
                end_index = match.end()
                now_index = end_index
                if label in ALL_LABELS:
                    file_gen.add_item(file_id , start_index , end_index , label , content , time)    
    
file_gen.save()



