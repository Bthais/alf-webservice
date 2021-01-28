from ExamsTemplates import ExamsTemplates


class StudentsAnswers:
    students_answers = []
    exams_templates: ExamsTemplates

    def __init__(self, exams_templates: ExamsTemplates):
        self.exams_templates = exams_templates

    def __questions_validate(self, exam):
        exam_name = list(exam.keys())[0]
        question_count = 0
        total_questions = 0
        for question1 in exam[exam_name]:
            if total_questions == 0:
                total_questions = len(list(exam[exam_name]))
            if self.exams_templates.question_exists(question1["Questao"], exam_name):
                question_count += 1
            else:
                return {"codigo": 404,
                        "resposta": "Prova ou questão não encontrada!"}
            if question1["Questao"] < 1:
                return {"codigo": 406,
                        "resposta": "Numero de questão inválida!"}
            for question2 in exam[exam_name]:
                if question1 != question2:
                    if question1["Questao"] == question2["Questao"]:
                        return {"codigo": 409,
                                "resposta": "Questões conflitantes!"}

        if question_count != total_questions:
            return {"codigo": 409,
                    "resposta": "Número de questões conflitante!"}


    @staticmethod
    def __exams_validate(self, student_answers):
        student_name = list(student_answers.keys())[0]
        for exam1 in student_answers[student_name]:
            response = self.__questions_validate(exam1)
            if response is not None:
                return response
            for exam2 in student_answers[student_name]:
                if exam1 != exam2:
                    if list(exam1.keys())[0] == list(exam2.keys())[0]:
                        return {"codigo": 409,
                                "resposta": "Provas conflitantes!"}

    def __validate_duplicity(self, studant_name):
        for student in self.students_answers:
            if studant_name in student.keys():
                return {"codigo": 409,
                        "resposta": "Respostas referentes ao aluno já existem!"}

    def __validate_max_100(self):
        if len(list(self.students_answers)) > 100:
            return {"codigo": 406,
                    "resposta": "Número máximo de alunos atingido!"}

    def insert(self, student_answers):
        response = self.__exams_validate(self, student_answers)
        if response is not None:
            return response
        response = self.__validate_duplicity(list(student_answers.keys())[0])
        if response is not None:
            return response
        self.students_answers.append(student_answers)
        return {"codigo": 200,
                "resposta": "Respostas do aluno inseridas com sucesso!"}

    def validate_grade(self, student_name):
        student_index = -1
        for student in self.students_answers:
            student_index += 1
            if student_name == list(student.keys())[0]:
                quit()
        response = {"Resultado do aluno": []}
        template_index = -1
        template_name = ""
        for exam in self.students_answers[student_index]:
            for exam_template in self.exams_templates.exams_templates:
                template_index += 1
                template_name = list(exam_template.keys())[0]
                if list(exam.keys())[0] == template_name:
                    quit()
            exam_result = 0
            for template_question in self.exams_templates.exams_templates[template_index]:
                for exam_question in self.students_answers[student_index]:
                    if exam_question["Questao"] == template_question["Qestao"]:
                        if exam_question["Resposta"] == template_question["Resposta"]:
                            exam_result += template_question["Peso"]
            response["Resultado do aluno"].append({template_name: exam_result})
        return response
