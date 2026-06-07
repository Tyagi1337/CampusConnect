# CampusConnect

A comprehensive Django-based campus management system designed to streamline academic operations and communication between students, staff, and administration.

## 📋 Project Overview

CampusConnect is a full-featured web application built with Django that facilitates seamless management of educational institutions. It provides role-based access for three main user types:
- **HOD (Head of Department)**: Administrative management
- **Staff**: Teaching and attendance management
- **Students**: Learning and information access

**Repository**: [Tyagi1337/CampusConnect](https://github.com/Tyagi1337/CampusConnect)  
**Created**: May 9, 2023  
**Language Composition**: 
- JavaScript: 91.7%
- CSS: 5.9%
- HTML: 1.9%
- Other: 0.5%

---

## 🎯 Key Features

### Admin/HOD Features
- **User Management**: Add, edit, and manage staff and students
- **Course Management**: Create and manage academic courses
- **Subject Management**: Assign subjects to courses and staff
- **Session Management**: Manage academic sessions and years
- **Attendance Monitoring**: View overall attendance records
- **Leave Management**: Approve/disapprove staff and student leave requests
- **Feedback Management**: View and reply to feedback from students and staff
- **Notification System**: Send notifications to staff and students
- **Profile Management**: Manage admin profile and settings

### Staff Features
- **Attendance Management**: Mark and update student attendance
- **Result Management**: Add and edit student exam and assignment marks
- **Leave Management**: Apply for leave with status tracking
- **Feedback System**: Submit feedback with admin replies
- **Notification System**: Receive and view notifications
- **Live Classroom**: Start and manage online classes
- **Profile Management**: Update personal profile information
- **FCM Token**: Firebase Cloud Messaging integration for push notifications

### Student Features
- **Attendance Tracking**: View personal attendance records
- **Result Viewing**: Check exam and assignment marks
- **Leave Application**: Submit leave requests
- **Feedback System**: Provide feedback to administration
- **Notifications**: Receive important notifications
- **Online Classes**: Join live classroom sessions
- **Profile Management**: Update student information
- **FCM Integration**: Receive push notifications

---

## 🏗️ Architecture & Structure

```
CampusConnect/
├── CampusConnect_app/              # Main Django application
│   ├── models.py                   # Database models
│   ├── views.py                    # Authentication and general views
│   ├── forms.py                    # Django forms for data validation
│   ├── HodViews.py                 # HOD/Admin-specific views
│   ├── StaffViews.py               # Staff-specific views
│   ├── StudentViews.py             # Student-specific views
│   ├── EmailBackEnd.py             # Custom email authentication backend
│   ├── LoginCheckMiddleWare.py     # Login validation middleware
│   ├── EditResultVIewClass.py      # Result editing view class
│   ├── admin.py                    # Django admin configuration
│   ├── migrations/                 # Database migrations
│   ├── templates/                  # HTML templates
│   ├── static/                     # CSS, JavaScript assets
│   └── tests.py                    # Test cases
├── CampusConnect_system/           # Django project settings
│   ├── settings.py                 # Project configuration
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI configuration
│   └── __init__.py
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
├── db.sqlite3                      # Database file
└── static/                         # Project-wide static files
```

---

## 📊 Database Models

### Core Models

**CustomUser** - Extended Django User model with role-based access
- `user_type`: HOD (1), Staff (2), Student (3)

**SessionYearModel** - Academic session information
- `session_start_year`: Start date of session
- `session_end_year`: End date of session

**AdminHOD** - HOD profile linked to CustomUser
- `admin`: OneToOne relationship with CustomUser
- `created_at`, `updated_at`: Timestamp tracking

**Staffs** - Staff profile information
- `admin`: OneToOne relationship with CustomUser
- `address`: Staff address
- `fcm_token`: Firebase Cloud Messaging token

**Students** - Student profile information
- `admin`: OneToOne relationship with CustomUser
- `gender`: Student gender
- `profile_pic`: Student profile picture
- `address`: Student address
- `course_id`: Foreign key to Courses
- `session_year_id`: Foreign key to SessionYearModel
- `fcm_token`: Firebase Cloud Messaging token

**Courses** - Academic courses offered
- `course_name`: Name of the course

**Subjects** - Course subjects/classes
- `subject_name`: Name of subject
- `course_id`: Foreign key to Courses
- `staff_id`: Foreign key to CustomUser (Staff)

### Academic Records

**Attendance** - Attendance session records
- `subject_id`: Foreign key to Subjects
- `attendance_date`: Date of attendance
- `session_year_id`: Foreign key to SessionYearModel

**AttendanceReport** - Individual student attendance records
- `student_id`: Foreign key to Students
- `attendance_id`: Foreign key to Attendance
- `status`: Boolean (Present/Absent)

**StudentResult** - Student exam and assignment marks
- `student_id`: Foreign key to Students
- `subject_id`: Foreign key to Subjects
- `subject_exam_marks`: Exam marks (Float)
- `subject_assignment_marks`: Assignment marks (Float)

**OnlineClassRoom** - Virtual classroom sessions
- `room_name`: Name of the classroom
- `room_pwd`: Room password
- `subject`: Foreign key to Subjects
- `session_years`: Foreign key to SessionYearModel
- `started_by`: Foreign key to Staffs
- `is_active`: Boolean (Active/Inactive)

### Leave Management

**LeaveReportStudent** - Student leave applications
- `student_id`: Foreign key to Students
- `leave_date`: Date of leave
- `leave_message`: Leave reason
- `leave_status`: Status (0=Pending, 1=Approved, 2=Rejected)

**LeaveReportStaff** - Staff leave applications
- `staff_id`: Foreign key to Staffs
- `leave_date`: Date of leave
- `leave_message`: Leave reason
- `leave_status`: Status (0=Pending, 1=Approved, 2=Rejected)

### Communication

**FeedBackStudent** - Student feedback
- `student_id`: Foreign key to Students
- `feedback`: Feedback message
- `feedback_reply`: Admin reply

**FeedBackStaffs** - Staff feedback
- `staff_id`: Foreign key to Staffs
- `feedback`: Feedback message
- `feedback_reply`: Admin reply

**NotificationStudent** - Notifications for students
- `student_id`: Foreign key to Students
- `message`: Notification message

**NotificationStaffs** - Notifications for staff
- `staff_id`: Foreign key to Staffs
- `message`: Notification message

---

## ⚙️ Technologies & Dependencies

```
Django 4.2.1
dj-database-url 2.0.0
Gunicorn 20.1.0
psycopg2 2.9.6
whitenoise 6.4.0
typing-extensions 4.5.0
```

### Key Technologies
- **Backend**: Django 4.2.1
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Authentication**: Custom email-based authentication backend
- **Notifications**: Firebase Cloud Messaging (FCM)
- **WSGI Server**: Gunicorn
- **Static Files**: WhiteNoise

---

## 🔑 Key Features Implementation

### Authentication & Middleware
- **EmailBackEnd.py**: Custom authentication using email instead of username
- **LoginCheckMiddleWare.py**: Validates user sessions and redirects unauthorized access
- **ReCAPTCHA**: Google reCAPTCHA integration on login page for security

### Views Organization
The application is organized into role-based view modules:
- **views.py**: General authentication and demo views
- **HodViews.py**: 50+ endpoints for administrative functions
- **StaffViews.py**: 20+ endpoints for staff operations
- **StudentViews.py**: 15+ endpoints for student access

### Forms
- **AddStudentForm**: Complete student registration form
- **EditStudentForm**: Student profile editing form
- **EditResultForm**: Dynamic result editing form with subject filtering
- **DateInput**: Custom date input widget

---

## 📍 URL Routing

The application includes comprehensive URL patterns:

### Authentication Routes
- `/` - Login page
- `/signup_admin` - Admin registration
- `/signup_staff` - Staff registration
- `/signup_student` - Student registration
- `/doLogin` - Login processing
- `/logout_user` - Logout

### Admin Routes (40+ routes)
- `/admin_home` - Admin dashboard
- `/add_staff`, `/manage_staff`, `/edit_staff/<id>` - Staff management
- `/add_student`, `/manage_student`, `/edit_student/<id>` - Student management
- `/add_course`, `/manage_course`, `/edit_course/<id>` - Course management
- `/add_subject`, `/manage_subject`, `/edit_subject/<id>` - Subject management
- `/admin_view_attendance` - Attendance overview
- `/student_leave_view`, `/staff_leave_view` - Leave requests
- `/admin_send_notification_staff/student` - Send notifications

### Staff Routes (20+ routes)
- `/staff_home` - Staff dashboard
- `/staff_take_attendance` - Mark attendance
- `/staff_apply_leave` - Apply for leave
- `/staff_add_result` - Add student results
- `/start_live_classroom` - Start online class
- `/staff_all_notification` - View notifications

### Student Routes (15+ routes)
- `/student_home` - Student dashboard
- `/student_view_attendance` - Check attendance
- `/student_apply_leave` - Request leave
- `/student_view_result` - View marks
- `/join_class_room/<subject_id>/<session_id>` - Join online class
- `/student_all_notification` - View notifications

---

## 🔄 Commit History

The project has been actively developed with 20+ commits. Key development phases include:

| Commit | Date | Key Changes |
|--------|------|---|
| ca9c38da | Latest | Final project structure and features |
| d2ff5696 | Earlier | Core functionality implementation |
| 65a6b4cc | Earlier | Database model refinement |
| ec1bdd59 | Earlier | Authentication system |
| 5ecb22d8 | Earlier | View implementation |
| 29bf2857 | Earlier | Form creation and validation |
| 1f17a99d | Earlier | Attendance tracking |
| edc22504 | Earlier | Staff management |
| ea1db1a6 | Earlier | Student features |
| 74479bbe | Earlier | Leave management |
| c235546 | Earlier | Result management |
| b8707a89 | Earlier | Feedback system |
| 43eae5fa | Earlier | Notifications |
| df7e0670 | Earlier | Live classroom |
| 7f409fb4 | Earlier | UI improvements |
| 24cb9ed3 | Earlier | Bug fixes |
| 8d26c669 | Earlier | Performance optimization |
| f70401be | Earlier | Security enhancements |
| a2f72c5e | Earlier | Template updates |
| 162744d3 | Initial commit | Project initialization |

**Last Updated**: June 7, 2026, 06:58 UTC

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/Tyagi1337/CampusConnect.git
cd CampusConnect
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Application: `http://localhost:8000`
- Admin Panel: `http://localhost:8000/admin`

---

## 📝 Configuration

### Settings
Configure the following in `CampusConnect_system/settings.py`:
- Database connection
- Email backend for notifications
- Firebase credentials for FCM
- Google reCAPTCHA keys
- Static and media file paths

### Environment Variables
Create a `.env` file for sensitive information:
- `DATABASE_URL`
- `SECRET_KEY`
- `DEBUG`
- `FIREBASE_API_KEY`
- `RECAPTCHA_SECRET_KEY`

---

## 🔐 Security Features

- **Email Authentication**: Custom backend using email credentials
- **ReCAPTCHA Integration**: Protects login from automated attacks
- **CSRF Protection**: Django CSRF middleware enabled
- **Password Hashing**: Django's built-in password hashing
- **Session Management**: Secure session handling with middleware
- **Role-Based Access**: Different permissions for HOD, Staff, and Students

---

## 📱 Features in Detail

### Attendance System
- Staff marks attendance for each subject/class
- Students can view their attendance records
- Admin can generate attendance reports
- Bulk attendance updates available

### Results Management
- Staff inputs exam and assignment marks
- Students can view their results
- Admin can view all student results
- Editable result records for corrections

### Leave Management
- Students and staff can apply for leaves
- Admin reviews and approves/rejects requests
- Leave history tracking
- Notification on approval/rejection

### Communication System
- Feedback submission from students and staff
- Admin can reply to feedback
- Notification system for important updates
- Firebase push notifications support

### Live Classroom
- Staff can create and manage online classrooms
- Students can join using room name and password
- Session tracking and management
- Integration with video conferencing solutions

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Tyagi1337** - [GitHub Profile](https://github.com/Tyagi1337)

---

## 📞 Support

For support, issues, or questions:
- Open an issue on [GitHub Issues](https://github.com/Tyagi1337/CampusConnect/issues)
- Check existing documentation
- Review the code comments for implementation details

---

## 🎓 Use Cases

This system is ideal for:
- **Educational Institutions**: Schools and colleges managing multiple departments
- **Online Learning Platforms**: Tracking attendance and results
- **Academic Management**: Centralizing student and staff information
- **Communication Hub**: Streamlining admin-to-staff and admin-to-student communication
- **Performance Tracking**: Monitoring student progress and attendance

---

## 📊 Project Statistics

- **Total Commits**: 20+
- **Main Language**: JavaScript (91.7%)
- **Repository Size**: 25,839 KB
- **Database**: SQLite (Development) with PostgreSQL support
- **Views**: 75+ unique endpoints
- **Models**: 15+ database models
- **Status**: Active Development (Last updated: June 7, 2026)

---

## 🔜 Future Enhancements

Potential features for future releases:
- Mobile app (React Native/Flutter)
- Advanced analytics and reporting
- Integration with other institutional systems
- AI-based attendance verification
- Parent-teacher communication portal
- Course recommendation system
- Advanced search and filtering

---

**Happy Learning with CampusConnect! 🎉**
