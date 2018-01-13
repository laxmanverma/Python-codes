import pyrebase

config = {
  "apiKey": "******",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

def writeToFirebase():
	firebase = pyrebase.initialize_app(config)
	db = firebase.database()
	data = {"name": "Mortimer 'Morty' Smith"}
	#db.child("users").push(data)			#To save data with a unique, auto-generated, timestamp-based key
	#db.child("users").child("Morty").set(data)	#To create your own keys
	db.child("users").child("Morty").update({"name": "Mortiest Morty"})	#To update data for an existing entry
	allMsg = db.child("users").get()
	for msg in allMsg.each():
	    print(msg.val())
 
writeToFirebase()
