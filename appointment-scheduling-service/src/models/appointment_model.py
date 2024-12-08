class Appointment:
    def __init__(self, id, patient_id, doctor_id, time, notes=None):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.time = time
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "time": self.time,
            "notes": self.notes,
        }
