import json
import os

from consants import STAT_PATH, API
from util.fetch import fetch

def get(assign_name):
    with open(os.path.join(STAT_PATH, "assign_mapping.json"), "rt") as json_in:
        assign_to_config = json.load(json_in)
    if assign_name not in assign_to_config:
        print("Invalid Assign Number!")
        print("Available names are:")
        for hwmap in assign_to_config:
            print("- " + hwmap + " [" + assign_to_config[hwmap]['contest_name'] + "]")
        print("If you want to update latest homework assignment, type: [oj update] to update.")
        return
    contest_id, problem_id = (
        assign_to_config[assign_name]["contest_id"],
        assign_to_config[assign_name]["contest_problem_id"],
    )
    endpoint = "contest/problem?contest_id={}&problem_id={}".format(
        contest_id, problem_id
    )
    result = json.loads(fetch("get", endpoint, {}).text)
    data = result["data"]
    if not data:
        print("Unexpected Error with Server")
        return
    try:
        samples = data["samples"]
    except:
        print("Unexpected Error in Parsing Response")
        print(data)
        return
    template = None
    if "C" in data["template"]:
        template = data["template"]["C"]
    else:
        template = "#include <stdio.h>\n\nint main() {\n  \n  return 0;\n}\n"
    dir_name = data["_id"].split(' ')[1]
    print("Made a [{}] folder in your current directory.".format(dir_name))
    template_path = dir_name + "/main.c"
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    with open(template_path, "wt") as fout:
        fout.write(template)
    for idx, sample in enumerate(samples):
        sample_num = idx + 1
        input_sample_path = dir_name + "/" + "{}.in".format(sample_num)
        input_ = sample["input"]
        with open(input_sample_path, "wt") as fout:
            fout.write(input_)
        output_sample_path = dir_name + "/" + "{}.out".format(sample_num)
        output = sample["output"]
        with open(output_sample_path, "wt") as fout:
            fout.write(output)