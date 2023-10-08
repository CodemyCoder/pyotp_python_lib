import pyotp

# base 32
print("Secret Key")
# Secret Key Generation
secret_key = pyotp.random_base32()
print(secret_key)

print("TOTP")
# TOTP
totp = pyotp.TOTP(
    s="QUZTHTE7VKTB2KR72YJZUOCW47PDKLO2",
    digits=6,
    digest="SHA256",
    name="CodemyCoder",
    issuer="CodemyCoder",
    interval=60
)
generate_totp = totp.now()
print(generate_totp)
print(totp.secret)
print(totp.digits)
print(totp.digest)
print(totp.name)
print(totp.issuer)
print(totp.interval)
print(totp.generate_otp(1))
print(totp.at(10, 1))
print(totp.byte_secret())
print(totp.verify(generate_totp))


