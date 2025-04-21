import json

class Teacher:
    def __init__(info, questions, answers, image=None):
        info.questions = questions
        info.answers = answers
        info.image = image
    
    def display_info(info):
        return f"{info.questions} {info.answers}"
    
    def to_dict(info):
        return {"questions": info.questions, "answers": info.answers, "image": info.image}