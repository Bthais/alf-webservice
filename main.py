from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

from ExamsTemplates import ExamsTemplates
from StudentsAnswers import StudentsAnswers


class ApiHandler(BaseHTTPRequestHandler):
    exams_templates = ExamsTemplates()
    students_answers = StudentsAnswers(exams_templates)

    def __set_header(self):
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def __successful_response(self):
        self.send_response(200)
        self.__set_header()

    def __not_found_response(self):
        self.send_response(404)
        self.__set_header()

    def __not_acceptable_response(self):
        self.send_response(406)
        self.__set_header()

    def __conflict_response(self):
        self.send_response(409)
        self.__set_header()

    def __send_response_msg(self, response):
        self.wfile.write(bytes(json.dumps(response), "utf8"))

    def __resolve_response(self, response):
        if response["codigo"] == 200:
            self.__successful_response()
        elif response["codigo"] == 404:
            self.__not_found_response()
        elif response["codigo"] == 406:
            self.__not_acceptable_response()
        elif response["codigo"] == 409:
            self.__conflict_response()
        self.__send_response_msg(response)

    def __fill_json_messege(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        message = json.loads(post_data.decode('utf-8'))
        return message

    def do_GET(self):
        if self.path == "/alunos_aprovados":
            self.__successful_response()
            student = '{"name":"Joao", "score":"100"}'
            self.wfile.write(bytes(student, "utf8"))

        if self.path.startswith("/valida_respostas_aluno?aluno="):
            query_keys = parse_qs(urlparse(self.path).query)
            response = self.students_answers.validate_grade(query_keys["aluno"])
            self.__successful_response()
            self.__send_response_msg(response)

    def do_POST(self):
        if self.path == "/cadastra_gabarito":
            exam_template = self.__fill_json_messege()
            response = self.exams_templates.insert(exam_template)
            self.__resolve_response(response)

        if self.path == "/cadastra_respostas_aluno":
            student_answers = self.__fill_json_messege()
            response = self.students_answers.insert(student_answers)
            self.__resolve_response(response)


handler_object = ApiHandler
server_address = ('', 80)
my_server = HTTPServer(server_address, handler_object)
my_server.serve_forever()
