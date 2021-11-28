l=['0','Night Blindness','Dry Skin','Dry Eyes','Delayed Growth','Acne and Break Out','Scurvy','Fatigue','Weight Loss','Anemia','Dry Hair','Bone Weakness','Joint Pain','Mood Swings','Muscle Cramps','Difficulty in Walking','Muscle Pain','Visual Disturbances','General Unwellness','InCoordination','Significant Bleeding','Poor Bone Development','Osceorosis','Risk of Cardiovascular Disease','Hemorrhage','Weakness','WeightLoss','Mouth Horness','Confusion','Loss of Appetite']

vnd={'Vitamin A':l[1:6],'Vitamin C':l[6:11],'Vitamin D':l[11:15],'Vitamin E':l[15:20],'Vitamin K':l[20:25],'Vitamin B':l[25:]}

med={'Vitamin A':['HealthyHey nutritional natural vitamin A- 2400mcg','Profoods vitamin A palmitate- 250 cws powder','Vitawin vitamin A capsules- 500mg'],'Vitamin B':['Biotin gummies','Persona vitamin B12','Nordic naturals vitamin B complex'],'Vitamin C':['Persona vitamin c with bioflavonoids- 500mg','Thorne vitamin c with flavonoids- 500mg','Nordic naturals vitamin c gummies'],'Vitamin D':['Pure encaplusation D3','NOW foods chewable vitamin D3','Throne Vitamin D/K2'],'Vitamin E':['Benvite vitamin E capsules','Covita vitamin E capsules','E-care vitamin E capsules'],'Vitamin K':['Healthvit vitamin K','Vitals multivitamin','Himalayan organics vitamin k2']}

def check(x):
    d={}
    for i in x:
        s=l[int(i)]
        for j in vnd:
            for k in vnd[j]:
                if k==s:
                    # print(j)
                    # print(med[j])
                    d[j]=med[j]
    return d

# print(med)