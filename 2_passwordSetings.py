from cryptography.fernet import Fernet
import pickle


key = Fernet.generate_key()
print('1-',key)
with open('datakey.bin','wb') as f1:
    pickle.dump(key,f1)
    
with open('datakey.bin','rb') as f2:
    key=pickle.load(f2)

print('2-',key)
cipher = Fernet(key)



pwd1r = input("Enter Administrator Password :-")
pwd1 = pwd1r.encode('utf-8')
encrypted_data1 = cipher.encrypt(pwd1)

pwd2r = input("Enter Database Password :-")
pwd2 = pwd2r.encode('utf-8')
encrypted_data2 = cipher.encrypt(pwd2)

pwd3r = input("Enter Super Password :-")
pwd3 = pwd3r.encode('utf-8')
encrypted_data3 = cipher.encrypt(pwd3)

dl=[encrypted_data1,encrypted_data2,encrypted_data3]

with open('passwords.bin','wb') as f3:
    pickle.dump(dl,f3)

with open('passwords.bin','rb') as f4:
    retfiles=pickle.load(f4)

for i in retfiles:
    print(i)
    decrypted_data = cipher.decrypt(i)
    print("Decrypted data:", decrypted_data.decode())
    print('***********************************************************')


"""
def importPasswords():
    global pwd_dict
    with open('datakey.bin','rb') as f1:
        key=pickle.load(f1)
    cipher = Fernet(key)

    with open('passwords.bin','rb') as f2:
        retfiles=pickle.load(f2)
    
    pwd_dict={"admin_pwd":retfiles[0] ,"database_pwd":retfiles[1] ,"super_password":retfiles[2] }

    for i in pwd_dict.keys():
        print(i," -->  ",pwd_dict[i])
"""
