'''Gen Comp'''

import os
import tags

template = '''
{0}
'''.format(
       tags.Tag({},'html').html(''.join([
           tags.Tag({},'head').html(''.join([
               tags.Link({'href':'../bower_components/bootstrap/dist/css/bootstrap.min.css','rel':'stylesheet'}).html(),
               tags.Link({'href':'../bower_components/bootstrap/dist/css/bootstrap-theme.min.css','rel':'stylesheet'}).html(),
           ])),
           tags.Body({'class':'container'},'body').html(''.join([
               tags.Tag({},'h1').html('Shaft alignment'),
               tags.Tag({},'hr').html(),
               tags.Tag({'style':'width:50em;margin-left:.7em;','placeholder':' Center to center'},'input').html(), tags.Tag({},'br').html(),
               tags.Tag({'style':'width:50em;margin-left:.7em;','placeholder':' Center to cylinder'},'input').html(), tags.Tag({},'br').html(),
               tags.Tag({'style':'width:50em;margin-left:.7em;','placeholder':' Axis to feet'},'input').html(), tags.Tag({},'br').html(),
               tags.Tag({'style':'width:50em;margin-left:.7em;','placeholder':' Feet to feet'},'input').html(), tags.Tag({},'br').html(),
               tags.Tag({'style':'width:50em;margin-left:.7em;'},'button').html('Register'), tags.Tag({},'br').html(),
               tags.Tag({},'hr').html(),
           ]))
    ]))
)

project_location = os.path.join('/Users/silva/war/shaft_alignment_app')
template_file_path = os.path.join(project_location,'visualization/index.html')

if __name__ == '__main__':
    template_file = open(template_file_path,'w')
    template_file.write(template)
    template_file.close()
