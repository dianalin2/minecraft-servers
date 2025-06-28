import docker
import glob
import yaml
import os
from os import path

client = docker.from_env()

IMAGE_NAME = os.getenv('IMAGE_NAME', None)
if not IMAGE_NAME:
    raise ValueError("IMAGE_NAME environment variable is not set. Please set it to the desired image tag prefix.")

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

for config_file in glob.iglob('*/server.yaml'):
    print(f'Building image from {config_file}')

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    context_dir = path.abspath(path.join(path.dirname(config_file), config['build'].get('context', '.')))

    tag = f"{IMAGE_NAME}:{config['id']}"
    
    # build
    client.images.build(
        path=context_dir,
        dockerfile=path.join(context_dir, config['build'].get('dockerfile', 'Dockerfile')),
        buildargs=config['build'].get('args', {}),
        tag=tag,
    )

    print('Pushing image:', tag)

    resp = client.images.push(
        repository=f"{IMAGE_NAME}",
        tag=config['id'],
        stream=True,
        decode=True
    )

    for line in resp:
        if LOG_LEVEL == 'DEBUG':
            print(line)

        if 'error' in line:
            print(f"Error pushing image {tag}: {line['error']}")

    print(f"Successfully pushed image {tag}")
