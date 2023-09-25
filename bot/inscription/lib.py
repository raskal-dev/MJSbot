
def confiramtion_btn(sender_id, data, name,bot):
    response = {
        "recipient": {"id": sender_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": f"Veuillez confirmer {name} votre inscription",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"Envoyer",
                                    "payload": f'send;{data}'
                                },
                                {
                                    "type": "postback",
                                    "title": f"Mettre à jour",
                                    "payload": f'update;{data}'
                                },
                                ]
                        },
                    ]

                }
            }
        }
    }
    bot.send_raw(response)



def quick_response(sender_id, bot):
    response = {
      "recipient": {"id": sender_id},
      "messaging_type": "RESPONSE",
      "message":{
        "text": "...",
        "quick_replies":[
         {
            "content_type":"text",
            "title":"Inscription",
            "payload":"quick",
            "image_url":"https://media.istockphoto.com/id/1136764302/fr/vectoriel/services-dinscription-conditions-contractuelles-formulaire-de-demande.jpg?s=612x612&w=0&k=20&c=QpAcqn1gtUkGtsFiveCdUej_J3kL1XDSevTVfpz8hQ4="
          }
        ]
      }
    }
    bot.send_raw(response)


def extract_information(data):
  
    # Diviser la chaîne en fonction des virgules
    elements = data.split(',')

    # Initialiser des dictionnaires vides pour stocker les informations
    informations = {}

    # Parcourir les éléments et extraire les informations
    for element in elements:
        # Diviser chaque élément en fonction des deux-points
        parts = element.split(':')
        if len(parts) == 2:
            cle = parts[0].strip().lower()
            valeur = parts[1].strip().strip('"')
            informations[cle] = valeur

    return informations
