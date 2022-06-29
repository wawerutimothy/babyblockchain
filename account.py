import secrets


class account:
    def createKeys(self):
        private_key = secrets.randbits(256)
        print(f"private key is {private_key}")

if __name__ == '__main__':
    acct = account()
    acct.createKeys()
