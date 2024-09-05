import sys
import json
import fastjsonschema
#import os
#os.chdir('/home/michall/Desktop/testy_tmp/json_schema/podtest')
# dwa argumenty pierwszy to oczekiwany schemat jsona drugi to json ktory chcemy sprawdzic czy do schematu pasuje
schemat = json.load(open(sys.argv[1]))
validate = fastjsonschema.compile(schemat)

analizowany_json = json.load(open(sys.argv[2]))

print(validate(analizowany_json))
