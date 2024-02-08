#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install qrcode[pil]


# In[4]:


import qrcode
import os


# In[10]:


# Input the website URL you want to generate a QR code for
url = 'https://pradyog.com'


# In[11]:


# Function to determine the default download path
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':  # for Windows
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:  # Linux and macOS
        return os.path.join(os.path.expanduser('~'), 'Downloads')


# In[12]:


# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)


# In[13]:


# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")


# In[14]:


# Save the image to the default download path
download_path = get_download_path()
filename = "website_qr.png"
save_path = os.path.join(download_path, filename)
img.save(save_path)

print(f"QR code generated and saved as {save_path}")


# In[ ]:




