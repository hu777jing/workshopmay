import setuptools

with open ('README.md','r') as rf:
	long_description=rf.read()
	
setuptools.setup(
	name="pavutils-Jing",
	version="0.1",
	author="Jing Hu",
	author_email="hu777jing@gmail.com",
	description="a suite of dh tools",
	long_description=long_description,
	long_description_content_type="text",
	url="www.google.com",
	packages=setuptools.find_packages(),
	keywords=["DH","text analysis","nlp","data visualization"],
	licese="Apache License 2.0"
	classifiers=[
		"programming Language :: Python :: 3",
		"Operating System :: OS Independent",
		"Development Status :: 1-Planning",
		"License :: OSI Apache License 2.0"
	]
)