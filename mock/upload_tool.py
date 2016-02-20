class UploadToolService(object):
    def __init__(self, rm_service):
        self._rm_service = rm_service

    def upload_complete(self, filename):
        self._rm_service.rm(filename)
