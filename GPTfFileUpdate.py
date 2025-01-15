from __future__ import annotations
from yandex_cloud_ml_sdk import YCloudML

class CodeAnalyzer:
    messages = [
        {
            "role": "user",
            "text": """Ты выступаешь в роли эксперта в программировании, специализирующегося на анализе кода и оптимизации структуры проектов. Твоя задача:
            1.	Анализировать предоставленный код и файловую структуру.
            2.	Определить слабые места, дублирование кода, неоптимальные паттерны, проблемы с читаемостью или масштабируемостью.
            3.	Предложить конкретные улучшения с объяснением, почему они необходимы.


        Вот часть кода, который нужно проанализировать:
        {code}

        Пожалуйста, приведи подробный анализ и рекомендации, включая пример исправленного кода, если это возможно.""",
        },
    ]

    def __init__(self, code: str):
        self.messages[0]['text'] = self.messages[0]['text'].format(code=code)

    def ask(self, folder_id: str, auth: str):
        sdk = YCloudML(folder_id=folder_id, auth=auth)
        result = (
            sdk.models.completions("yandexgpt").configure(temperature=0.5).run(self.messages)
        )

        for alternative in result:
            print(alternative.text)

