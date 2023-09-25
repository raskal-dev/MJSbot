from flask import request

#Verification access token et verify tokent
def access_page(verify_token):
    token_sent = request.args.get("hub.verify_token")
    return verify_meta_token(token_sent, verify_token)

def verify_meta_token(token_sent,verify_token):
    if token_sent == verify_token:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'
