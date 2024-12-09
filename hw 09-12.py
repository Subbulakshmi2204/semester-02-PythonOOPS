class Camera:
    def __init__(self,resolution):
        self.resolution=resolution
    def take_photo(self):
        print(f"Taking a photo with resolution:{self.resolution} MP")
class Phone:
    def __init__(self,phone_number):
        self.phone_number=phone_number
    def make_call(self):
        print(f"Making a call from {self.phone_number} number")
class SmartPhone(Camera,Phone):
    def __init__(self,brand,android_version,resolution,phone_number):
        Camera.__init__(self,resolution)
        Phone.__init__(self,phone_number)
        self.brand=brand
        self.android_version=android_version
    def displaydeviceinfo(self):
        print(f"Brand:{self.brand}\nAndroid's Version:{self.android_version}\nResolution:{self.resolution}\nPhone Number:{self.phone_number}")
sp=SmartPhone("IQOO Z9X","14",55,9382835213)
sp.displaydeviceinfo()

class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def student_info(self):
        print(f"Name:{self.name}\nCourse:{self.course}")
class StudentAthlete(Student):
    def __init__(self,name,course,sport):
        super().__init__(name,course)
        self.sport=sport
    def displayathleteinfo(self):
        self.student_info()
        print(f"Sport:{self.sport}")
s=StudentAthlete("Subbulakshmi","AI","Badminton")
s.displayathleteinfo()
