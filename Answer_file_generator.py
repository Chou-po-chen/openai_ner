import pandas as pd

class Answer_file_generator:
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = pd.DataFrame(columns=['file','label','start','end','content','time'])
        self.index = 0
        self.dtype = {'file':str,'label':str,'start':int,'end':int,'content':str,'time':str}
    def add_item(self,file_name,start,end,label,content,time=None):
        self.data.loc[len(self.data)] = pd.Series({'file':file_name,'label':label,'start':start,'end':end,'content':content,'time':time})

    def save(self):
        self.data.to_csv(self.file_name,index=False , sep='\t' , header=False)
        # if row is not time info , it will be \t\t at the end of the line , del it 
        with open(self.file_name, 'r' , encoding='UTF-8') as f:
            lines = f.readlines()
            lines = [line.replace('\t\n', '\n') for line in lines]
            f.close()
        with open(self.file_name, 'w') as f:
            f.writelines(lines)
            f.close()
        