{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  buildInputs = [
    python310
    nodePackages.pyright
    python310Packages.z3
    python310Packages.numpy
    python310Packages.matplotlib
    python310Packages.pandas
    python310Packages.scipy
    python310Packages.ipython
    python310Packages.requests
  ];
}
