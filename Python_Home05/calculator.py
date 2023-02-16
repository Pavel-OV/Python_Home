s=input('введите выражение')
operatory=['*','/','+','-']
s=[s]
#digital=[]
# for i in s:
#     text=''
#     if i.isdigit():
#         text=''.join([text,i])
#         sp=int(text)
#         digital.append(sp) 
# print(digital)
# sums=0
def get_calculation(s):
    for i in operatory:
        calculation=s.partition(operatory)
        if i==operatory:
            return get_calculation(operatory[0])*get_calculation(operatory[2]))
                
        
  
