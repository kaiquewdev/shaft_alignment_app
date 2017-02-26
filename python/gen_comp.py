'''Gen Comp'''

import os
import tags

template = '''
{0}
'''.format(
    tags.Tag({},'h1').html('Shaft alignment'),
)

project_location = os.path.join('/Users/silva/war/shaft_alignment_app')
template_file_path = os.path.join(project_location,'visualization/index.html')

if __name__ == '__main__':
    template_file = open(template_file_path,'w')
    template_file.write(template)
    template_file.close()
