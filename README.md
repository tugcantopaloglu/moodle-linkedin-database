# Moodle-Linkedin Database 
Moodle-Linkedin database which has functionalities from both sites.   
# **1. Analysis**   
## **1.1 Brief Explanation**   
   If we look at these two programs independently for the first time, LinkedIn is a business networking application that connects registered individuals, corporations, and schools all around the world. Job advertising, employment applications, job contacts, and talents, work experiences, interests, and other fields relevant to each user are all included in the application, as are profiles in the form of a CV.
   Moodle, on the other hand, caters to a more specialized audience and allows teachers to require students to register for the course using the passwords they have created, and it incorporates quizzes, exams, homework, and other course-related activities.   
## **2.1 Analysis Report for Each Web application**   
###	   **2.1.a What is the aim of each application?**   
   LinkedIn's goal is to link professionals all over the world in order to create a more efficient and productive business network by allowing them to interact. Moodle's goal is to provide a unique educational environment for educators and students through its use and control, resulting in a more efficient teaching platform.   
###	   **2.1.b What are the main entities of them?**   
   Common main entities of both Db_User , User_Profile , College , Faculty , Department , Transcript.   
   In addition to these, the main entities of LinkedIn Company , Company_Profile , Collection , Job_Offer , Post , Achievement.   
  In addition to these, the main entities of Moodle Course , Grading_Req.   
###	   **2.1.c What are the characteristics of each entity?**   
   Db_User entity has unique user_id,username and password. The user can be of Student,Teacher and Worker. It has flag attributes that control each of them. If the user is a worker it has sector,career title and work time. If the user is a teacher it has teacher degree.
   User_Profile entity has unique user_profile_id , full name , unique mail , address , unique phone , sex and birth date.   
   Company entity entity has unique company_id and mgr_id.   
   Company_Profile entity has unique company_profile_id,unique company name,company location, and unique company phone.   
   Transcript entity has unique transcript no , type , taken date and gpa.   
   College entity has unique college id , college name , location and phone.   
   Faculty entity has unique faculty id , name , location and phone.   
   Department entity has unique id,phone , name and location.   
   Course entity has unique id,name and description.   
   Grading_Req entity has unique id and type.One Grading_req can be only one of four types.These are Quiz,Project,Exam and Homework.Each of them has grade attribute.   
   Achievement entity has unique id,type and date. One Achievement can be only one of four types. These are Test Score , Willing Project , Language and Certificate. Each of them has name attribute and Test Score has score attribute.   
   Collection entity has unique id. Collection includes two type data.These are Job Offer and Post. Job Offer has unique id , title and location. Post has unique id.       
###	   **2.1.d What relationships exists among the entities?**    
   Each Db_User must has a User_Profile.Each User_Profile must belong a Db_User.   
   Each User_Profile can display more than one profile, and each User_Profile can be viewed by more than one User_Profile.Each User_Profile can connect with multiple User_Profile.   
   Each Db_User can save more than one Collection. Each Collection must necessarily be registered by a Db_User.   
   Each Db_User can apply to or view more than one Job_Offer. Each Job_Offer can be applied or viewed by more than one Db_User.   
   Each Db_User can share, like, comment on more than one Post. Each Post can be liked, shared, commented on by more than one Db_User.   
   Each Db_User can achieve more than one Achievement. An Achievement can belong to more than one Db_User.   
   Each Db_User can upload more than one Private_File. One Private_File must necessarily be uploaded by a Db_User.   
   Each Db_User can has more than one Transcript. One Transcript can only belong to one Db_User.   
   One Transcript can taken by only one College. Each College can take more than one Transcript.   
   Each Student can study only one College. Each College can has more than one Student.   
   Each Teacher can work only one College. Each College can has more than one Teacher.   
   Each College can have more than one Faculty. Each Faculty can belong to only one College.   
   Each Faculty can has more than one Department. Each Department must necessarily and only belong to one Faculty.   
   Each Department can give one or more Course. Each Course is provided by only one Department.   
   Each Student can enroll in more than one Course. Each Course can receive more than one Student registration.   
   Each Teacher can teach more than one Course. Each Course must be taught by one or more Teacher.   
   Each Course must has one or more Grading_Req. Each Grading_Req must belong to only one Course.   
   Every Worker can has a career in a Company. Each Company can has more than one Worker.   
   Each Company must has a Company_Profile. Each Company_Profile must belong to a Company.   
   Each Company can offers more than one Job_Offer. Each Job_Offer must be offered by only one Company.   
###	   **2.1.e What are the constraints related to entities, their characteristics and the relationships among them?**   
   Db_User’s user_id attiribute must be initialized between 100000 and 199999.   
   Transcript’s transcprit_no attribute must be initialized between 200000 and 299999.   
   College’s college_id attribute must be initialized between 300000 and 399999.   
   Faculty’s faculty_id attribute must be initialized between 400000 and 499999.      
   Department’s department_id attribute must be initialized between 500000 and 599999.   
   Course’s course_id attribute must be initialized between 600000 and 699999.   
   Grading_Req’s grading_req_id attribute must be initialized between 700000 and 799999.   
   Company’s company_id attribute must be initialized between 800000 and 899999.   
   User_Profile’s user_profile_id attribute must be initialized between 900000 and 999999.   
   Company_Profile’s company_profile_id attribute must be initialized between 700000 and 799999.   
   Achievement’s achievement_id attribute must be initialized between 110000 and 119999.   
   Collection’s cllection_id attribute must be initialized between 120000 and 129999.   
   Job_Offer’s job_offer_id attribute must be initialized between 130000 and 139999.   
   Post’s post_id attribute must be initialized between 140000 and 149999.   
   Private_File’s file_id attribute must be initialized between 150000 and 159999.   
   Grading types can be Exa, Project, Homework or Quiz.   
   Achievements types can be Willing Project, Language, Test Score or Certificate.   
   Collection can be both job offer or post.   
# **2. Design - Conceptual Design**   

![Picture1](https://user-images.githubusercontent.com/53763911/163815953-31551b49-9dba-4115-a406-7274278b68d6.jpg)   

# **3. Design - Logical Model**
##   3.1 Mapping   
**1.ITERATION**   
1-)   
TRANSCRIPT(transcript_no,type,taken_date,gpa)   
COLLEGE(college_id,college_name,college_location,college_phone)   
FACULTY(faculty_id,faculty_name,faculty_location,faculty_phone)      
DEPARTMENT(department_id,department_phone,department_name,department_location)   
COURSE(course_id,course_name,course_description)   
COMPANY(company_id,mgr_id)   
COMPANY_PROFILE(c_profile_id,company_name,comapny_loc,company_phone)   
USER_PROFILE(user_profile_id,fname,minit,lname,mail,address,phone,sex,bdate)   
2-)      
3-) 1 to 1   
COMPANY(company_id,mgr_id,c_profile_id)  C_HAS_PROFILE   
4-)  1 TO N   
FACULTY(faculty_id,faculty_name,faculty_location,faculty_phone,faculty_college_id) BELONGS   
DEPARTMENT(department_id,department_phone,department_name,department_location,department_faculty_id) HAS   
COURSE(course_id,course_name,course_description,course_department_id) GIVE   
TRANSCRIPT(transcript_no,type,taken_date,gpa,t_college_id) TAKEN_BY   
5-) M to N   
VIEW_PROFILE(user_profile_id,user_viewer_id)   
CONNECT(user_profile_id,user_connect_id)   
6-)   
7-)   
8-)   
8.D.)   
DB_USER(user_id,username,psswrd,student_flag,teacher_flag,worker_flag,teacher_degree,sector)   
8.A.)   
ACHIEVEMENT(achievemet_id,date,achievement_type)   
TEST_SCORE(achievemet_id,score,test_name)   
WILLING_PROJECT(achievemet_id,project_name)   
LANGUAGE(achievement_id,language_name)   
CERTIFICATE(achievement_id,certificate_name)   
8.A.)   
GRADING_REQ(grading_req_id,grading_type)   
QUIZ(grading_req_id,quiz_grade)   
PROJECT(grading_req_id,project_grade)   
EXAM(grading_req_id,exam_grade)   
HOMEWORK(grading_req_id,homework_grade)   
9-)   
COLLECTION(collection_id)   
POST(post_id,post_collection_id)   
JOB_OFFER(job_offer_id,job_collection_id,job_title,job_location)   
**2.ITERATION**   
1-)      
2-)   
PRIVATE_FILE(file_id,private_user_id,file_name)  UPLOAD   
3-) 1 to 1   
DB_USER(user_id,username,psswrd,student_flag,teacher_flag,worker_flag,teacher_degree,sector,user_profile_id) HAS_PROFILE   
4-) 1 to N   
TRANSCRIPT(transcript_no,type,taken_date,gpa,t_college_id,t_user_id) HAS_TRANS   
DB_USER(user_id,username,psswrd,student_flag,teacher_flag,worker_flag,teacher_degree,sector,user_profile_id,student_college_id)  STUDY   
DB_USER(user_id,username,psswrd,student_flag,teacher_flag,worker_flag,teacher_degree,sector,user_profile_id,student_college_id,teacher_college_id) WORK    
DB_USER(user_id,username,psswrd,student_flag,teacher_flag,worker_flag,teacher_degree,sector,user_profile_id,student_college_id,teacher_college_id,worker_company_id,career_title,start_date,finish_date) CAREER   
JOB_OFFER(job_offer_id,job_collection_id,job_title,job_location,job_offer_company_id) OFFERS      
COLLECTION(collection_id,collection_user_id) SAVE   
GRADING_REQ(grading_req_id,grading_type,grading_req_course_id) HAS_CRITERIA   
5-) N TO M   
LIKE(post_id,user_id)   
COMMENT(post_id,user_id)   
SHARE(post_id,user_id)      
ENROLL(user_id,course_id,grade)   
TEACH(user_id,course_id,year,semester)   
ACHIEVE(achievement_id,user_id)   
APPLY(job_offer_id,user_id)   
VIEW(job_offer_id,user_id)   
6-)   
7-)   
8-)   
9-)   

##   3.2 Relational Model   
![Picture2](https://user-images.githubusercontent.com/53763911/163816400-ff39f626-1109-477e-baff-688965a5e166.jpg)   

## 4. Implementation - Physical Model
   Physical model implemented with POSTGRE SQL and pgAdmin 4.   
   All SQL codes can be found in Project folder. Tables can be found in “Tables.txt”. In order to maintain readibility all tuples are not included in tuples section and tuples can be found in “Tuples.txt”. Triggers can be found in “Triggers.txt”. Because of the disability of POSTGRE SQL instead of assertions we used check constraints and check constraints can be found in “CheckConstraints.txt”.Delete and Update insertions can be found in “DeleteUpdate.txt”. SQL statements can be found in “SelectStatements.txt”.   

