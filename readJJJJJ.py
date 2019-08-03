import importlib
import os,sys,time,re
import json,operator
#读取json必须要encoding utf-8
newPath = '111111.json'
n =0
with open('111.json',encoding='utf-8')as load_f:
	with open(newPath,mode='w+',encoding='utf-8') as f:
		for line1 in load_f:
			n=n+1
			#'%s->%s start' %(startTime,filename)
			print('第%s行'%n)
			load_dict = json.loads(line1)
			#print(load_dict)
			#print('--------------')
		
		
		#转化为python字典类型load_dict
			json_dict_Geojson = load_dict.get('geojson')
			if(json_dict_Geojson is None):
				#print('successful')
			
				#print(load_dict)
				
				json.dump(load_dict,f)
				f.write('\n')
				#print('记录下奇数行')
			elif(json_dict_Geojson is not None):
		#筛选出第二行含有geojson字段的
				geojson_Coordinates = json_dict_Geojson['coordinates']
				geojson_List = geojson_Coordinates
				geojson_Array = geojson_List[0][0]
				#print(type(geojson_Array))
			#List数组类型，读取到最后含有多个数组的时候截止
				Temp = []
			#temp用来储存重复的索引
				for j in range(len(geojson_Array)-1):
					Array_First = geojson_Array[j]
					Array_Next = geojson_Array[j+1]
					if(operator.eq(Array_First,Array_Next)):
						print(Array_First)
						Temp.append(j)
				print(Temp)
				print(len(Temp))
				print('-------------')
				#print(geojson_Array)
				print(len(geojson_Array))
				print('+++++++++++++')
				if(len(Temp)!=0):
					for h in range(len(Temp)):
					#print(len(Temp))
						#print(geojson_Array[Temp[h]])
						#print(Temp[len(Temp)-h])
						print(Temp[len(Temp)-h-1])
						#倒序刪除循環裏的索引
						print(geojson_Array[Temp[len(Temp)-h-1]])
						del geojson_Array[Temp[len(Temp)-h-1]]
						#geojson_Array.remove(geojson_Array[Temp[h]])
						#print(geojson_Array[Temp[h]])
						#del geojson_Array[Temp[h]]
				#print(len(geojson_Array))
				geojson_Coordinates[0][0]=geojson_Array
				json_dict_Geojson['coordinates'] = geojson_Coordinates
				load_dict['geojson'] = json_dict_Geojson
		
			#更新后的值赋给过去
			
		
			#with open(newPath,'w+') as f:
			#print(load_dict)
				json.dump(load_dict,f)
				f.write('\n')
				#print('记录下第偶数行')