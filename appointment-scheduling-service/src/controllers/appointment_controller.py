from flask import Flask, request, jsonify
from services.appointment_service import AppointmentService

app = Flask(__name__)
appointment_service = AppointmentService()

@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input, JSON data is required"}), 400
        result = appointment_service.create_appointment(data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_all_appointments():
    try:
        result = appointment_service.get_all_appointments()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    try:
        result = appointment_service.get_appointment(appointment_id)
        if not result:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments/doctor/<int:doctor_id>', methods=['GET'])
def get_appointments_by_doctor(doctor_id):
    try:
        result = appointment_service.get_appointments_by_doctor(doctor_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input, JSON data is required"}), 400
        result = appointment_service.update_appointment(appointment_id, data)
        if not result:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        result = appointment_service.delete_appointment(appointment_id)
        if not result:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify({"message": "Appointment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
