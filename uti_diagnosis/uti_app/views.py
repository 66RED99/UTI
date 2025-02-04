from django.shortcuts import render
from .forms import UTIForm
import joblib
import pandas as pd


def predict_uti(request):
    result = None
    if request.method == "POST":
        form = UTIForm(request.POST)
        if form.is_valid():
            # Create feature dictionary
            features = [
                "dysuria",
                "polyuria",
                "fever",
                "fatigue",
                "hematuria",
                "flank_pain",
                "abd_pain",
                "abx",
                "Chronic_renal_failure",
                "Diabetes_mellitus_without_complication",
                "Diabetes_mellitus_with_complications",
                "WBC",
                "Creatinine",
                "age",
            ]

            data = {
                f: int(form.cleaned_data[f]) if f != "age" else form.cleaned_data[f]
                for f in features[:-3]
            }
            data.update(
                {
                    "WBC": form.cleaned_data["WBC"],
                    "Creatinine": form.cleaned_data["Creatinine"],
                    "age": form.cleaned_data["age"],
                }
            )

            # Create DataFrame
            input_df = pd.DataFrame([data], columns=features)

            # Scale age
            scaler = joblib.load("age_scaler.pkl")
            input_df["age"] = scaler.transform(input_df[["age"]])

            # Load model and predict
            model = joblib.load("uti_model.pkl")
            prediction = model.predict(input_df)
            print(prediction)

            result = "UTI Detected" if prediction[0] == 1 else "No UTI Detected"
    else:
        form = UTIForm()

    return render(request, "uti_app/index.html", {"form": form, "result": result})
