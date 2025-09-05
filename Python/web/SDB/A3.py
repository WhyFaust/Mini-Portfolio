import sqlite3

def get_question_after(question_id=0, quiz_id=1):
    '''
    возвращает следующий вопрос после вопроса с переданным id
    для первого вопроса передаётся значение по умолчанию
    '''
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id
    '''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    conn.close()
    return result