def BMR(sex: str, age: int, weight: float, height: float, **kwargs) -> float:
    if sex.lower() in ["male", "m"]:
        return 10 * weight + 6.25 * height + 5
    elif sex.lower() in ["female", "f"]:
        return 10 * weight + 6.25 * height - 161
    raise (ValueError(f"Unknown sex: {sex}.\tIt must be either male or female"))

def TDEE(activity_current: int, **kwargs) -> float:
    if 'BMR' in kwargs:
        bmr = kwargs['BMR']
    else:
        bmr = BMR(**kwargs)
    activity_multiplier = [1.2, 1.375, 1.55, 1.725, 1.9]
    return bmr * activity_multiplier[activity_current-1]

def BMI(weight: float, height: float, **kwargs) -> float:
    return weight / ((height / 100) ** 2)

def BMI_prime(**kwargs) -> float:
    if 'BMI' in kwargs:
        bmi = kwargs['BMI']
    else:
        bmi = BMI(**kwargs)
    return bmi / 25
