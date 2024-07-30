Hi,
To startup the project,

we first need to setup a virtual enviornment,
1) Installation  : pip install virtualenv
2) Create virtual env : python -m venv myenv
3) To activate virtual env :
   a) Windows : myenv\Scripts\activate
   b) Mac/Linux : source myenv/bin/activate
4) Requirements : pip install fastapi uvicorn pydantic motor uuid
5) TO RUN THE APP:
     cd /path/to/folder
     RUN uvicorn app.main:app --reload
6) Go to "localhost:8000/docs", this is where you can see all the endpoint, and can try them
