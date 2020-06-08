# import yaml

# with open(r'C:\Users\sumsa\Desktop\sample.yml', 'r') as file:
#     data = yaml.safe_load(file)
# user = data['user']
# user['roles'].append('new_role')
# print(user)

# with open(r'C:\Users\sumsa\Desktop\sample.yml', 'w') as file:
#     yaml.dump(user, file, default_flow_style=False)

# import json

# with open(r'C:\Users\sumsa\Desktop\sample.json', 'r') as file:
#     data = json.load(file)
# user = data['user']
# print(user)
# user['location']['city'] = 'Dallas'

# with open(r'C:\Users\sumsa\Desktop\sample.yml', 'w') as file:
#     json.dump(user, file)

# import xml.etree.ElementTree as ET

# with open(r'C:\Users\sumsa\Desktop\sample.xml', 'r') as file:
#     tree = ET.parse(file)
#     root = tree.getroot()

# user = root.find('user')
# print(user.find('name').text)

# user.find('location').find('city').text = 'Dallas'

# with open(r'C:\Users\sumsa\Desktop\sample.xml', 'w') as file:
#     tree.write(file, encoding='unicode')