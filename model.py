from openai import OpenAI
import openai
import backoff 
import tiktoken




class Model():
    def __init__(self , model = None):
        self.model = model
        self.client = OpenAI()
        self.completion = None

        self.encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    
    def count_tokens(self , text):
        return len(self.encoding.encode(text))
    
    # @backoff.on_exception(backoff.expo, openai.RateLimitError)
    def sent_to_model(self , input):
        # return '########## send: token = '+ str(self.count_tokens(input))
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": 'Find PHI(DOCTOR,DATE,IDNUM,MEDICALRECORD,PATIENT,HOSPITAL,TIME,DEPARTMENT,CITY,ZIP,STREET,STATE,AGE,ORGANIZATION,DURATION,PHONE,URL,LOCATION-OTHER,SET,COUNTRY,ROOM) and normalize time information'},
                {"role": "user", "content": input}
            ]
        )
        
        return completion.choices[0].message.content
    
    
    def middle_split(self , input_str):
       # 找到所有換行符號的位置
        newline_indices = [i for i, char in enumerate(input_str) if char == '\n']

        if newline_indices:
            # 如果存在換行符號
            middle_index = len(input_str) // 2
            closest_newline = min(newline_indices, key=lambda x: abs(x - middle_index))

            first_half = input_str[:closest_newline + 1]
            second_half = input_str[closest_newline + 1:]
        else:
            # 如果沒有換行符號，直接在字串的中間進行切割
            middle_index = len(input_str) // 2
            first_half = input_str[:middle_index]
            second_half = input_str[middle_index:]

        return first_half, second_half
    
    def del_longest_line(self , input_str):
        sp = input_str.split('\n')
        longest_line = ''
        for s in sp:
            if len(s) > len(longest_line):
                longest_line = s
        sp.remove(longest_line)
        print('del_longest_line: ' )
        return '\n'.join(sp)
    
    
    def get_phi(self , input):
        while self.count_tokens(input) > 4000:
            input = self.del_longest_line(input)
        return self.sent_to_model(input)
        
        
        '''
        # if token > 4000 split it until all part <4000
        if self.count_tokens(input) <= 4000:
            return self.sent_to_model(input)
        else:
            
            
            inputs = [input]
            new_inputs = []
            all_token_len_ok = False
            while not all_token_len_ok:
                for s in inputs:
                    if self.count_tokens(s) > 4000:
                        first_half, second_half = self.middle_split(s)
                        new_inputs.append(first_half)
                        new_inputs.append(second_half)
                    else:
                        new_inputs.append(s)
                inputs = new_inputs
                
                # update ok state
                all_token_len_ok = True
                for s in inputs:
                    if self.count_tokens(s) > 4000:
                        all_token_len_ok = False
                        break
            res = []
            for s in inputs:
                res.append(self.sent_to_model(s))
            res = '\n'.join(res)
            return res
            '''



if __name__ == '__main__':
    model = Model('ft:gpt-3.5-turbo-0613:personal::8N0agg9Z')
    
    file = ''
    with open('First_Phase_Validation/data/file9042.txt' , 'r') as f:
        file = f.read()
    
    cnt = model.count_tokens(file)
    print(cnt)
    
    res = model.get_phi(file)
    print(res)