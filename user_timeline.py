import requests
import json
import codecs

output_result=[]
output_dic={}
endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/nsr.json" 

headers = { "Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAHFJ%2BQAAAAAArz9h8BbARhS6KjXci4zXuBGOSeo%3DnDs9hpJPLRSJwh6gx2TxOdga0mJDN6Qs3zmLj9xWQaziWnjgqg", "content-type": "application/json" }
enter_id=str(input())
data = { "query":"from:" + enter_id + '' ,"maxResults": "500","fromDate":"200603210000", "toDate":"201903250000" }
# print(data)
num=1


if (num == 1) :
	response = requests.post(endpoint, data=json.dumps(data),headers=headers).json()
	for i in response["results"] :
		output_result.append(i)
	
	while("next" in response.keys()) : 
		num+=1
		print("num",num)
		data2={"query":"from:" + enter_id + '' ,"maxResults": "500","fromDate":"200603210000", "toDate":"201903250000" , "next" : response["next"]}
		response = requests.post(endpoint, data=json.dumps(data2),headers=headers).json()
		for j in response["results"] :
			output_result.append(j)

F_NAME = 'All_'+ enter_id + '.json'
output_dic['tweets']=output_result

with codecs.open(F_NAME, 'w', encoding='utf8') as f_out:
	output_data=json.dumps(output_dic, indent=2)
	f_out.write(output_data)

f_out.close()

print("================================================")
print("END")

print(type(output_dic))
print(len(output_result))
print(type(output_result))

print(len(output_dic['tweets']))







# if(response["next"] is not None) : 
# 	while (response["next"] is not None) :
# 		print(response["next"])
# 		print("total tweets", len(response["results"]))
# 		i+=1
# 		data2={"query":"from:" + enter_id + '' ,"maxResults": "100","fromDate":"200603210000", "toDate":"201903250000" , "next" : response["next"]}
# 		response = requests.post(endpoint, data=json.dumps(data2),headers=headers).json()
# 		print("num",i)
		
# 		twitter=json.dumps(response, indent=2)
# 		F_NAME =  enter_id + 'tweets'+'.json'
# 		with open(F_NAME,'w') as f_out:
# 			f_out.write(twitter)
# else :
# 	print("END")