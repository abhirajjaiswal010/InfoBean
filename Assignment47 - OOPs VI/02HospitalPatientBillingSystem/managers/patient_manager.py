class PatientManager():
    def __init__(self):
        self.patients=[]

    def add_patient(self,patient):
        self.patients.append(patient)
    
    def search_patient(self,patient_id):
        
        for i in self.patients:
            if patient_id==i.patient_id:
                return i