import os


def check_before_run():
	try:
		open("name.db")
	except:
		os.system("python db/init_db.py")

try:
	check_before_run()
except:
	exit("Lỗi,vui lòng kiểm tra lại databases")
