from flask import Flask, jsonify, send_from_directory
import csv
import os
import ast

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/patient.html')
def serve_patient():
    return send_from_directory(os.getcwd(), 'patient-dashboard.html')

@app.route('/patient/<user_id>')
def serve_patient_with_id(user_id):
    return send_from_directory(os.getcwd(), 'patient-dashboard.html')

@app.route('/patient-dashboard.html')
def serve_patient_dashboard():
    return send_from_directory(os.getcwd(), 'patient-dashboard.html')

@app.route('/patient-vitals.html')
def serve_patient_vitals():
    return send_from_directory(os.getcwd(), 'patient-vitals.html')

@app.route('/patient-medications.html')
def serve_patient_medications():
    return send_from_directory(os.getcwd(), 'patient-medications.html')

@app.route('/patient-symptoms.html')
def serve_patient_symptoms():
    return send_from_directory(os.getcwd(), 'patient-symptoms.html')

@app.route('/patient-communication.html')
def serve_patient_communication():
    return send_from_directory(os.getcwd(), 'patient-communication.html')

@app.route('/patient-reports.html')
def serve_patient_reports():
    return send_from_directory(os.getcwd(), 'patient-reports.html')

@app.route('/patient-appointments.html')
def serve_patient_appointments():
    return send_from_directory(os.getcwd(), 'patient-appointments.html')

@app.route('/api/patient-data')
def patient_data():
    data = []
    def compute_risk(row):
        # Example scoring: heart rate, blood oxygen, sleep, steps
        score = 0
        points = {'heart_rate': 0, 'blood_oxygen': 0, 'sleep_hours': 0, 'steps': 0}
        try:
            hr = float(row.get('heart_rate', 0))
            o2 = float(row.get('blood_oxygen', 100))
            sleep = float(row.get('sleep_hours', 8))
            steps = int(row.get('steps', 10000))
        except Exception:
            hr, o2, sleep, steps = 0, 100, 8, 10000
        # Heart rate risk
        if hr >= 100 or hr <= 60:
            points['heart_rate'] = 4
        elif hr >= 90 or hr <= 65:
            points['heart_rate'] = 2
        score += points['heart_rate']
        # Blood oxygen risk
        if o2 < 92:
            points['blood_oxygen'] = 4
        elif o2 < 95:
            points['blood_oxygen'] = 2
        score += points['blood_oxygen']
        # Sleep risk
        if sleep < 5:
            points['sleep_hours'] = 2
        elif sleep < 7:
            points['sleep_hours'] = 1
        score += points['sleep_hours']
        # Steps risk (sedentary)
        if steps < 3000:
            points['steps'] = 2
        elif steps < 7000:
            points['steps'] = 1
        score += points['steps']
        # Clamp score
        score = min(max(int(score), 0), 15)
        # Category
        if score <= 3:
            category = 'Low'
        elif score <= 7:
            category = 'Mid'
        elif score <= 11:
            category = 'Moderate'
        else:
            category = 'High'
        return score, category, points
    with open('patient_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Parse ecg_waveform as a list if present
            if 'ecg_waveform' in row and row['ecg_waveform']:
                try:
                    row['ecg_waveform'] = ast.literal_eval(row['ecg_waveform'])
                except Exception:
                    row['ecg_waveform'] = []
            risk_score, risk_category, points = compute_risk(row)
            row['risk_score'] = risk_score
            row['risk_category'] = risk_category
            row['risk_points'] = points
            data.append(row)
    return jsonify(data)

@app.route('/api/patient/<user_id>')
def get_patient_by_id(user_id):
    def compute_risk(row):
        # Example scoring: heart rate, blood oxygen, sleep, steps
        score = 0
        try:
            hr = float(row.get('heart_rate', 0))
            o2 = float(row.get('blood_oxygen', 100))
            sleep = float(row.get('sleep_hours', 8))
            steps = int(row.get('steps', 10000))
        except Exception:
            hr, o2, sleep, steps = 0, 100, 8, 10000
        # Heart rate risk
        if hr >= 100 or hr <= 60:
            score += 4
        elif hr >= 90 or hr <= 65:
            score += 2
        # Blood oxygen risk
        if o2 < 92:
            score += 4
        elif o2 < 95:
            score += 2
        # Sleep risk
        if sleep < 5:
            score += 2
        elif sleep < 7:
            score += 1
        # Steps risk (sedentary)
        if steps < 3000:
            score += 2
        elif steps < 7000:
            score += 1
        # Clamp score
        score = min(max(int(score), 0), 15)
        # Category
        if score <= 3:
            category = 'Low'
        elif score <= 7:
            category = 'Mid'
        elif score <= 11:
            category = 'Moderate'
        else:
            category = 'High'
        return score, category
    
    with open('patient_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get('patient_id') == user_id or row.get('name') == user_id:
                # Parse ecg_waveform as a list if present
                if 'ecg_waveform' in row and row['ecg_waveform']:
                    try:
                        row['ecg_waveform'] = ast.literal_eval(row['ecg_waveform'])
                    except Exception:
                        row['ecg_waveform'] = []
                risk_score, risk_category = compute_risk(row)
                row['risk_score'] = risk_score
                row['risk_category'] = risk_category
                return jsonify(row)
    
    return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)