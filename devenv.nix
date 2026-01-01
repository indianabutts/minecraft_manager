{ pkgs, lib, config, ... }:

{
  # 2. Configure Python and uv
  languages.python = {
    enable = true;
    uv.enable = true;
    # Optional: creates a virtualenv automatically
    venv.enable = true;
  };

  enterShell = ''
    export UV_PYTHON=$(which python)
    echo "🐍 Python + UV Environment Loaded"
  '';
}
