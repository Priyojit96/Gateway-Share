import webbrowser
url='http://sanjivani.org/'
title='SanjivaniNGOTest'
Email='email'
def share_whatsapp(url,title):
    class SocialMedia:
        def __init__(self):
            pass
        
        def SocialMedia(self):
            return {
                'whatsapp':'WhatsApp',
            }

        def ShareLinks(self):
            return [
                'whatsapp'
            ]
        
        def WithLinksByOrder(self):
            socialmediasites = self.SocialMedia().keys()
            socialmediasites.sort()
            return socialmediasites
        
        def RefLinks(self, args):
            safeargs = [
                'url',
                'title',
                'image',
                'desc',
                'appid',
                'redirecturl',
                'via',
                'hash_tags',
                'provider',
                'language',
                'user_id',
                'category',
                'phone_number',
                'email_address',
                'cc_email_address',
                'bcc_email_address',
            ]
            
            for safearg in safeargs:
                if not args.get(safearg):
                    args[safearg] = ''
            
            text = args['title']
            
            if len(args['desc']):
                text += '%20%3A%20' + args['desc']

            return {
                'whatsapp':'https://api.whatsapp.com/send?text=' + text + '%20' + args['url'],
            }

    sm = SocialMedia()
    socialmediasites = sm.ShareLinks()
    socialmediaurls = sm.RefLinks({
        'url':url, #The link Goes here.
        'title':title, #The Title of Share goes here.
    })

    for socialmediasite in socialmediasites:
        print(socialmediasite + " : " + socialmediaurls[socialmediasite])
        webbrowser.open(socialmediaurls[socialmediasite])
#share_whatsapp(url,title)