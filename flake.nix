{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    nix-utils = {
      url = "github:mislavzanic/nix-utils";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
  outputs = inputs@{nixpkgs,nix-utils,...}: let
    inherit (nix-utils) mkPkgs mkLib;
    system = "x86_64-linux";
    pkgs = mkPkgs {inherit system; overlays = []; pkgs = nixpkgs;};
  in {
    devShells."${system}".default = pkgs.mkShell {
      buildInputs = with pkgs;
        let
          pythonPackages = ps: [
            ps.requests
            ps.beautifulsoup4
            ps.z3
            ps.numpy
            ps.matplotlib
            ps.pandas
            ps.scipy
            ps.sympy
            ps.ipython
            ps.colorama
          ];
        in [
          (python311.withPackages pythonPackages)
          nodePackages.pyright
          poetry
          pypy3
          # (pypy3.withPackages pythonPackages)
        ];
      shellHook = ''
        export PATH="$(pwd)/alias:$PATH"
        export PYTHONPATH="$(pwd):$PYTHONPATH"
        export INPUT_DIR="$(pwd)/input"
        export AOC_RUN="$(pwd)/run.py"
        export TOKEN_FILE="$HOME/.config/.aoc_token"
      '';
    };
  };
}
