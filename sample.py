from hashlib import sha256

app_id = "S8GUU9IDF5WA4MYB0AC0W6H6" #(Please refer to required parameters section)
seg_name = "TEST"
api_secret = "89HR85UGSQEQ" # This is the sample key. Each app has a different secret key
signature = sha256(app_id+'|'+ seg_name+'|'+ api_secret).hexdigest()
print signature

# b82cc9a691029895e53c2fe782a75214d69ee4a50e893fb4abf3b59e7c996488
