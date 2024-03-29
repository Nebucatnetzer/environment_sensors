{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-21.11";
    flake-utils = {
      url = github:numtide/flake-utils;
      inputs.nixpkgs.follows = "nixpkgs";
    };
    pypi = {
      url = "github:DavHau/pypi-deps-db";
      flake = false;
    };
    mach-nix = {
      inputs.pypi-deps-db.follows = "pypi";
      url = "mach-nix/3.5.0";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        machNix = mach-nix.lib."${system}";
        devEnvironment = machNix.mkPython {
          requirements = builtins.readFile ./requirements.txt;
        };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            devEnvironment
            pkgs.gnumake
            pkgs.python39Packages.autopep8
            pkgs.python39Packages.black
            pkgs.python39Packages.flake8
            pkgs.python39Packages.jedi
            pkgs.python39Packages.pip
            pkgs.python39Packages.yapf
          ];
          shellHook = ''
            export DJANGO_SETTINGS_MODULE=sensors.settings.development; \
          '';
        };
        packages.venv = devEnvironment;
        defaultPackage = (machNix.mkDockerImage {
          packagesExtra = with pkgs;
            [ pkgs.bash ];
          requirements = builtins.readFile ./requirements.txt;
          _.pytest-cov.propagatedBuildInputs.mod = pySelf: self: oldVal: oldVal ++ [ pySelf.tomli ];
        }).override
          (oldAttrs: {
            name = "environment-sensors";
            config.Cmd = [ "run.sh" ];
          });
      });
}
