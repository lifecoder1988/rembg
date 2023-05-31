import os
import json
import subprocess
import uuid

from PIL import Image
from io import BytesIO

def read2byte(path):
    '''
    图片转二进制
    path：图片路径
    byte_data：二进制数据
    '''
    with open(path,"rb") as f:
        byte_data = f.read()
    return byte_data

def handleEvent(event):
    url = event["url"]
    args = event["args"]
    filename = event["uuid"]

    tpl = '''curl -s "%s" | rembg i %s > /data/bg-input/%s.tmp && mv %s.tmp %s'''
    cmd = tpl %(url,args,filename,filename,filename)

    result = subprocess.run(cmd,shell=True)
    print(result)


if __name__ == '__main__':
    FC_EVENT = os.environ['FC_CUSTOM_CONTAINER_EVENT']
    print("Hello serverless image")
    print("FC event is: " + FC_EVENT)

    event = json.loads(FC_EVENT)
    handleEvent(event)

