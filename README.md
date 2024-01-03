
# Encrypt API
Simple API to make strings unreadable
## Features

- Encrypt and Decrypt strings with your private key
- Generate private keys
## Installation

Requirements:
- You need Python3 or newer
- flask
- (requests, only for testing)

```bash
  git clone https://github.com/meltree/encrypt-api.git
  cd encrypt-api
  python3 app.py
```
## FAQ

#### Is this secure?

Yes, you can only decrypt your string if you have the private key so DO NOT share it.

#### Do you store the generated keys?

No, you can look into the code if you want
## License

[MIT](https://choosealicense.com/licenses/mit/)

