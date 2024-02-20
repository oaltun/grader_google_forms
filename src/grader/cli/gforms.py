from pathlib import Path
import random
import re
from typing import List
from rich import print

import typer
from typer import Option


from grader.schema.question_schema import Choice, ChoiceType, MultipleChoiceQuestion
from pathlib import Path
import random
from subprocess import run
from typing import List
from toolz import take


from pathlib import Path
import re
import random


app = typer.Typer()


def fallback(if_correct, if_false, condition):
    """new if condition else"""
    if condition:
        return if_correct
    else:
        return if_false


def ternary(condition, if_correct, if_false):
    """new if condition else default"""
    if condition:
        return if_correct
    else:
        return if_false


def return_raise(e):
    raise e
    return -1


@app.command()
def grade(
    out_dir: Path = Option(Path('/home/o/repo/grader/tex_exam/out'), help="Path to output dir."),
    shuffle_options_enabled: bool = Option(True, help="options are to be shuffled?"),
    shuffle_questions_enabled: bool = Option(True, help="questions are to be shuffled?"),
    reverse_questions_enabled: bool = Option(True, help="questions are to be reversed?"),
    keys: List[str] = Option(["A", "B", "C", "D"], help="keys/exam-versions to generate"),
    tpl_path: Path = Option(Path("/home/o/repo/grader/tex_exam/tpl/main.tex"), help="path to latex template"),
    questions_placeholder: str = Option(
        r"\input{questions.tex}", help="str that will be replaced by questions in the template"
    ),
    answer_switch_placeholder: str = Option(
        r"\input{print_answers_or_not.tex}", help="str that will be replaced by '\printanswers' or '% \printanswers'"
    ),
    key_find: str = Option(rf"""\newcommand{{\coursegroup}}{{A}}""", help="path to latex template"),
) -> None:
    print("hello")
