from .external_request import send_inscription

from .lib import confiramtion_btn, extract_information
import re
#modification manomboka eto 
class GenericMessage:
    greeting_message = "Ministère de la jeunesse et des sports, nous vous souhaitons la bienvenu"
    default_message = "Ministère de la jeunesse et des sports,que puis je faire pour vous ?"
    mjs_message = "Ministère de la jeunesse et des sports, choisissez la région qui vous convient."
    sorry_message = "Il semble que nous ne disposons actuellement l'information que vous recherchez sur cette information."
    inscripton_format = """Nom:votre nom,\nPrenom:votre prenom,\nEmail:votre email,\nSexe:M ou F,\nCIN:votre cin,\nDateNaissance:AAAA-MM-JJ,\nTel:votre numéro téléphone,\nFormation:exemple de formation."""
    inscription_response_success = "Votre demande est envoyé et en cours de traitement"
    inscripton_response_error = "Il semble qu'une erreur se produit , veuillez reéssayer plutard"
    inscripion_message = """
    Pour s’inscrire à des formation au sein de la ministére de la jeunesse et des sports , veuillez saisir votre information , dont le format et la suivante,pour beneficier notre formation.
    """
    


def handle_postback_event(event,bot):
    sender_id = event['sender']['id']
    payload = event['postback']['payload']
    data = payload.split(";")
    
    if payload == "start":
        bot.send_text_message(sender_id, GenericMessage.greeting_message)
        bot.send_text_message(sender_id, GenericMessage.inscripion_message)
        bot.send_text_message(sender_id, GenericMessage.inscripton_format)
        return
    
    if payload == "quick":
        bot.send_text_message(sender_id, GenericMessage.inscripion_message)
        bot.send_text_message(sender_id, GenericMessage.inscripton_format)
        return
    
    #si user send inscription
    if len(data) ==2 and data[0] == "send":
        information = extract_information(data[1])
        information['id_fb'] = sender_id
        response = send_inscription(information)
        if response == "ok":
            bot.send_text_message(sender_id, GenericMessage.inscription_response_success)
            return
        bot.send_text_message(sender_id, GenericMessage.inscripton_response_error)
        return
    
    #if update
    if len(data) ==2 and data[0] == "update":
        bot.send_text_message(sender_id, GenericMessage.inscripton_format)
        return


def handle_message_event(event, bot):
    sender_id = event['sender']['id']
    payload = event['message']['text']
    information = extract_information(payload)
    print(payload)
    print(information)
    print(len(information))   
    
    if payload == "Inscription":
        bot.send_text_message(sender_id, GenericMessage.inscripion_message)
        bot.send_text_message(sender_id, GenericMessage.inscripton_format)
        return
     
    if len(information) < 3 or information.get("nom") =="" or information.get("email") =="":
        bot.send_text_message(sender_id, GenericMessage.default_message)
        print("tsisy information")
        return
        
    else:
        # confiramtion_btn(sender_id,payload,information.get("nom"),bot)
        information['id_fb'] = sender_id
        response = send_inscription(information)
        if response == "ok":
            bot.send_text_message(sender_id, GenericMessage.inscription_response_success)
            return
        bot.send_text_message(sender_id, GenericMessage.inscripton_response_error)
        print("misy information")
        return
    

