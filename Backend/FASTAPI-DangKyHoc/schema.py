from datetime import date
from pydantic import BaseModel
class UserSchema(BaseModel):
    userID =int
    userName=str
    userEmail=str
    userPassword=str
    userRole=int
    class Config:
        orm_mode = True

class StudentSchema(BaseModel):
    studentID=str
    studentEmail=str
    studentName=str
    studentK=int
    studentDOB=date
    studentGender=str
    studentAddress=str
    studentPhone=str
    studentYearJoin=int
    studentParent=str
    branchID=int
    group=int
    status=int

class TeacherSchema(BaseModel):
    teacherID=str
    teacherEmail=str
    teacherName=str
    teacherDOB=date
    teacherGender=str
    teacherAddress=str
    teacherPhone=str
    teacherDatejoin=date
    majorID=str
    branchID=int

class ImageSchema(BaseModel):
    userName=str
    image=str

class MajorSchema(BaseModel):
    majorID=str
    majorName=str

class BranchSchema(BaseModel):
    branchID=str
    branchName=str
    majorID=str
    groupEnd=int

class SubjectSchema(BaseModel):
    subjectID=str
    subjectName=str
    majorID=str
    subjectCredit=int

class CourseSchema(BaseModel):
    courseID=int
    subjectID=str
    subjectName=str
    className=str
    courseDate=int
    courseShiftStart=int
    courseShiftEnd=int
    courseCredits=int
    courseRoom=str
    teacherID=str
    teacherName=str
    groupID=str

class ClassSchema(BaseModel):
    courseID=str
    studentID=str

class GradeSchema(BaseModel):
    studentID=str
    groupID=str
    courseID=str
    progressGrade=float
    bonusGrade=float
    examGrade1=float
    examGrade2=float
    finalGrade=float

class GroupSchema(BaseModel):
    groupID=str
    groupName=str
    groupYear=str
    groupTerm=str

class YearSchema(BaseModel):
    yearID=int
    yearStart=date
    yearEnd=date