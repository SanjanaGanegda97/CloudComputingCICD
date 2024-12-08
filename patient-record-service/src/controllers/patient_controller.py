from flask import Flask, request, jsonify
from services.patient_service import PatientService

app = Flask(__name__)
patient_service = PatientService()

# Route to create a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input, JSON data is required"}), 400
        result = patient_service.create_patient(data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a patient's details by ID
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    try:
        result = patient_service.get_patient(patient_id)
        if not result:
            return jsonify({"error": "Patient not found"}), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all patients
@app.route('/patients', methods=['GET'])
def get_all_patients():
    try:
        result = patient_service.get_all_patients()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a patient's details
@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input, JSON data is required"}), 400
        result = patient_service.update_patient(patient_id, data)
        if not result:
            return jsonify({"error": "Patient not found"}), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a patient
@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        result = patient_service.delete_patient(patient_id)
        if not result:
            return jsonify({"error": "Patient not found"}), 404
        return jsonify({"message": "Patient deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
