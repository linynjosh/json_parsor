import pytest
from json_parsor.json_parsor import parse

step1_valid = {}
step1_invalid = None

step2_valid = None
step2_invalid = None
step2_valid2 = None
step2_invalid2 = None

step3_valid = None
step3_invalid = None

step4_valid = None
step4_invalid = None
step4_valid2 = None

def test_step1_valid():
    assert parse(step1_valid) == True

def test_step1_invalid():
    assert parse(step1_invalid) == False