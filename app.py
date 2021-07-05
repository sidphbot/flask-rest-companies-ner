from ner_app import create_ner_app

if __name__ == '__main__':
    ner_app = create_ner_app()
    ner_app.run(debug=False)