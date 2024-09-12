from config import EXERCISE_DATA_FILE, EXERCISE_INPUT_FILE

import pandas as pd
import yaml
from typing import Tuple, Union, List
import numpy as np


def generate_exercise_plan() -> pd.DataFrame:
    with open(EXERCISE_INPUT_FILE, "r") as fp:
        exercise_order = yaml.safe_load(fp)

    exercise_plan = exercise_plan_from_order(exercise_order)

    exercise_plan.to_csv(EXERCISE_DATA_FILE)


def exercise_plan_from_order(order) -> pd.DataFrame:
    return pd.DataFrame(
        parse_exercise_order(order),
        columns=[
            "Macrocycle",
            "Mesocycle",
            "Week",
            "Day",
            "Exercise",
            "Sets",
            "Reps",
            "Weight",
            "Duration",
        ],
    )


def parse_exercise_order(order) -> pd.DataFrame:
    plan_data = []
    for ma, macro in order.items():
        for me, meso in macro.items():
            weeks, days_per_week = meso[0]
            for exercise_definition in meso[1:]:
                days_values = list(
                    zip(
                        *get_exercise_values(weeks, days_per_week, *exercise_definition)
                    )
                )
                for (week, day), day_values in zip(
                    [(w, d) for w in range(weeks) for d in range(days_per_week)],
                    days_values,
                ):
                    plan_data.append((ma, me, week + 1, day + 1, *day_values))

    return plan_data


ExerciseValuesDefinition = Union[float, Tuple[float]]


def get_exercise_values(weeks: int, days_per_week: int, *args):
    iterations = weeks * days_per_week
    return tuple(get_values_from_definition(iterations, a) for a in args)


def get_values_from_definition(
    iterations: int, value_definition: ExerciseValuesDefinition
) -> List[float]:
    if not isinstance(value_definition, (tuple, list)):
        return [value_definition] * iterations
    return [
        round(float(v), 1)
        for v in np.linspace(
            min(value_definition), max(value_definition), num=iterations
        )
    ]
