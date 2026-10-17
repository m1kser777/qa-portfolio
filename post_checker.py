def check_post(text):
    problems = []
    paragraphs = text.split("\n")
    for p in paragraphs:
        p = p.strip()
        if p.endswith(".") and not p.endswith("..."):
            problems.append("Точка в конце абзаца: " + p[:30])
    if len(text) > 2200:
        problems.append("Пост длиннее 2200 символов: " + str(len(text)))
    return problems