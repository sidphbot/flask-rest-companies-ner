from ner_app import create_ner_app

app = create_ner_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')