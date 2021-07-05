from ner_app.utils import words_to_companies

from flask import jsonify
from flask_restful import Resource, reqparse


class ScanText(Resource):
    """A flask restful API resource class for extracting company names from a given text"""

    def __init__(self, ner):
        """:param ner:pipeline object initializes ner engine with the given pipeline object"""
        self.ner = ner

    def extract_companies(self, text):
        """scan for extracting company names
        :param ner:pipeline object, pretrained named entity recognition transformer pipeline
        :param text:str, text to scan for extracting company names

        :return either of the below,
        - a python dict object of company names as keys and respective scores as values, or,
        - a python dict object of string "Error" as key and "no companies found" as value
        """
        result = self.ner(text)
        words = [entry["word"] for entry in result if entry["entity"] == "I-ORG"]
        scores = [entry["score"] for entry in result if entry["entity"] == "I-ORG"]
        confidences, names = words_to_companies(scores, words)
        if len(names) < 1:
            return {"Error": "no companies found"}
        return dict(zip(names, confidences))

    def post(self):
        """API post function"""
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        text = parser.parse_args()["text"]
        if text == "":
            company_names = {"Error": "empty text"}
        else:
            company_names = self.extract_companies(text)  # no persistence assumed

        # build API response object
        resp = jsonify(company_names)
        if "Error" not in str(company_names):
            resp.status_code = 200
        else:
            resp.status_code = 400

        return resp
