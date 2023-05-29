import os

if __name__ == '__main__':
    FC_EVENT = os.environ['FC_CUSTOM_CONTAINER_EVENT']
    print("Hello serverless image")
    print("FC event is: " + FC_EVENT)