def BMR(sex: str, age: int, weight: float, height: float, **kwargs) -> float:
    if sex.lower() in ["male", "m"]:
        return 10 * weight + 6.25 * height + 5
    elif sex.lower() in ["female", "f"]:
        return 10 * weight + 6.25 * height - 161
    raise (ValueError(f"Unknown sex: {sex}.\tIt must be either male or female"))


def BMI(weight: float, height: float, **kwargs) -> float:
    return weight / ((height / 100) ** 2)
