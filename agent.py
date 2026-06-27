# agent.py

from openai import OpenAI
import json
from pypdf import PdfReader
from system_prompt import system_prompt
import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)


def push(text):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message":text
        }
    )

def record_user_details(email, name="Non fourni", context="Non fourni"):
    message = (
        f"👤 Nouveau contact\n"
        f"━━━━━━━━━━━━━━━\n"
        f"Nom     : {name}\n"
        f"Email   : {email}\n"
        f"━━━━━━━━━━━━━━━\n"
        f"Contexte: {context}\n"
    )
    push(message)
    return {"recorded": "ok"}


record_user_details_json = {
    "name": "record_user_details",
    "description": "Enregistre les coordonnées d'un utilisateur qui souhaite être contacté par Godwill. À appeler dès qu'un email est fourni, avec un contexte précis et détaillé de la raison du contact.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "L'adresse email de l'utilisateur"
            },
            "name": {
                "type": "string",
                "description": "Le nom de l'utilisateur s'il l'a fourni"
            },
            "context": {
                "type": "string",
                "description": "Résumé précis et détaillé du contexte : pourquoi contacte-t-il Godwill ? Quelle question a posé ? Quel type d'opportunité ? Que recherche-t-il ?"
            }
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

tools = [
    {"type":"function","function": record_user_details_json},
]




class Me:

    def __init__(self) -> None:
        self.openai = OpenAI()
        self.name = "Godwill Alexis AGUEMON"
        reader = PdfReader("cv.pdf")
        self.linkedin = ""
        for page in reader.pages:
            if page:
                self.linkedin += page.extract_text()
        with open("summary.txt","r",encoding="utf-8") as f:
            self.summary = f.read()
        self.system_prompt = system_prompt(self.linkedin,self.summary)
    
    def handle_tool_call(self, tool_calls) -> list:
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            tool = globals().get(tool_name)
            result = tool(**arguments) if tool else {}
            results.append({"role":"tool","content":json.dumps(result),"tool_call_id":tool_call.id})
        return results
    
    def chat(self,message,history):
        messages = [{"role":"system","content": self.system_prompt}] + history + [{"role":"user","content":message}]
        done = False
        while not done:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=tools
                )
            if response.choices[0].finish_reason == "tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                result = self.handle_tool_call(tool_calls)
                messages.append(message)
                messages.extend(result)
            else:
                done = True
        return response.choices[0].message.content
