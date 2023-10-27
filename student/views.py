from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.views.generic import CreateView
from .models import stud
from .forms import studform
import cv2
import face_recognition
from datetime import datetime, date
import os
import mimetypes

class Add_student(CreateView):
    model = stud
    template_name = "student/stud_register.html"
    form_class = studform


def attendance(request):
    if request.method == "POST":
        roll_no = request.POST['roll_no']
        cam = cv2.VideoCapture(0)   #switch on web camera
        cv2.namedWindow("test")     # open a window
        img_counter = 0
        capture = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)
            k = cv2.waitKey(1)

            if k % 256 == 27:
                print("Escape hit, closing...")
                break

            elif k % 256 == 32:       # space bar
                img_name = "media/images/Image_capture_{}.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                capture = 1
                break

        cam.release()
        cv2.destroyAllWindows()  

        if capture == 1:
            try:
                    cap_image = face_recognition.load_image_file(img_name)
            except:
                    return HttpResponse("Error occured in image handling")
                    
            known_img = "media/student_images/{}.jpg".format(roll_no)
            
            try:
                    known_image = face_recognition.load_image_file(known_img)
            except:
                    return HttpResponse("404 error in image handling ")

            cap_face_encoding = face_recognition.face_encodings(cap_image)
            known_face_encoding = face_recognition.face_encodings(known_image)

            if len(cap_face_encoding) == 0:
                HttpResponse(" No face detevted ")
                print("No face found ")

            else:
                cap_encoding = cap_face_encoding
                known_encoding = known_face_encoding[0]

                results = face_recognition.compare_faces(known_encoding, cap_face_encoding, tolerance=0.6)

                if results:
                        excel_name = 'media/student_attendance/{}.txt'.format(roll_no)
                        print(excel_name)
                        with open(excel_name, 'a') as f:
                            
                            entry = str(datetime.now())
                            entry_line = entry +"\n "
                            f.write(entry_line)
                            
                        print("Person is the same ")
                        return redirect('home')
                else:
                        return redirect('stud_register')
                        print("Different persons")

        return redirect('stud_attendance')
    return render (request=request, template_name="student/attendance.html")



def download(request):
    if request.method == "POST":
        roll_no = request.POST['roll_no']
        print(roll_no)
        try:
            file_name = "{}.txt".format(roll_no)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filepath = BASE_DIR + '/media/student_attendance/' + file_name

            print(filepath)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)

            response['Content-Disposition'] = "attachment; filename=%s" % file_name
            print(response)
            return response
            return redirect('home')
        except: 
            return HttpResponse('404 Invalid roll no, No file for this roll_no')
            

        

    else:
            return render(request, 'student/download.html')