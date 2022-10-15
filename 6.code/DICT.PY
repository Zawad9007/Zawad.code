#  It is creating a dictionary with keys as English words and values as Hindi words.
# 2. Then it is printing the keys of the dictionary.
# 3. Then it is taking input from the user and storing it in variable a.
# 4. Then it is printing the value of the key which was entered by the user.

Hindi = {
    "pankha":"fan",
    "yani":"but",
    "chese":"items",
    "Hindi":"hindi",
    "ya":"this",
    "nahi":"not",
    "vastu":"items",
    "ya":"it",
    "chiye":"need" 
}
print("Opsins are:",Hindi.keys())
a = input("Enter the Word:\n\t")
print("Word meaning is:",Hindi.get(a))