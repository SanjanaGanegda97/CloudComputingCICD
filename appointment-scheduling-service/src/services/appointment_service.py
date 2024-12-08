from models.appointment_model import Appointment

class AppointmentService:
    def __init__(self):
        self.appointments = {}

    def create_appointment(self, data):
        if "id" not in data:
            return {"error": "Appointment ID is required"}, 400
        if data["id"] in self.appointments:
            return {"error": "Appointment ID already exists"}, 400

        appointment = Appointment(**data)
        self.appointments[appointment.id] = appointment
        return {"message": "Appointment created", "id": appointment.id}

    def get_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            return appointment.to_dict()
        return {"error": "Appointment not found"}, 404

    def get_appointments_by_doctor(self, doctor_id):
        result = [
            appointment.to_dict()
            for appointment in self.appointments.values()
            if appointment.doctor_id == doctor_id
        ]
        return result

    def get_all_appointments(self):
        return [appointment.to_dict() for appointment in self.appointments.values()]

    def update_appointment(self, appointment_id, data):
        appointment = self.appointments.get(appointment_id)
        if not appointment:
            return {"error": "Appointment not found"}, 404

        for key, value in data.items():
            if hasattr(appointment, key):
                setattr(appointment, key, value)

        self.appointments[appointment_id] = appointment
        return {"message": "Appointment updated", "id": appointment.id}

    def delete_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            return {"message": "Appointment deleted"}
        return {"error": "Appointment not found"}, 404
