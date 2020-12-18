from aiohttp import web
from .config import db_block, web_routes, render_html


@web_routes.get("/grade")
async def view_list_grades(request):
    with db_block() as db:
        db.execute("""
        SELECT sn AS stu_sn, name as stu_name FROM student ORDER BY name
        """)
        students = list(db)

        db.execute("""
        SELECT sn AS cou_sn, name as cou_name FROM course ORDER BY name
        """)
        courses = list(db)

    return render_html(request, 'grade_list.html',
                       students=students,
                       courses=courses)


@web_routes.get('/grade/check/{stu_sn}/{cou_sn}')
async def edit_grade_action(request):
    stu_sn = request.match_info.get("stu_sn")
    cou_sn = request.match_info.get("cou_sn")
    stu_sn = int(stu_sn)
    cou_sn = int(cou_sn)
    print
    if cou_sn == 1:
        with db_block() as db:
            db.execute("""
            select student.name as stu_name, course.name as cou_name, grade
            from student,course,course_grade,courseplan
            where course_grade.stu_sn = student.sn and  course_grade.courseplan_sn = courseplan.sn and  courseplan.cou_sn= course.sn
            and course_grade.stu_sn = %(stu_sn)s;
            """,dict(stu_sn = stu_sn))
            items = list(db)
    else:
        with db_block() as db:
            db.execute("""
            select student.name as stu_name, course.name as cou_name, grade
            from student, course , course_grade,courseplan
            where course_grade.stu_sn = student.sn and  course_grade.courseplan_sn = courseplan.sn and course.sn = courseplan.cou_sn 
            and course_grade.stu_sn = %(stu_sn)s and course.sn = %(cou_sn)s;
            """,dict(stu_sn = stu_sn,cou_sn = cou_sn))
            items = list(db)
    return render_html(request, 'checkgrade.html',
                       items=items)