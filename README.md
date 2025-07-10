# Patient Health Dashboard

This project is a modern, comprehensive web-based dashboard for healthcare professionals to remotely monitor patient health data collected from wristband devices. The dashboard features a beautiful, responsive interface with multiple specialized views for different aspects of patient care.

## ✨ Features

### **Core Monitoring**
- **Real-Time Monitoring:** View patient data collected from wristbands with live updates
- **Comprehensive Health Metrics:** Track heart rate, steps, sleep hours, blood oxygen, and ECG waveforms
- **Interactive Visualizations:** Modern charts with smooth animations and hover effects
- **Risk Assessment:** Automatic health risk scoring with color-coded alerts
- **Trend Analysis:** 24-hour and historical trend monitoring

### **Multi-Page Dashboard**
- **Main Dashboard:** Overview with quick health status and navigation
- **Vitals & Health:** Detailed vital signs monitoring with 24-hour heart rate trends
- **Medications:** Medication tracking, reminders, and adherence monitoring
- **Symptoms:** Interactive symptom logging and pattern tracking
- **Communication:** Messages and video call interface with care team
- **Reports:** Downloadable health reports and analytics
- **Appointments:** Appointment scheduling and management

### **Modern UI/UX**
- **Glass Morphism Design:** Beautiful translucent effects with backdrop blur
- **Smooth Animations:** Engaging hover effects and transitions
- **Mobile-First Responsive:** Optimized for all device sizes
- **Dark/Light Theming:** Automatic contrast adjustments
- **Micro-Interactions:** Delightful user feedback throughout the interface

### **Advanced Features**
- **Patient Context Preservation:** Seamless navigation between pages with patient ID tracking
- **Early Warning System:** Automated alerts for abnormal readings
- **Medication Management:** Take medication buttons with status tracking
- **Symptom Tracking:** Visual symptom selection with analytics
- **Emergency Contact:** One-click emergency service contact

## 🏗️ How It Works

1. **Wristband Device:** Patients wear smart wristbands that continuously record health metrics and sync data automatically
2. **Backend (Flask):** A robust Python Flask server processes patient data from `patient_data.csv` and serves it via RESTful APIs
3. **Multi-Page Frontend:** The dashboard consists of multiple specialized pages:
   - **Healthcare Provider View (`index.html`):** Patient selection and overview dashboard
   - **Patient Dashboard (`patient-dashboard.html`):** Main patient interface with navigation
   - **Specialized Views:** Dedicated pages for vitals, medications, symptoms, communication, reports, and appointments
4. **Real-Time Updates:** Automatic data refresh and live health monitoring
5. **Patient Navigation:** Seamless transitions between different health management sections

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Flask 2.0+
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone or download** this repository to your local machine
2. **Install Flask** and dependencies:
   ```sh
   pip install flask
   ```
3. **Verify file structure** - ensure all files are in the same directory as the Flask app

### Running the Dashboard

1. **Start the Flask server:**
   ```sh
   python "from flask import Flask, jsonify.py"
   ```
2. **Open your browser** and navigate to:
   - **Healthcare Provider Dashboard:** [http://localhost:5000](http://localhost:5000)
   - **Patient Dashboard:** [http://localhost:5000/patient-dashboard.html](http://localhost:5000/patient-dashboard.html)
   - **Specific Patient View:** [http://localhost:5000/patient/{patient_id}](http://localhost:5000/patient/1)

### 📁 File Structure

```
├── from flask import Flask, jsonify.py    # Flask backend server
├── index.html                             # Healthcare provider dashboard
├── patient-dashboard.html                 # Main patient dashboard
├── patient-vitals.html                   # Vitals monitoring page
├── patient-medications.html              # Medication management
├── patient-symptoms.html                 # Symptom tracking
├── patient-communication.html            # Care team communication
├── patient-reports.html                  # Health reports & analytics
├── patient-appointments.html             # Appointment management
├── patient.html                          # Legacy patient view (redirects)
├── patient_data.csv                      # Sample patient data
└── README.md                             # Documentation
```

## 📖 Usage Guide

### For Healthcare Providers
1. **Access the main dashboard** at [http://localhost:5000](http://localhost:5000)
2. **Select a patient** from the dropdown menu to view their health data
3. **Review comprehensive metrics** including heart rate, steps, sleep, blood oxygen, and ECG
4. **Monitor risk levels** with color-coded health status indicators
5. **Identify trends** using interactive charts and historical data

### For Patients
1. **Navigate to your dashboard** via the patient portal
2. **Explore different sections:**
   - **Dashboard:** Quick health overview and navigation
   - **Vitals:** Detailed health metrics and 24-hour trends
   - **Medications:** Track and manage your prescriptions
   - **Symptoms:** Log how you're feeling with interactive tracking
   - **Communication:** Connect with your care team
   - **Reports:** Access your health reports and summaries
   - **Appointments:** Schedule and manage medical appointments

### Key Features in Action
- **Real-time Updates:** Health data refreshes automatically every 30 seconds
- **Interactive Charts:** Hover over data points for detailed information
- **Mobile Responsive:** Use on any device - phone, tablet, or desktop
- **Emergency Features:** Quick access to emergency contacts and alerts
- **Medication Reminders:** Track when medications are due and mark them as taken

## 🎨 UI/UX Highlights

- **Glass Morphism Design:** Modern translucent interface with backdrop blur effects
- **Smooth Animations:** Engaging hover effects and seamless transitions
- **Intuitive Navigation:** Easy-to-use interface with clear visual hierarchy
- **Accessibility:** High contrast ratios and keyboard navigation support
- **Performance Optimized:** Fast loading times and smooth interactions

## 🔧 Customization

### Adding New Patients
- **Add patient data** to `patient_data.csv` with the required columns:
  - `patient_id`, `name`, `age`, `diagnosis`, `heart_rate`, `steps`, `sleep_hours`, `blood_oxygen`, `ecg_waveform`, `timestamp`

### Extending Functionality
- **New Health Metrics:** Add columns to CSV and update visualization code
- **Custom Alerts:** Modify the risk calculation algorithm in the Flask backend
- **Additional Pages:** Create new patient sub-pages following the existing pattern
- **Styling Changes:** Customize CSS variables for colors, fonts, and animations
- **API Extensions:** Add new endpoints in the Flask app for additional data sources

### Configuration Options
- **Chart Colors:** Modify chart color schemes in JavaScript
- **Thresholds:** Adjust health warning/danger thresholds in the risk calculation
- **Refresh Intervals:** Change auto-refresh timing in the JavaScript
- **UI Animations:** Enable/disable animations by modifying CSS transition properties

## 🔒 Security & Privacy

- **Local Data:** All patient data is stored and processed locally
- **No External Dependencies:** Charts and UI components are self-contained
- **HIPAA Considerations:** Suitable for development and testing environments
- **Data Encryption:** Consider implementing SSL/TLS for production use

## 🚀 Future Enhancements

- **Real-time WebSocket** connections for live data streaming
- **Machine Learning** integration for predictive health analytics
- **Mobile App** companion for patients
- **Database Integration** for scalable data storage
- **Multi-tenant Support** for multiple healthcare organizations
- **Advanced Reporting** with PDF generation and email delivery

## 📊 Technical Stack

- **Backend:** Python Flask with RESTful API endpoints
- **Frontend:** Vanilla HTML5, CSS3, and JavaScript (ES6+)
- **Charts:** Chart.js for interactive data visualizations
- **Styling:** Modern CSS with Flexbox/Grid, animations, and glass morphism
- **Data Storage:** CSV file-based (easily adaptable to databases)
- **Icons:** Font Awesome for consistent iconography

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit your changes:** `git commit -m 'Add amazing feature'`
4. **Push to the branch:** `git push origin feature/amazing-feature`
5. **Open a Pull Request**

## 📝 License

This project is provided for **demonstration and educational purposes**. Feel free to use and modify for your healthcare applications.

## 📞 Support

For questions, issues, or feature requests, please create an issue in the repository or contact the development team.

---

*✨ Empowering healthcare professionals with beautiful, intuitive, and actionable patient insights. ✨*
