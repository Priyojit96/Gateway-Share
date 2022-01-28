import webbrowser
url='http://sanjivani.org/'
title='SanjivaniNGOTest'
Email='email'
def share_gmail(url,title):
    class SocialMedia:
        def __init__(self):
            pass
        
        def SocialMedia(self):
            return {
                'gmail':'GMail',
            }

        def ShareLinks(self):
            return [
                'gmail',
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
                'gmail':'https://mail.google.com/mail/?view=cm&to=' + args['email_address'] + '&su=' + args['title'] + '&body=' + args['url'] + '&bcc=' + args['bcc_email_address'] + '&cc=' + args['cc_email_address'],
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
#share_gmail(url,title)