def main_script():
    import pandas as pd
    import math 
    df = pd.read_excel(r"C:\Users\prakr\OneDrive\Desktop\burs_nachbac_baseline.xlsx",sheet_name="Gen1",dtype=object)
    df = df.iloc[range(0,len(df),1),0:32]
    df = df[0:1440]
    list1,list2,list3,count1,count2,count3,numerator,denominator,mph = ([] for i in range(9))
    
    for col in df.columns:
        col_ls = df[col].tolist()
        list1.append((col_ls))    
    for sublist in list1:
        for item in sublist:
            list2.append(item)
    list2= [int((x)) for x in list2] 
    main=[list2[1440*x:1440*x+1440] for x in range(0,math.ceil(len(list2)/1440))]
    hour=[list2[60*x:60*x+60] for x in range(0,math.ceil(len(list2)/60))]
    
    for a in main:
        k = 5
        for i in range(len(a)-5):
            if a[i:i+k] == [0 for i in range(k)]:
                a[i:i+k] = ['zero' for i in range(k)]
        for i in range(len(a)-1):
            if a[i] == 'zero' and a[i+1] == 0:
                a[i+1] = 'zero'
    
    for i in main:
        for j in i:
            list3.append(j)
    sleep_per_day=[hour[24*x:24*x+24] for x in range(0,math.ceil(len(hour)/24))]
    
    for i in sleep_per_day:
        for j in i:
            minn=[]
            for e in j:
                if e != 0:   
                    minn.append(e)  
            count1.append(minn)
        count1.append
    sleep_per_fly=[count1[24*x:24*x+24] for x in range(0,math.ceil(len(count1)/24))]
    for i in sleep_per_fly:
        for j in i:
            n=(sum(j))
            numerator.append(n)
    #per_f=[numerator[24*x:24*x+24] for x in range(0,math.ceil(len(numerator)/24))]
    for i in sleep_per_day:
        for j in i:
            minn=[]
            for e in j:
                if e != 'zero':   
                    minn.append(e)  
            count3.append(minn)
    per_fly1=[count3[24*x:24*x+24] for x in range(0,math.ceil(len(count3)/24))]
    for i in per_fly1:
        for j in i:
            d=(len(j))
            denominator.append(d)
    #per_f1=[denominator[24*x:24*x+24] for x in range(0,math.ceil(len(denominator)/24))]
    for m,n in zip(numerator,denominator):
        z= m/n if n!= 0 else 0
        count2.append(z)
    per_f2=[count2[24*x:24*x+24] for x in range(0,math.ceil(len(count2)/24))]
    
    d=[list3[60*x:60*x+60] for x in range(0,math.ceil(len(list3)/60))]
    p=[d[24*x:24*x+24] for x in range(0,math.ceil(len(d)/24))]
    
    for i in p:
        for j in i:                            
            cnt= j.count('zero')
            mph.append(cnt)
   
    new2_lst=[mph[24*x:24*x+24] for x in range(0,math.ceil(len(mph)/24))]
    new3_lst=[list3[720*x:720*x+720] for x in range(0,math.ceil(len(list3)/720))]
    
    day=new3_lst[::2]
    night=new3_lst[1:][::2]
    day1_lst=[]
    night1_lst=[]
    def daynight(inputt,inlist): 
        for i in inputt:
            day_lst=[]
            count=0
            for e in i:
                if e== 'zero':
                    count=count+1    
                else:
                    if(count>=5):
                        day_lst.append(count)
                    count=0
            if(count>=5):
                day_lst.append(count)
            inlist.append(day_lst)        
    daynight(day,day1_lst)
    daynight(night,night1_lst)

    zeroCount = 0
    countLst = []
    for i in night:
        for j in i:
            if j == "zero":
                countLst.append(zeroCount+1 if (zeroCount) != 0 else 0)
                break
            zeroCount+=1
        zeroCount=0

    list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9 = ([] for i in range(9))
    
    for lst in day1_lst:
        list_1.append(lst)
        list_2.append(len(lst))                     #Total number of day bouts - day
        list_3.append(sum(lst))                     #Total minutes of deep sleep - day 
        list_4.append((sum(lst) / len(lst)) if (len(lst)) != 0 else 0)                     #Average deep sleep per fly - day
            
    for lstt in night1_lst:    
        list_5.append(lstt)
        list_6.append(len(lstt))                     #Total number of day bouts - night
        list_7.append(sum(lstt))                     #Total minutes of deep sleep - night
        list_8.append((sum(lstt) / len(lstt)) if (len(lstt)) != 0 else 0)                     #Average deep sleep per fly - night
    
    for i,j in zip(list_3,list_7):
        list_9.append(i+j)
    
    jnt_data=[[list_1,list_2,list_3,list_4],[list_5,list_6,list_7,list_8],[list_9,countLst]]
    emptylist=[]
    for i in jnt_data:
        o=pd.DataFrame(i).transpose()
        emptylist.append(o)
    
    df1,df2,df3= emptylist[0],emptylist[1],emptylist[2]
    df1.columns=["length of day bouts","Total no. of day bouts","Total minutes of deep sleep in daylight","Average day bout length"]  
    df2.columns=["length of night bouts","Total no. of night bouts","Total minutes of deep sleep in night","Average night bout length"] 
    df3.columns=["Total deep sleep in a day","Latency"]
    frame=pd.DataFrame(new2_lst, columns = ['hr-1', 'hr-2','hr-3','hr-4','hr-5','hr-6','hr-7','hr-8','hr-9','hr-10','hr-11','hr-12','hr-13', 'hr-14','hr-15','hr-16','hr-17','hr-18','hr-19','hr-20','hr-21','hr-22','hr-23','hr-24'])
    frame1=pd.DataFrame(per_f2, columns = ['hr-1', 'hr-2','hr-3','hr-4','hr-5','hr-6','hr-7','hr-8','hr-9','hr-10','hr-11','hr-12','hr-13', 'hr-14','hr-15','hr-16','hr-17','hr-18','hr-19','hr-20','hr-21','hr-22','hr-23','hr-24'])

    for i in [df1,df2,df3,frame,frame1]:
        idx = 0
        data = ['Ch-1', 'Ch-2', 'Ch-3', 'Ch-4','Ch-5','Ch-6','Ch-7','Ch-8','Ch-9','Ch-10','Ch-11','Ch-12','Ch-13','Ch-14','Ch-15','Ch-16','Ch-17','Ch-18','Ch-19','Ch-20','Ch-21','Ch-22','Ch-23','Ch-24','Ch-25','Ch-26','Ch-27','Ch-28','Ch-29','Ch-30','Ch-31','Ch-32']
        i.insert(loc=idx, column='fly', value=data)

    writer2 = pd.ExcelWriter('file.xlsx')
    df1.to_excel(writer2, sheet_name = 'Day sleep', index = False)
    df2.to_excel(writer2, sheet_name = 'Night sleep', index = False)
    df3.to_excel(writer2, sheet_name = 'TsLt', index = False)
    frame.to_excel(writer2, sheet_name = 'Sleep per hour', index = False)
    frame1.to_excel(writer2, sheet_name = 'Countmin', index = False)
     
    writer2.save()    
    
main_script()
