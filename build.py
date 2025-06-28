import docker
import glob
import yaml
import os
from os import path

client = docker.from_env()

TAG_PREFIX = os.getenv('TAG_PREFIX', None)
if not TAG_PREFIX:
    raise ValueError("TAG_PREFIX environment variable is not set. Please set it to the desired image tag prefix.")

for config_file in glob.iglob('*/server.yaml'):
    print(f'Building image from {config_file}')

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    context_dir = path.abspath(path.join(path.dirname(config_file), config['build'].get('context', '.')))
    
    # build
    client.images.build(
        path=context_dir,
        dockerfile=path.join(context_dir, config['build'].get('dockerfile', 'Dockerfile')),
        buildargs=config['build'].get('args', {}),
        tag=f"{TAG_PREFIX}:{config['id']}",
    )

    print('Pushing image...')

    client.images.push(
        repository=f"{TAG_PREFIX}",
        tag=config['id'],
        stream=True,
        decode=True
    )
