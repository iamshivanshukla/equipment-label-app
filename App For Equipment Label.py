from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def fetch_machine_info(label):
    conn = sqlite3.connect("equipment.db")
    cursor = conn.cursor()
    cursor.execute("SELECT machine_name, purchase_date, last_inspection_date, last_service_date FROM MachineInfo WHERE existing_image=?", (label,))
    result = cursor.fetchone()
    conn.close()
    print(f"🔹 Query Result: {result}")  # Debug: Print the query result
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    info = None
    label = None
    if request.method == "POST":
        try:
            label = request.form["equipment_label"].strip().upper()
            print(f"🔹 Equipment Label Submitted: {label}")  # Debug: Print the label
            info = fetch_machine_info(label)  # Fetch machine info from DB using label
            return render_template("index.html", info=info, label=label)  # Pass data to template
        except KeyError:
            return "❌ Error: Missing 'equipment_label' field", 400
    return render_template("index.html", info=info, label=label)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)