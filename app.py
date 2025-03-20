from flask import Flask, jsonify


todo = Flask('__name__')

students = [
        {
            'id': 1,
            'student_name': 'Akshaya K',
            'age': 20,
            'email':'akshayak@gmail.com'
        },
        {
            'id':2,
            'student_name': 'Bhavya D',
            'age': 20,
            'email': 'bhavya@gmail.com'
        },
        {
            'id':3,
            'student_name': 'Kavya G',
            'age': 19,
            'email': 'kavya@gmail.com'
        },
{
            'id':4,
            'student_name': 'Kusuma G',
            'age': 20,
            'email': 'kusuma@gmail.com'
        },
    ]


@todo.route('/students-list')
def students_list():
    return jsonify(students)


@todo.route('/student/get/<int:id>')
def student_get_by_id(id):
    for std in students:
        if std['id'] == id:
            return jsonify(std)

    return "id not found"



if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )