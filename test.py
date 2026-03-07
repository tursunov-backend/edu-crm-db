from db.session import get_session
from db.services.users import UserService
from db.services.students import StudentService


session = get_session()
user_service = UserService(session)
student_service = StudentService(session)


# user_service.register('ali', '1234', 'student')

user = user_service.get_user_by_username('ali')
# print(user.hashed_password)

# print(user_service.valid_password(user, '12345'))

# username = input('username: ')
# password = input('password: ')
# user = user_service.authenticate(username, password)
# if user:
#     print('yes')
# else:
#     print('no')

# student_service.create_student(user, 'Ali', 'Valiyev', '901231212')
# print(user.student_profile.last_name)

