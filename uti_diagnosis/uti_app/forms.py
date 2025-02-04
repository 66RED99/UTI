from django import forms

class UTIForm(forms.Form):
    YES_NO_CHOICES = [(1, 'Yes'), (0, 'No')]

    dysuria = forms.ChoiceField(choices=YES_NO_CHOICES, label="Painful urination?")
    polyuria = forms.ChoiceField(choices=YES_NO_CHOICES, label="Excessive urination?")
    fever = forms.ChoiceField(choices=YES_NO_CHOICES, label="Fever?")
    fatigue = forms.ChoiceField(choices=YES_NO_CHOICES, label="Fatigue?")
    hematuria = forms.ChoiceField(choices=YES_NO_CHOICES, label="Blood in urine?")
    flank_pain = forms.ChoiceField(choices=YES_NO_CHOICES, label="Flank pain?")
    abd_pain = forms.ChoiceField(choices=YES_NO_CHOICES, label="Abdominal pain?")
    abx = forms.ChoiceField(choices=YES_NO_CHOICES, label="Antibiotics use?")
    Chronic_renal_failure = forms.ChoiceField(choices=YES_NO_CHOICES, label="Chronic renal failure?")
    Diabetes_mellitus_without_complication = forms.ChoiceField(choices=YES_NO_CHOICES,
                                      label="Diabetes without complications?")
    Diabetes_mellitus_with_complications = forms.ChoiceField(choices=YES_NO_CHOICES,
                                      label="Diabetes with complications?")
    WBC = forms.FloatField(label="White Blood Cell count (cells/µL)")
    Creatinine = forms.FloatField(label="Creatinine level (mg/dL)")
    age = forms.IntegerField(label="Age (years)")