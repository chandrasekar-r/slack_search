from flask import render_template, request, jsonify
from slack_api import fetch_messages_from_all_channels  # Update this line
from message_processor import process_messages, store_questions_answers
from search_engine import search_questions
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = search_questions(query)
    return jsonify(results)


if __name__ == '__main__':
    messages = fetch_messages_from_all_channels()  # Update this line
    questions_answers = process_messages(messages)
    store_questions_answers(questions_answers)
    app.run(debug=True)
