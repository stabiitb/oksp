from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intime = models.DateTimeField(blank=True, null=True)
    outtime = models.DateTimeField(blank=True, null=True)


class Member(models.Model):
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    HOSTELS = (
        ('Hostel 1', 'Hostel 1'),
        ('Hostel 2', 'Hostel 2'),
        ('Hostel 3', 'Hostel 3'),
        ('Hostel 4', 'Hostel 4'),
        ('Hostel 5', 'Hostel 5'),
        ('Hostel 6', 'Hostel 6'),
        ('Hostel 7', 'Hostel 7'),
        ('Hostel 8', 'Hostel 8'),
        ('Hostel 9', 'Hostel 9'),
        ('Hostel 10', 'Hostel 10'),
        ('Hostel 11', 'Hostel 11'),
        ('Hostel 12', 'Hostel 12'),
        ('Hostel 13', 'Hostel 13'),
        ('Hostel 14', 'Hostel 14'),
        ('Hostel 15', 'Hostel 15'),
        ('Tansa', 'Tansa'),
        ('QIP', 'QIP')
    )
    DEPARTMENT = (
        ('Aerospace Engineering', 'Aerospace Engineering'),
        ('Animation', 'Animation'),
        ('Application Software Centre', 'Application Software Centre'),
        ('Applied Geophysics', 'Applied Geophysics'),
        ('Applied Statistics and Informatics', 'Applied Statistics and Informatics'),
        ('Biomedical Engineering', 'Biomedical Engineering'),
        ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'),
        ('Biotechnology', 'Biotechnology'),
        ('Centre for Aerospace Systems Design and Engineering', 'Centre for Aerospace Systems Design and Engineering'),
        ('Centre for Distance Engineering Education Programme', 'Centre for Distance Engineering Education Programme'),
        ('Centre for Environmental Science and Engineering', 'Centre for Environmental Science and Engineering'),
        ('Centre for Formal Design and Verification of Software',
         'Centre for Formal Design and Verification of Software'),
        ('Centre for Research in Nanotechnology and Science', 'Centre for Research in Nanotechnology and Science'),
        ('Centre for Technology Alternatives for Rural Areas', 'Centre for Technology Alternatives for Rural Areas'),
        ('Centre for Urban Science and Engineering', 'Centre for Urban Science and Engineering'),
        ('Centre of Studies in Resources Engineering', 'Centre of Studies in Resources Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Chemistry', 'Chemistry'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Climate Studies', 'Climate Studies'),
        ('Computer Centre', 'Computer Centre'),
        ('Computer Science & Engineering', 'Computer Science & Engineering'),
        ('Continuing Education Programme', 'Continuing Education Programme'),
        ('Corrosion Science and Engineering', 'Corrosion Science and Engineering'),
        ('Desai Sethi Centre for Entrepreneurship', 'Desai Sethi Centre for Entrepreneurship'),
        ('Earth Sciences', 'Earth Sciences'),
        ('Educational Technology', 'Educational Technology'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Energy Science and Engineering', 'Energy Science and Engineering'),
        ('Humanities & Social Science', 'Humanities & Social Science'),
        ('IITB-Monash Research Academy', 'IITB-Monash Research Academy'),
        ('Industrial Design Centre', 'Industrial Design Centre'),
        ('Industrial Design Centre', 'Industrial Design Centre'),
        ('Industrial Engineering and Operations Research', 'Industrial Engineering and Operations Research'),
        ('Industrial Management', 'Industrial Management'),
        ('Interaction Design', 'Interaction Design'),
        ('Kanwal Rekhi School of Information Technology', 'Kanwal Rekhi School of Information Technology'),
        ('Material Science', 'Material Science'),
        ('Materials, Manufacturing and Modelling', 'Materials, Manufacturing and Modelling'),
        ('Mathematics', 'Mathematics'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Metallurgical Engineering & Materials Science', 'Metallurgical Engineering & Materials Science'),
        ('Mobility and Vehicle Design', 'Mobility and Vehicle Design'),
        ('National Centre for Aerospace Innovation and Research',
         'National Centre for Aerospace Innovation and Research'),
        ('National Centre for Mathematics', 'National Centre for Mathematics'),
        ('Physical Education', 'Physical Education'),
        ('Physics', 'Physics'),
        ('Physics, Material Science', 'Physics, Material Science'),
        ('Preparatory Course', 'Preparatory Course'),
        ('Reliability Engineering', 'Reliability Engineering'),
        ('Shailesh J. Mehta School of Management', 'Shailesh J. Mehta School of Management'),
        ('Sophisticated Analytical Instrument Facility', 'Sophisticated Analytical Instrument Facility'),
        ('Systems and Control Engineering', 'Systems and Control Engineering'),
        ('Tata Center for Technology and Design', 'Tata Center for Technology and Design'),
        ('Visual Communication', 'Visual Communication'),
        ('Wadhwani Research Centre for Bioengineering', 'Wadhwani Research Centre for Bioengineering'),
    )
    JOIN_YEAR = (
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
    )
    GRAD_YEAR = (
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.CharField(max_length=9, blank=True, null=True)
    STATUS = (
        ('IN', 'IN'),
        ('OUT', 'OUT')
    )
    DEGREE = (
        ('Bachelor of Technology', 'Bachelor of Technology'),
        ('Master of Technology', 'Master of Technology'),
        ('B.Tech. + M.Tech. Dual Degree', 'B.Tech. + M.Tech. Dual Degree'),
        ('Master of Science', 'Master of Science'),
        ('Doctor of Philosophy', 'Doctor of Philosophy'),
        ('Bachelor of Design', 'Bachelor of Design'),
        ('Master of Design', 'Master of Design'),
        ('Master of Philosophy', 'Master of Philosophy'),
        ('Master of Management', 'Master of Management'),
        ('M.S. (Exit Degree)', 'M.S. (Exit Degree)'),
        ('Master of Technology (Exit Degree)', 'Master of Technology (Exit Degree)'),
        ('M.Tech. + Ph.D. Dual Degree', 'M.Tech. + Ph.D. Dual Degree'),
        ('Preparatory Course', 'Preparatory Course'),
        ('Visiting Student', 'Visiting Student'),
        ('Master of Philosophy (Exit Degree)', 'Master of Philosophy (Exit Degree)'),
        ('Master of Science (Exit Degree)', 'Master of Science (Exit Degree)'),
        # ('M.Sc. + M.Tech. Dual Degree', 'M.Sc. + M.Tech. Dual Degree'),
        ('M.Sc. + Ph.D. Dual Degree', 'M.Sc. + Ph.D. Dual Degree'),
        ('M.Phil. + Ph.D. Dual Degree', 'M.Phil. + Ph.D. Dual Degree'),
        ('Executive MBA', 'Executive MBA'),
        ('Four Year BS', 'Four Year BS'),
        ('Integrated M.Tech.', 'Integrated M.Tech.'),
        ('Master of Science By Research', 'Master of Science By Research'),
        ('Two Year M.Sc.', 'Two Year M.Sc.'),
        ('Five Year Integrated M.Sc.', 'Five Year Integrated M.Sc.'),
        ('D.I.I.T.', 'D.I.I.T.'),
        ('D.I.T.T. (Exit Degree)', 'D.I.T.T. (Exit Degree)'),
       )
    sex = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=12, blank=True, null=True)
    hostel = models.CharField(max_length=20, blank=True, null=True, choices=HOSTELS)
    room = models.CharField(max_length=5, blank=True, null=True)
    discipline = models.CharField(max_length=100, blank=True, null=True, choices=DEPARTMENT)
    join_year = models.CharField(max_length=4, blank=True, null=True, choices=JOIN_YEAR)
    graduation_year = models.CharField(max_length=4, blank=True, null=True, choices=GRAD_YEAR)
    degree = models.CharField(max_length=50, blank=True, null=True, choices=DEGREE)
    current_status = models.CharField(max_length=5, blank=True, null=True, choices=STATUS)
    current_log = models.ForeignKey(Log, on_delete=models.SET_NULL, blank=True, null=True)
    secondary_email = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='/static')
    access_token = models.TextField()

