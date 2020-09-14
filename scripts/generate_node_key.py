from iroha import IrohaCrypto as ic

# TODO
# Add support for ursa keys

def save_keys_to_file(account_id):
    private_key = ic.private_key()
    public_key = ic.derive_public_key(private_key)
    try:
        with open(f"{account_id}.priv", "wb+") as private_key_file:
            private_key_file.write(private_key)
    except:
        raise
    try:
        with open(f"{account_id}.pub", "wb+") as public_key_file:
            public_key_file.write(public_key)
    except:
        raise

account_id = input("Please provide a name for the keypair files")

save_keys_to_file(account_id=account_id)

print("Done!, Please copy the keys to the correct paths and change config")