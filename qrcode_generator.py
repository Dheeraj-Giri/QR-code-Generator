# importing the qrcode
import qrcode
import time 

qr=qrcode.QRCode(
    version=2,
    box_size=10,
    border=5
)

url=input("Enter the URL: ")
save_file=input("Enter name of file to save in system: ")
if(url[0:8]=='https://'):
    qr.add_data(url)
else:
    qr.add_data('https://'+url)

qr.make(fit=True)
    
img=qr.make_image(fill_color='black', back_color="white")
img.save(save_file+'.png')

time.sleep(1)
print("Successfully Created Qrcode !!!")