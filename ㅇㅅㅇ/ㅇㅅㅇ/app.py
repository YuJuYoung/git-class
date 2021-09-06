from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    cnt = sqlite3.connect('topics.db')
    sql = 'SELECT title FROM topic'
    result = cnt.execute(sql)
    titles = result.fetchall()

    title_list = '<ol>'
    for title in titles:
        title_list += f'<li>{title[0]}</li>'
    title_list += '</ol>'

    return f'<h1>ㅇㅅㅇ</h1>{title_list}'

app.run(debug=True)