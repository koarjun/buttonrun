from flask_restful import Resource


class RunJobApi(Resource):
    def __init__(self):
        self.files_to_profile = None

    def post(self):
        print('POST EXECUTED')
        return {"data": "12345", "status": "success"}
    
    def get(self, job_name):
        # MAKING CODE SLEEP TO TEST LOADER IN THE FRONTEND 
        import time
        time.sleep(3)
        print('GET EXECUTED for job %s' % job_name)
        return {"data": "54321", "status": "success"}