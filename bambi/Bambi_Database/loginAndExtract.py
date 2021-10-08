import re
import config

from robobrowser import RoboBrowser

# sign in
br = RoboBrowser ()
br.open("https://loyverse.com/signin")
form = br.get_form()
form['email'] = config.rloyverse_Username
form['password'] = config.rloyverse_Password
br.submit_form(form)

# clicking download
#download_CSV = br.get_link("Exportar")
#br.open(download_CSV.get("href"))

# naming file
#file_Name = "Bambi_report.csv"