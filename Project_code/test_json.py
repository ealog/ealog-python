import json

lt_impep={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}

k = 1
file_name = 'lt_impep.json'

json_str = json.dumps(lt_impep)

print(json_str)
print(lt_impep)


with open(file_name,'w') as file_object:
    file_object.write(json_str)

with open(file_name,'r') as f:
    i = json.loads(f.read())

print(i[str(k)])