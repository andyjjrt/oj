import os
import json
from util.fetch import fetch
from consants import STAT_PATH

def update():
	if not os.path.isdir(STAT_PATH):
		os.mkdir(STAT_PATH)
	inputstr = '{'
	result = json.loads(fetch("get", "problem?offset=0&limit=200", "{}").text)
	counter_1 = 1
	for i in range(0,len(result['data']['results'])):
		real_id = result['data']['results'][i]['id']
		display_id = result['data']['results'][i]['_id'].replace(" ","_")
		if counter_1 != 1:
			inputstr += ','
		inputstr += '"' + str(display_id) + '":{"_id":"' + str(real_id) + '"}'
		counter_1+=1
	inputstr += '}'
	f = open(os.path.join(STAT_PATH, "problem_mapping.json"),'w')
	f.write(inputstr)
	f.close
	print("Updated problems successfully!")
	inputstr = '{'
	result = json.loads(fetch("get", "contests?offset=0&limit=10&status=0", "{}").text)
	counter = 1
	for i in range(0,len(result['data']['results'])):
		contestid = result['data']['results'][i]['id']
		payload = {"contest_id" : str(contestid)}
		endpoint = "contest/problem?contest_id=" + str(contestid)
		result2 = json.loads(fetch("get", "contest/problem?contest_id=" + str(contestid), payload).text)
		if result2["error"] == "error":
			print("Error : " + result2["data"])
			continue
		q_string3 = result['data']['results'][i]["title"]
		q_string2 = ""
		for q1 in q_string3.split(" "):
			try:
				q_string2 += q1 + " "
			except:
				q_string2 += "XX "
		q_string = result2['data'][0]['_id']
		_pid = q_string.split()[0] + "+" + q_string.split()[1]
		print("Found HomeWork: " + "hw" + str(counter) + " [" + q_string2 + "]")
		if counter != 1:
			inputstr += ','
		inputstr += '"hw' + str(counter)+'":{"contest_name":"' + str(q_string2) + '","contest_id":' + str(contestid) + ',"contest_problem_id":"' + str(_pid)+ '","problem_id":' + str(result2["data"][0]["id"]) + '}'
		counter += 1
	inputstr += '}'
	f = open(os.path.join(STAT_PATH, "assign_mapping.json"),'w')
	f.write(inputstr)
	f.close
	print("Updated assign successfully!")
	