import os
import json
from tutorial4_fixture.SampleCode.main import save_dict



def test_json_load(tmpdir):
    filepath=os.path.join(tmpdir,"test.json")
    _dict={"a":1,"b":2}
    save_dict(_dict,filepath)
    assert json.load(open(filepath,'r'))==_dict

def test_json_load2(tmpdir,capsys):
    filepath=os.path.join(tmpdir,"test.json")
    _dict={"a":1,"b":2}
    save_dict(_dict,filepath)
    #assert json.load(open(filepath,'r'))==_dict
    assert capsys.readouterr().out=="Saved Successfully\n"