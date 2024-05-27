def gather_credits(credit_num, *course_data):
    sum_credit = 0
    courses = []

    for name, credit in course_data:
        if sum_credit >= credit_num:
            break
        if name in courses:
            continue
        courses.append(name)
        sum_credit += credit

    if sum_credit >= credit_num:
        return f"""Enrollment finished! Maximum credits: {sum_credit}.
Courses: {', '.join(sorted(courses))}"""
    return f"You need to enroll in more courses! You have to gather {credit_num - sum_credit} credits more."
