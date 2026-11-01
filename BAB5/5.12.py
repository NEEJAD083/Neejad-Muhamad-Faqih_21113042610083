# BEFORE: this runs, but the conditional tests are badly styled.
age=25
name='Ada'
if age<18 and name=='Ada':
    print("Ada is under 18.")
elif age>=18 and age<65:
    print("Ada is an adult.")
else:
    print("Ada is an elder.")
if name!='Sam':
    print("The name is not Sam.")
 
 # AFTER: the same program, with one space around every operator.
age = 25
name = 'Ada'
 
if age < 18 and name == 'Ada':
    print("Ada is under 18.")
elif age >= 18 and age < 65:
    print("Ada is an adult.")
else:
    print("Ada is an elder.")
 
if name != 'Sam':
    print("The name is not Sam.")
 