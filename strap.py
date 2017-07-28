import argparse
import glob
import os

from jinja2 import Template


def render(path, params):
    with open(path, 'r') as f:
        return Template(f.read()).render(params)

def mkdir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_name', required=True)
    parser.add_argument('--port', required=True)
    parser.add_argument('--output', required=True)

    args = parser.parse_args()

    output_root = os.path.join(os.path.join(args.output, ''), args.app_name)
    mkdir(output_root)

    params = {
        'app_name': args.app_name,
        'port': args.port
    }

    template_files = glob.glob('template/**', recursive=True)

    for template_file in template_files:
        if os.path.isfile(template_file):
            blob = render(template_file, params)

            # output to output_root
            path = template_file.split('/')
            path[0] = output_root

            # change src folder to app_name
            if path[1] == 'src':
                path[1] = args.app_name

            mkdir('/'.join(path[:-1]))

            with open('/'.join(path), 'w') as f:
                f.write(blob)

            # make scripts executable
            if path[1] == 'script':
                os.chmod('/'.join(path), 0o755)
