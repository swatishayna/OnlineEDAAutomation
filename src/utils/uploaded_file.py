import os 


def save_uploaded_file(uploaded_file):
    with open(os.path.join("src//data",uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success("Saved file {} in data ".format(uploaded_file.name))

def save_cassandra_bundle(user,uploaded_file):
	os.mkdir("{}//")
	with open(os.path.join("{}\\config".format(user),uploaded_file.name),'wb') as f:
		f.write(uploaded_file.getbuffer())
	return st.success("Saved file {} in {}'s config folder".format(uploaded_file.name,user))