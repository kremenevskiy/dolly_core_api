from fastapi import HTTPException


class SubcriptionNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail='Subcription not found')
