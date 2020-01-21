from .models import student,student_marks

def classTopper(cls):
    adm,mark = [],[]
    for i in student.objects.filter(class_in=cls):
        adm.append(i.adm_no)
    for i in adm:
        m=0
        for j in student_marks.objects.filter(adm_no=i):
            m+=int(j.marks_in_theory)+int(j.marks_in_practical)
        mark.append(m)
    try:
        maxm=max(mark)
        index=mark.index(maxm)
        adm_no=adm[index]
        for i in student.objects.filter(adm_no=adm_no):
            name=i.first_name +" "+i.last_name
        return (name,maxm)
    except:
        return ('no student',0)
