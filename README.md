# dropbox-api-demo
Dropbox api demo with python

To get started, add a .env file following the format of the .env.example
To find your access token, go to https://www.dropbox.com/developers/apps/info for your account
and generate the ACCESS_TOKEN there. Note also that you will need to create an app with file and folder
read and write permissions.

Then, create a virtual environment with:
`python -m venv project_env`

Activate your venv on windows with:
`project_env\scripts\activate.bat`

You should see your terminal get the (project_env) description before the path.
If not or to be extra sure, you can verify with:
`which python`
and if the path points to within your project, you should be sorted.

Next, we need to install the requirements.txt
Run the command:
`pip install -r requirements.txt`

Finally, you should be ready to run the project.
Something like the following should suffice:
`python dropbox-script.py`

You'll be greeted with a menu like:
`
0 /RidhaaCupidoHyperionDev
1 /Sent files
Enter an action to take:
Download
Forward
Back
Exit
`

Follow the prompts from there.
Note that the Download file option is currently not working and the Back functionality.
All you can do is Navigate forward with commands like `Forward 0` to move forward in the first folder
you see.
Hopefully I can get a few more pieces of functionality in here before someone sees it :))

