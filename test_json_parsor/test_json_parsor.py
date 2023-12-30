import pytest
from json_parsor.json_parsor import parse

step1_valid = {}
step1_invalid = None

step2_valid = {"key": "value"}
step2_invalid = {"key": "value",}
step2_valid2 = {
  "key": "value",
  "key2": "value"
}
step2_invalid2 = {
  "key": "value",
  key2: "value"
}

step3_valid = {
  "key1": true,
  "key2": false,
  "key3": null,
  "key4": "value",
  "key5": 101
}
step3_invalid = {
  "key1": true,
  "key2": False,
  "key3": null,
  "key4": "value",
  "key5": 101
}

step4_valid = {
  "key": "value",
  "key-n": 101,
  "key-o": {},
  "key-l": []
}
step4_invalid = {
  "key": "value",
  "key-n": 101,
  "key-o": {
    "inner key": "inner value"
  },
  "key-l": ['list value']
}
step4_valid2 = {
  "key": "value",
  "key-n": 101,
  "key-o": {
    "inner key": "inner value"
  },
  "key-l": ["list value"]
}

def test_step1_valid():
    assert parse(step1_valid) == True

def test_step1_invalid():
    assert parse(step1_invalid) == False