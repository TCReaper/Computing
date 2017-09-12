

import time
import xlsxwriter

def options(op_list):
      print(op_list[0])
      for i in range(1,len(op_list)):
            print(str(i)+'. '+op_list[i])
      query = input('>>> ')
      if op_list[int(query)] == 'N/A':
            return 'NA'
      elif op_list[1] != 'N/A':
            return int(query)-1
            print('here')
      else:
            return int(query)-2

def decisions(dec_list):
      made = []
      for i in range(len(dec_list)//2):
            print(dec_list[2*i]+'\t'+dec_list[2*i+1],end='  > ')
            cur_dec = int(input(''))
            made.append(cur_dec)
      return made
      
                  
def get_response():
      
      print('\n\t\tInput \'x\' next to stop receiving data')
      age = input('Age: ')
      if age in [None,'x','stop','end']:
            return None
      else:
            pass
      

      gender = options(['Gender:','Male','Female'])
      education = options(['Education:','N/A','PSLE','O Levels','A Levels','ITE','Diploma','Degree & above'])
      income = options(['Monthly income:','N/A','< $2000','< $3000','< $4000','$4000 & above'])

      #fertility intention questions
      marital_status = options(['Marital status:','Single','Married','Divorced'])
      if marital_status == 0:
            plan_marriage = options(['Planning to marry:','Yes','No'])
            plan_kids = options(['Plan for kids:','Yes','No'])
            if plan_kids == 0:
                  first_kid = int(input('When would you have first kid: '))
                  kid_size = int(input('How many kids: '))
            else:
                  first_kid = ''
                  kid_size = ''
            
            have_kids = ''
            sons = ''
            daughters = ''
            when_first_kid = ''
            plan_for_more = ''
            when_next = ''
            how_many = ''
            
      else:
            plan_marriage = ''
            plan_kids = ''
            first_kid = ''
            kid_size = ''
            
            have_kids = options(['Have kids:','Yes','No'])
            if have_kids == 0:
                  sons = int(input('How many sons: '))
                  daughters = int(input('How many daughters'))
                  when_first_kid = int(input('When did you have first kid: '))
            else:
                  sons = ''
                  daughters = ''
                  when_first_kid = ''
                  
            plan_for_more = options(['Planning for more kids:','Yes','No'])
            if plan_for_more == 0:
                  when_next = int(input('When would you want next kid: '))
                  how_many = int(input('How many in total: '))
            else:
                  when_next = ''
                  how_many = ''
      
      #decision questions

      print('TODAY/t1 MONTH')
      decisions_made_1 = decisions(['750','800','700','800','650','800','600','800','500','800'])
      print('6 MONTHS/t7 MONTHS')
      decisions_made_2 = decisions(['750','800','700','800','650','800','600','800','500','800'])
      print('SURE\tRISKY')
      decisions_made_3 =  decisions(['450','50% of 800','400','50% of 800','350','50% of 800','300','50% of 800','250','50% of 800'])

      risk_taker = int(input('How risky are you: '))
      money = options(['Donate or Keep','Donate','Keep'])
      if money == 0:
            organisation = input('Letter: ')
      else:
            organisation = ''

      condition = input('Donation condition: ')

      #input to list

      datalist = [age,gender,education,income,marital_status,plan_marriage,plan_kids,first_kid,kid_size,
                have_kids,sons,daughters,when_first_kid,plan_for_more,when_next,how_many]
      for i in [decisions_made_1,decisions_made_2,decisions_made_3]:
            for choice in i:
                  datalist.append(choice)
      for i in [risk_taker,condition,money,organisation]:
            datalist.append(choice)
            
      print(datalist)
      return datalist


workbook = xlsxwriter.Workbook('SurveyData.xlsx')
worksheet = workbook.add_worksheet('Responses')

response = [#list of lists
      ]

top_row = ['1. Age','2. Gender','3. Education','4. Monthly Income','5. Marital status','6. Plan_marriage','7. Plan_kids','8. When_first kid','9. How many kids',
           '10. Have kids?','Nson','Ndaughter','11. When_first kid','12. More kids in future','13. When_next kid','14. How many kids','Decision_condition',
           'Decision 1','Decision 2','Decision 3','Decision 4','Decision 5','Decision 6','Decision 7','Decision 8','Decision 9','Decision 10',
           'Decision 11','Decision 12','Decision 13','Decision 14','Decision 15','Risk aversion','Donation_Condition','Keep','Donate (A,B,C)','Draw (if C)',
           'Date','Site','Helper']

row = 1
col = 0
for i in top_row:
      worksheet.write(row, col, i)
      col += 1

new_data = ''

while new_data != None:
      new_data = get_response()
      if new_data != None:
            response.append(new_data)

print(response)

row = 2
col = 0
for dataset in response:
      for i in dataset:
            worksheet.write(row, col, i)
            col += 1
      row += 1

#worksheet.write('A1', 'Hello world')

time.sleep(1)

workbook.close()
