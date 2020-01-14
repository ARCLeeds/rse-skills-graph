# 2020-01-13
# Alex Coleman, a.coleman1@leeds.ac.uk
# a class for data preparation for the rse-skills-graph

### TODO

class data_prep:

    def __init__():
        return
        
    def get_people():
        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'people.json'))
        return get_file_contents(filepath)

    # thanks to Colin Morris for adding this code originally
    def get_skills_list():
        skills_list = {}
        json_results = get_people()
        for supervisor, data in json_results.items():
            for section in data:
                for item in json_results[str(supervisor)][section]:
                    if item not in skills_list:
                        skills_list[item] = 1;
                    else:
                        skills_list[item] = skills_list[item] +1;

        skills_list_new = OrderedDict(natsort.natsorted(skills_list.items()))
        return skills_list_new


    def get_file_contents(filename):
        data = None

        try:
            fp = open(filename, 'rb')
            try:
                contents = fp.read()
                data = json.loads(contents)
            finally:
                fp.close()
        except IOError:
            print('Could not open JSON file:' + filename, file=sys.stderr)
            sys.exit(1)

        return data
