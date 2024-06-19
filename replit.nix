{pkgs}: {
  deps = [
    pkgs.gnupg
    pkgs.glibcLocales
    pkgs.borgbackup
    pkgs.rustc
    pkgs.openssl
    pkgs.libxcrypt
    pkgs.libiconv
    pkgs.cargo
    pkgs.cacert
    pkgs.taskflow
    pkgs.rapidfuzz-cpp
    pkgs.pkg-config
    pkgs.libffi
    pkgs.dbus
    pkgs.gitFull
  ];
}
