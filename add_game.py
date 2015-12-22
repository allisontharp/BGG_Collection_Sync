import requests
def add_game_by_id(id,user,passwd):
	login_data={'username': user, 'password': passwd, 'B1': 'Submit'}
	payload={'objecttype':'thing','objectid':id,'addowned':'true','status':'%5Bobject%20HTMLDivElement%5D','ajax':'1','action':'additem','quickadd':'1'}
	with requests.Session() as s:
		# post login data
		s.post('https://www.boardgamegeek.com/login', data=login_data,verify=False)
		# Then do another s.post with your collection addition using the JSON payload from above
		s.post('https://boardgamegeek.com/geekcollection.php', data=payload,verify=False)
# Sample Function Call
# add_game_by_id(12750,'WhoDislikesKittens','ff^&|!L%DEA4')
