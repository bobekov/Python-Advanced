def students_credits(*args):
    sum_credits = 0
    subject = {}
    for info in args:
        course_name, credits, max_test_points, diyan_points = info.split("-")
        percent = int(diyan_points) / int(max_test_points)
        credit_course = int(credits) * percent
        sum_credits += credit_course
        subject[course_name] = credit_course

    final_result = []
    if sum_credits >= 240:
        final_result.append(f"Diyan gets a diploma with {sum_credits:.1f} credits.")
    else:
        final_result.append(f"Diyan needs {240 - sum_credits:.1f} credits more for a diploma.")

    sort_subject = sorted(subject.items(), key=lambda x: -x[1])
    for name, points in sort_subject:
        final_result.append(f"{name} - {points:.1f}")

    return '\n'.join(final_result)