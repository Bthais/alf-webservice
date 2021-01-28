
import json


class ExamsTemplates:
    exams_templates = []

    @staticmethod
    def __questions_validate(exam_template):
        total = 0
        exam_name = list(exam_template.keys())[0]
        for question1 in exam_template[exam_name]:
            total += question1["Peso"]
            if question1["Questao"] < 1:
                return {"codigo": 406,
                        "resposta": "Numero de questão inválida!"}
            if question1["Peso"] < 1:
                return {"codigo": 406,
                        "resposta": "Peso não pode ser menor que 1!"}
            for question2 in exam_template[exam_name]:
                if question1 != question2:
                    if question1["Questao"] == question2["Questao"]:
                        return {"codigo": 406,
                                "resposta": "Questões conflitantes!"}
        if total < 1 or total > 10:
            return {"codigo": 406,
                    "resposta": "Total da nota deve estar entre 1 e 10!"}

    def __validate_duplicity(self, exam_name):
        for exam in self.exams_templates:
            if exam_name in exam.keys():
                return {"codigo": 409,
                        "resposta": "Gabarito já existe!"}

    def insert(self, exam_template):
        response = self.__questions_validate(exam_template)
        if response is not None:
            return response
        response = self.__validate_duplicity(list(exam_template.keys())[0])
        if response is not None:
            return response
        self.exams_templates.append(exam_template)
        return {"codigo": 200,
                "resposta": "Gabarito inserido com sucesso!"}

    def question_exists(self, question_number, exam_name):
        current_exam = []
        for exam in self.exams_templates:
            if list(exam.keys())[0] == exam_name:
                current_exam = exam
        if len(current_exam) == 0:
            return False
        for question in current_exam[exam_name]:
            if question["Questao"] == question_number:
                return True
        return False




