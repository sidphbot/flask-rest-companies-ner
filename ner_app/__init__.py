from .resouces.ScanText import ScanText

from flask import Flask
from flask_restful import Api


def create_ner_app():
    """
    app factory for company name extraction REST API

    :return app: flask app object
    """

    # initialize ner pipeline (pre-trained) - from hugging face transformers
    # - may use custom ner pipeline object generation function with custom checkpoints
    from transformers import pipeline

    ner_pipeline = pipeline("ner", framework='pt')

    # create flask app
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ScanText, "/", resource_class_kwargs={"ner": ner_pipeline})

    return app


if __name__ == "__main__":
    ner_app = create_ner_app()
    ner_app.run(debug=False)
