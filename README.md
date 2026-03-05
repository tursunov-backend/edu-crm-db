# Education Center ERP System

An **ERP (Enterprise Resource Planning) system** designed for managing the operations of an education center.

This system centralizes core educational workflows including:

* student management
* teacher management
* course organization
* group scheduling
* enrollment management
* payment tracking

The goal of the project is to demonstrate **clean domain modeling**, **object-oriented architecture**, and **real-world education management workflows**.

---

# System Overview

The ERP system manages the lifecycle of students and courses inside an education center.

Main workflow:

1. Admin creates courses
2. Teachers are assigned to courses
3. Groups are created for specific courses
4. Students register in the system
5. Students enroll in groups
6. Lessons are scheduled
7. Payments are recorded
8. Student progress is tracked

---

# Domain Objects

The system is built around the following core entities.

| Object     | Description                                             |
| ---------- | ------------------------------------------------------- |
| Student    | Represents a student registered in the education center |
| Teacher    | Represents an instructor who teaches courses            |
| Course     | Represents an educational course                        |
| Group      | A class group assigned to a course and teacher          |
| Enrollment | Represents a student joining a group                    |
| Lesson     | Represents a scheduled lesson for a group               |
| Payment    | Represents a payment made by a student                  |

---

# Data Model

## Student

Represents a student enrolled in the education center.

### Fields

| Field      | Type     | Description               |
| ---------- | -------- | ------------------------- |
| id         | int      | Unique student identifier |
| first_name | str      | Student first name        |
| last_name  | str      | Student last name         |
| phone      | str      | Contact phone number      |
| email      | str      | Email address             |
| created_at | datetime | Registration date         |

### Methods

| Method         | Description                    |
| -------------- | ------------------------------ |
| register()     | Registers a new student        |
| enroll_group() | Enrolls student in a group     |
| make_payment() | Records a payment for a course |
| view_courses() | Displays enrolled courses      |

---

## Teacher

Represents an instructor responsible for teaching courses.

### Fields

| Field          | Type | Description               |
| -------------- | ---- | ------------------------- |
| id             | int  | Unique teacher identifier |
| first_name     | str  | Teacher first name        |
| last_name      | str  | Teacher last name         |
| phone          | str  | Contact phone number      |
| specialization | str  | Teacher specialization    |

### Methods

| Method          | Description                        |
| --------------- | ---------------------------------- |
| assign_course() | Assigns teacher to a course        |
| view_groups()   | Shows groups taught by the teacher |
| create_lesson() | Creates lesson schedule            |

---

## Course

Represents a course offered by the education center.

### Fields

| Field       | Type  | Description              |
| ----------- | ----- | ------------------------ |
| id          | int   | Unique course identifier |
| name        | str   | Course name              |
| description | str   | Course description       |
| duration    | int   | Course duration in weeks |
| price       | float | Course price             |

### Methods

| Method          | Description                |
| --------------- | -------------------------- |
| create_course() | Adds a new course          |
| update_course() | Updates course information |
| delete_course() | Removes a course           |

---

## Group

Represents a class group within a course.

### Fields

| Field      | Type | Description                |
| ---------- | ---- | -------------------------- |
| id         | int  | Unique group identifier    |
| course_id  | int  | Associated course          |
| teacher_id | int  | Assigned teacher           |
| start_date | date | Group start date           |
| capacity   | int  | Maximum number of students |

### Methods

| Method           | Description                    |
| ---------------- | ------------------------------ |
| create_group()   | Creates a new group            |
| add_student()    | Adds student to the group      |
| remove_student() | Removes student from the group |

---

## Enrollment

Represents the relationship between students and groups.

### Fields

| Field       | Type     | Description       |
| ----------- | -------- | ----------------- |
| id          | int      | Unique identifier |
| student_id  | int      | Student reference |
| group_id    | int      | Group reference   |
| enrolled_at | datetime | Enrollment date   |

---

## Lesson

Represents a scheduled lesson for a group.

### Fields

| Field      | Type     | Description              |
| ---------- | -------- | ------------------------ |
| id         | int      | Unique lesson identifier |
| group_id   | int      | Associated group         |
| teacher_id | int      | Lesson instructor        |
| date       | datetime | Lesson date              |
| topic      | str      | Lesson topic             |

### Methods

| Method            | Description                |
| ----------------- | -------------------------- |
| schedule_lesson() | Creates lesson schedule    |
| update_lesson()   | Updates lesson information |
| cancel_lesson()   | Cancels lesson             |

---

## Payment

Represents payments made by students.

### Fields

| Field      | Type     | Description               |
| ---------- | -------- | ------------------------- |
| id         | int      | Unique payment identifier |
| student_id | int      | Student reference         |
| group_id   | int      | Group reference           |
| amount     | float    | Payment amount            |
| paid_at    | datetime | Payment date              |

### Methods

| Method           | Description               |
| ---------------- | ------------------------- |
| make_payment()   | Records a student payment |
| refund_payment() | Processes a refund        |

---

# Entity Relationships

```
Student
 └── Enrollment
        └── Group
              └── Course

Teacher
 └── Group
        └── Lesson

Student
 └── Payment
        └── Group
```

Relationship summary:

| Relationship         | Type        |
| -------------------- | ----------- |
| Course → Group       | One-to-Many |
| Teacher → Group      | One-to-Many |
| Group → Lesson       | One-to-Many |
| Student → Enrollment | One-to-Many |
| Group → Enrollment   | One-to-Many |
| Student → Payment    | One-to-Many |

---

# Student Enrollment Flow

1. Student registers in the system
2. Admin creates course
3. Admin creates group for the course
4. Teacher is assigned to the group
5. Student enrolls in the group
6. Lessons are scheduled
7. Student makes payments
8. System tracks attendance and progress

---

# Example Usage (Conceptual)

```python
student = Student.register(
    first_name="Ali",
    last_name="Karimov"
)

course = Course.create_course(
    name="Python Backend",
    duration=16,
    price=300
)

group = Group.create_group(
    course=course,
    capacity=20
)

student.enroll_group(group)

student.make_payment(amount=300)
```
