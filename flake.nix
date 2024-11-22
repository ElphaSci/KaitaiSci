{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... } @ inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        kaitaisci = pkgs.python311Packages.buildPythonPackage rec {
          pname = "kaitaisci";
          version = "0.1";
          src = builtins.fetchGit {
            ref = "main";
            url = "git@gitlab.com:cmhulbert/kaitaisci.git";
          };
          propagatedBuildInputs = with pkgs.python311Packages; [
            pillow
            kaitaistruct
          ];

          meta = {
            description = "Python Parser for Sierra Creative Interpreter files, using Kaitai";
            homepage = "https://gitlab.com/cmhulbert/kaitaisci";
            email = "cmhulbert@gmail.com";
          };
        };
      in rec {
        devShells = {
          default = pkgs.mkShell {

            packages = with pkgs; [ python311 virtualenv ] ++
              (with pkgs.python311Packages; [
                ipython
                pip
                matplotlib
                kaitaistruct
                pillow
                venvShellHook
              ]);
              venvDir = ".venv";
              postVenvCreation = ''
                unset SOURCE_DATE_EPOCH
                pip install -e .
              '';
          };
        };
      }
    );
}
