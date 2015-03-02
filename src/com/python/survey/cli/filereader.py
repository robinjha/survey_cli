'''
Created on Feb 28, 2015

@author: robin
'''
#!/usr/bin/env python

import sys, json, collections
from pprint import pprint
class FileReader(object):
    filename = ""
    '''
    def locateByName(self, e, name):
        if e.get('name', None) == name:
            return e

        for child in e.get('children', []):
            result = locateByName(child, name)
            if result is not None:
                return result

        return None
    
    def nested_dict_iter(self, nested):
        for key, value in nested.iteritems():
            if isinstance(value, collections.Mapping):
                for inner_key, inner_value in self.nested_dict_iter(value):
                    yield inner_key, inner_value
                    print(inner_key, inner_value)
            else:
                yield key, value 
                print(key, value)           
    '''  
    def nestedJSON(self, d, responses):
        for k, v in d.iteritems():
            if isinstance(v, dict):
                self.nestedJSON(v, responses)
            elif(k == 'choices'):
                for s in v:
                    print s
            else:
                print "{0} : {1}".format(k, v)
                
        choice = raw_input("Please enter your choice : ")
        json.dump({'question': v,'answer':choice}, responses, indent = 4, ensure_ascii = False)
        
         
    def processSurvey(self, inputfile, outputfile):
        surveyques = open(inputfile, "r")
        responses = open(outputfile, "w")
        while True:
            try:
                text = json.load(surveyques) 
                #json_string = json.dumps(text, sort_keys=True, indent = 2)
                #print(json_string)
                questions = text['questions']
                print("No of questions: " , len(questions)) # find out how many questions are in the survey
                #pprint(questions[2])
                for item in questions:
                    self.nestedJSON(item, responses)
                    #print("#####printing item#######")
                    #print(item)
                    
                    #if(item.has_key('choices')):
                    #    self.nestedJSON(item, responses)
                    #else:
                    #    print(item["question"])
                    #choice = raw_input("Please enter your choice : ")
                    #json.dump({'question': item["question"],'answer':choice}, responses, indent = 4, ensure_ascii = False)
        
                            
                    '''   
                    #self.nested_dict_iter(item)
                    if "qu" in item:
                        print("#################")
                        ques = raw_input("Q: "+item["question"]+" \nA: ")
                        json.dump({'question':item["question"], 'answer':ques}, responses, indent = 4, ensure_ascii = False)
                    '''
                break
                    
            except ValueError:
                continue
            else:
                surveyques.close()
                responses.close()
        #surveyques.close()
        #responses.close()

    def __init__(self, filename):
        self.filename = sys.argv[0]
        
ques = FileReader("/Users/robin/Documents/workspace/survey_cli/src/resources/sample_survey.json")
inputfile = "/Users/robin/Documents/workspace/survey_cli/src/resources/sample_survey.json"
outputfile = "/Users/robin/Documents/workspace/survey_cli/src/resources/responses.json"
ques.processSurvey(inputfile, outputfile)
#print ques.filename
#ques.readFile("/Users/robin/Documents/workspace/survey_cli/src/resources/sample_survey.txt")
