# -*- coding: utf-8 -*-
"""Document QA Pipeline and Predictionipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aswx--oTCF3zyxOP5Sy5QGF4pZzoeEd9
"""

# !pip install 'git+https://github.com/facebookresearch/detectron2.git'

!pip install transformers datasets
!pip install torchvision
!pip install pytesseract
!sudo apt install tesseract-ocr

from google.colab import drive
drive.mount('/content/drive')

from datasets import Dataset, DatasetDict
import detectron2
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import datasets
class MyPipeline:
    def load_dataset(self, conf):
        #loading the saved dataset from our model
        saved_path = conf["parent_dir"] + "/" + "dataset"
        loaded_dataset = datasets.DatasetDict.load_from_disk(saved_path)
        return loaded_dataset


    def create_pipeline(self, conf):
        #creating pipeline using the tokenizer weights and model weights of our trained model
        model = AutoModelForQuestionAnswering.from_pretrained(conf["model_dir"])
        qa_pipeline = pipeline("document-question-answering", model= conf["parent_dir"] + "/" + "model")
        print("pipeline completed")
        return qa_pipeline

    def run(self, conf):
        loaded_dataset = self.load_dataset(conf)
        dataset = loaded_dataset["test"]
        image = dataset["image"][0]
        question = dataset["question"][0]
        pipeline = self.create_pipeline(conf)
        answer_dict = pipeline(image, question)
        print("The answer is:",answer_dict[0]['answer'])


conf = {}
conf["parent_dir"] = "/content/drive/MyDrive/Accure.ai/Document QA"
conf["model_dir"] = conf["parent_dir"] + "/" + "model"
conf["tokenizer"] = conf["parent_dir"] + "/" + "tokenizer"
pipeline_obj = MyPipeline()
pipeline_obj.run(conf)

