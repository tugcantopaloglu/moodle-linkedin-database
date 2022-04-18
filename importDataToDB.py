import random
project=["'Database Project'","'OOP Project'","'Research Project'","'Thesis Project'","'International Project'","'Scientific Project'"]
language=["'German'","'English'","'French'","'Japanese'","'Spanish'","'Turkish'","'Russian'","'Arabic'","'Korean'"]
certificate=["'Project Management Software Certification'","'Digital Marketing Certificate'","'Leadership and Effective Management Certificate'",
              "'Human Resources Management Certificate'","'Office 365 Programs Certification'"]
test_name=["'IELTS'","'TOEFL'","'GOETHE'","'GRE'","'SAT'"]
test_score=[90,86,50,65,100,75,80,87,92,61,54,76,98,83]
company=[800000,
800001,
800002,
800003]
dosya = open("dosya.txt")
list = []
for satir in dosya:
       list = satir.split("	")
       if list[1] == '"Test_Score"':
          print("INSERT INTO Test_Score VALUES (",list[0],",",random.choice(test_name),",",random.choice(test_score),")",";")
tarih=["'05-03-2011'","'02-04-2016'","'08-07-2015'","'03-01-2020'","'16-07-2022'","'16-12-2014'","'19-05-2013'","'03-01-2020'"]
title=["'Engineer'","'Manager'","'Human Resources'","'Cleaning Staff'","'Data Scientist'","'Accounter'","'Computer Engineer'",
       "'Software Engineer'","'Advertiser'","'Game Developer'","'IT'","'Web Developer'","'Intern'","'Frontend Developer'","'Backend Developer'"]
user_id=[100000,
100001,
100002,
100003,
100004,
100005,
100011,
100012]

course_id=[140000,
140001,
140002,
]
location=["'İzmir'","'İstanbul'","'Ankara'","'Konya'","'Avusturya'","'İngiltere'","'Fransa'","'İtalya'","'İspanya'","'Amerika'",
          "'Japonya'"]
ad=["'Pictures'","'CVs'","'Videos'","'Notes'","'Lectures'","'Plans'"]
j=0
for i in range(160000,160050):
      print("INSERT INTO Post_Like VALUES (",random.choice(course_id),",",random.choice(user_id),");")
