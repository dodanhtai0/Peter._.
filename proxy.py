import httpx

with open("http.txt", 'w') as file:
	file.write(httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http").text)