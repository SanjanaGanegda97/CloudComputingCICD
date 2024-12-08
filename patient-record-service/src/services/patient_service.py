from models.patient_model import Patient

class PatientService:
    def __init__(self):
        self.patients = {}

    def create_patient(self, data):
        if "id" not in data:
            return {"error": "Patient ID is required"}, 400
        if data["id"] in self.patients:
            return {"error": "Patient ID already exists"}, 400
        patient = Patient(**data)
        self.patients[patient.id] = patient
        return {"message": "Patient created", "id": patient.id}

    def get_patient(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            return patient.to_dict()
        return {"error": "Patient not found"}, 404

    def get_all_patients(self):
        return [patient.to_dict() for patient in self.patients.values()]

    def update_patient(self, patient_id, data):
        patient = self.patients.get(patient_id)
        if not patient:
            return {"error": "Patient not found"}, 404
        for key, value in data.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        self.patients[patient_id] = patient
        return {"message": "Patient updated", "id": patient.id}

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            return {"message": "Patient deleted"}
        return {"error": "Patient not found"}, 404
