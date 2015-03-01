'''
Created on Feb 28, 2015

@author: robin
'''
#!/usr/bin/env python

import sys, json
from pprint import pprint

class FileReader(object):
    filename = ""
   
    def readFile(self, filename):
        with open(filename,'r') as f:
            data = f.readlines()
            
            for line in data:
                print line,
        
    def processSurvey(self, inputfile, outputfile):
        surveyques = open(inputfile, "r")
        responses = open(outputfile, "w")
        while True:
            text = surveyques.readline()
            pprint(text)
            if len(text) == 0:
                break;
            
            ques = raw_input(text)
            #json_string = json.dumps({'question':text, 'answer': ques}, responses,sort_keys=False,indent=2)
            #print json_string
            #print(ques)
            #responses.write(text)
            json.dump({'question':text, 'answer': ques}, responses, sort_keys = False, indent = 4, ensure_ascii = False)
            
        surveyques.close()
        responses.close()

    def __init__(self, filename):
        self.filename = sys.argv[0]
        
ques = FileReader("/Users/robin/Documents/workspace/survey_cli/src/resources/sample_survey.txt")
inputfile = "/Users/robin/Documents/workspace/survey_cli/src/resources/sample_survey.txt"
outputfile = "/Users/robin/Documents/workspace/survey_cli/src/resources/responses.json"
ques.processSurvey(inputfile, outputfile)
#print ques.filename
#ques.readFile("/Users/robin/Documents/workspace/survey_cli/src/resources/sample_survey.txt")