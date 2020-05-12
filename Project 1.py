from student import Student

s1 = Student("Hunter",0)
s2 = Student("Bob",0)



print(s1.getName(),'&', s1.getName(),":",s1._eq_(s1))
print(s1.getName(),'&', s2.getName(),":",s2._eq_(s1))
print(s2.getName(),'&', s2.getName(),":",s2._eq_(s2))
print(s2.getName(),'&', s1.getName(),":",s1._eq_(s2))
