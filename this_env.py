import os


ENVRC_FMT = ".envrc"


def get_cwd():
    return os.path.abspath(os.getcwd())


def get_current_env():
    return dict(os.environ)


def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def envrc_exists(directory):
    return ENVRC_FMT in list_files(directory)


def parse_export(line):
    line_data = line.strip().split("export")[1].strip()
    env_key = line_data.split("=")[0].strip()
    env_value = "=".join(line_data.split("=")[1:]).strip()
    return env_key, env_value


def merge_envrc():
    if envrc_exists(get_cwd()):
        this_envrc = os.path.join(get_cwd(), ENVRC_FMT)
        with open(this_envrc, 'r') as fh:
            for line in fh.readlines():
                if "export" in line:
                    env_key, env_value = parse_export(line)
                    if env_key not in os.environ.keys():
                        os.environ[env_key] = env_value
                    elif env_key in os.environ.keys() and os.environ[env_key] != env_value:
                        os.environ[env_key] = env_value


def main():
    merge_envrc()


if __name__ == "__main__":
    main()
