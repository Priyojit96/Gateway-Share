import webbrowser
url='http://sanjivani.org/'
title='SanjivaniNGOTest'
Email='email'
def share_twitter(url,title):
    class SocialMedia:
        def __init__(self):
            pass
        
        def SocialMedia(self):
            return {
                'twitter':'Twitter',
            }

        def ShareLinks(self):
            return [
                'twitter',
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
                'twitter':'https://twitter.com/intent/tweet?url=' + args['url'] + '&text=' + text + '&via=' + args['via'] + '&hashtags=' + args['hash_tags'],
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
#share_twitter(url,title)