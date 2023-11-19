set -eux

mkdir miniplaner

bash install_wxwidgets.sh
bash install_meson.sh
bash download_miniplaner.sh
bash build_miniplaner.sh
