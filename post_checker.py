BANNED = ["пишите в телеграм", "ссылка в профиле"]
def check_post(text):
    problems = []
    paragraphs = text.split("\n")
    for p in paragraphs:
        p = p.strip()
        if p.endswith(".") and not p.endswith("..."):
            problems.append("Точка в конце абзаца: " + p[:30])
    if len(text) > 2200:
        problems.append("Пост длиннее 2200 символов: " + str(len(text)))
    for phrase in BANNED:
        if phrase in text.lower():
            problems.append("Запрещённая фраза: " + phrase)
    return problems