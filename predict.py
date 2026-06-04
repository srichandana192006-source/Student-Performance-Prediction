import joblib

model = joblib.load(
    "model/student_model.pkl"
)

study_hours = float(
    input("Enter Study Hours: ")
)

attendance = float(
    input("Enter Attendance: ")
)

previous_score = float(
    input("Enter Previous Score: ")
)

result = model.predict(
    [[
        study_hours,
        attendance,
        previous_score
    ]]
)

if result[0] == 1:
    print("PASS")
else:
    print("FAIL")
