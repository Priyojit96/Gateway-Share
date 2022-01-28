import webbrowser
url='http://sanjivani.org/'
title='SanjivaniNGOTest'
def share_email(url,title):
    class SocialMedia:
        def __init__(self):
            pass
        
        def SocialMedia(self):
            return {
                'email':'EMail'
            }

        def ShareLinks(self):
            return [
                'email'
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
                'email':'mailto:' + args['email_address'] + '?subject=' + args['title'] + '&body=' + args['desc'],
                
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
#share_email(url,title)