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
    overlays = [];
    system = "x86_64-linux";
    pkgs = mkPkgs {inherit system overlays; pkgs = nixpkgs;};
  in {
    devShells."${system}".default = pkgs.mkShell {
      buildInputs = with pkgs; [
        (python311.withPackages (ps: [
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
        ]))
        nodePackages.pyright
        poetry
        pypy3
      ];
      shellHook = ''
        export PYTHONPATH="$(pwd):$PYTHONPATH"
      '';
    };
  };
}
