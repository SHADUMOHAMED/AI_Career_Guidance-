from flask import Flask, render_template, request

app = Flask(__name__)

# ================= ANSWER KEYS =================

cs_key = {
"q1":"A","q2":"B","q3":"B","q4":"A","q5":"B",
"q6":"C","q7":"D","q8":"B","q9":"B","q10":"C",
"q11":"C","q12":"A","q13":"B","q14":"A","q15":"D",
"q16":"A","q17":"A","q18":"C","q19":"C","q20":"A"
}

bio_key = {
"q1":"B","q2":"C","q3":"C","q4":"A","q5":"A",
"q6":"A","q7":"A","q8":"A","q9":"A","q10":"A",
"q11":"A","q12":"A","q13":"A","q14":"A","q15":"A",
"q16":"A","q17":"A","q18":"A","q19":"B","q20":"A"
}

com_key = {
"q1":"A","q2":"A","q3":"A","q4":"A","q5":"A",
"q6":"A","q7":"A","q8":"A","q9":"A","q10":"A",
"q11":"A","q12":"A","q13":"A","q14":"A","q15":"A",
"q16":"A","q17":"A","q18":"A","q19":"A","q20":"A"
}

# ================= COMMON RESULT FUNCTION =================

def calculate_result(answer_key, form_data):
    scores = [0,0,0,0]

    for i in range(1,21):
        if form_data.get(f"q{i}") == answer_key[f"q{i}"]:
            index = (i-1)//5
            scores[index] += 2

    total = sum(scores)
    percentage = (total/40)*100

    if percentage >= 90:
        performance = "Excellent"
    elif percentage >= 70:
        performance = "Good"
    else:
        performance = "Average"

    return scores, round(percentage,2), performance

# ================= HOME =================

@app.route('/')
def group():
    return render_template("group.html")

# ================= CS =================

@app.route('/cs_test')
def cs_test():
    return render_template("cs_test.html")

@app.route('/cs_result', methods=['POST'])
def cs_result():
    student_name = request.form.get("student_name")
    subjects = ["Computer Science","Mathematics","Physics","Chemistry"]

    scores, percentage, performance = calculate_result(cs_key, request.form)

    if percentage >= 90:
        degree = "B.Tech Computer Science Engineering"
        message = "Outstanding performance! You are highly suitable for core engineering programs."
    elif percentage >= 75:
        degree = "B.E IT / AI & Data Science"
        message = "Very good performance. You can pursue advanced technical fields."
    elif percentage >= 55:
        degree = "BCA / B.Sc Computer Science"
        message = "Good foundation. Improve skills to reach higher levels."
    elif percentage >= 40:
        degree = "Diploma in Computer Engineering"
        message = "Strengthen fundamentals before moving to major degrees."
    else:
        degree = "Skill-Based Programming Courses"
        message = "Focus on basic programming and problem solving skills."

    return render_template("result.html",
        group="Computer Science Group",
        student_name=student_name,
        subjects=subjects,
        scores=scores,
        degree=degree,
        percentage=percentage,
        performance=performance,
        message=message,
        degrees_list=["B.Tech CSE","AI & DS","BCA","Cyber Security","Software Engineering"]
    )

# ================= BIO =================

@app.route('/bio_test')
def bio_test():
    return render_template("bio_test.html")

@app.route('/bio_result', methods=['POST'])
def bio_result():
    student_name = request.form.get("student_name")
    subjects = ["Biology","Physics","Chemistry","Mathematics"]

    scores, percentage, performance = calculate_result(bio_key, request.form)

    if percentage >= 95:
        degree = "MBBS"
        message = "Excellent performance! You are strongly suitable for medical studies."
    elif percentage >= 75:
        degree = "BDS / Nursing"
        message = "Very good performance in life sciences."
    elif percentage >= 60:
        degree = "Biotechnology / Pharmacy"
        message = "Good potential in applied biological sciences."
    elif percentage >= 40:
        degree = "Allied Health Sciences"
        message = "Build stronger science fundamentals."
    else:
        degree = "Paramedical Skill Courses"
        message = "Improve core science knowledge before entering medical field."

    return render_template("result.html",
        group="Biology Group",
        student_name=student_name,
        subjects=subjects,
        scores=scores,
        degree=degree,
        percentage=percentage,
        performance=performance,
        message=message,
        degrees_list=["MBBS","BDS","Nursing","Biotechnology","Pharmacy"]
    )

# ================= COMMERCE =================

@app.route('/commerce_test')
def commerce_test():
    return render_template("commerce_test.html")

@app.route('/commerce_result', methods=['POST'])
def commerce_result():
    student_name = request.form.get("student_name")
    subjects = ["Accountancy","Business Studies","Economics","Mathematics"]

    scores, percentage, performance = calculate_result(com_key, request.form)

    if percentage >= 90:
        degree = "Chartered Accountant (CA)"
        message = "Excellent financial and analytical skills."
    elif percentage >= 70:
        degree = "B.Com Accounting & Finance"
        message = "Strong foundation in commerce subjects."
    elif percentage >= 55:
        degree = "BBA / B.Com General"
        message = "Good business understanding."
    elif percentage >= 40:
        degree = "Diploma in Business Management"
        message = "Strengthen commerce fundamentals."
    else:
        degree = "Basic Accounting Skill Courses"
        message = "Improve core business concepts first."

    return render_template("result.html",
        group="Commerce Group",
        student_name=student_name,
        subjects=subjects,
        scores=scores,
        degree=degree,
        percentage=percentage,
        performance=performance,
        message=message,
        degrees_list=["CA","B.Com","BBA","Finance","Economics"]
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)