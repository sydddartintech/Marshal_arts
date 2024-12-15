# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arts(models.Model):
    artsid = models.AutoField(primary_key=True)
    artsname = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'arts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    bank_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    expiry = models.CharField(max_length=200)
    cvv = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bank'


class Booking(models.Model):
    bookid = models.AutoField(primary_key=True)
    fk_reg_id = models.IntegerField()
    fk_master_id = models.IntegerField()
    fk_package_id = models.IntegerField()
    booking_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'booking'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    feedid = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sender = models.CharField(max_length=200)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'feedback'


class ForgotPassword(models.Model):
    forgot_password_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    random_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forgot_password'


class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=200)
    password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'login'


class Master(models.Model):
    master_id = models.AutoField(primary_key=True)
    fk_art_id = models.IntegerField()
    full_name = models.CharField(max_length=200)
    profile = models.TextField()
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'master'


class Package(models.Model):
    packgeid = models.AutoField(primary_key=True)
    package_title = models.CharField(max_length=200)
    fk_arts_id = models.IntegerField()
    duration = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'package'


class Reg(models.Model):
    reg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    usertype = models.CharField(max_length=50)
    doj = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg'


class Scheduling(models.Model):
    scheduleid = models.AutoField(primary_key=True)
    time_from = models.CharField(max_length=50)
    time_to = models.CharField(max_length=50)
    date = models.DateField()
    fk_package_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scheduling'


class Studentfee(models.Model):
    feeid = models.AutoField(primary_key=True)
    fk_book_id = models.IntegerField()
    amount = models.IntegerField()
    due_date = models.DateField()
    pay_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'studentfee'


class VideoTips(models.Model):
    tips_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.TextField()
    fk_arts_id = models.IntegerField()
    fk_master_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'video_tips'
