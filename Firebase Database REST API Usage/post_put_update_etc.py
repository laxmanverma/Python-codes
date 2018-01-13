import pyrebase

config = {
  "apiKey": "AAAACJPNUos:APA91bEv3xJ7Hyo53nEPoxlXqxFYI_pQJzt05_s5bFYMfZg_zYjpZfhqTbOuc4vS1WDnD_Qh9P0GliMh5Jh5lsHxGgAy_e6Gq3Z4DrdwfZ8AJ9RG3baf9AwB3SlkI6R3DOLyNW807pFZ",
  "authDomain": "myproject-96528.firebaseapp.com",
  "databaseURL": "https://myproject-96528.firebaseio.com",
  "storageBucket": "myproject-96528.appspot.com"
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
