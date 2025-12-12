INSTALLATION

cd ~
mkdir davids_game

cd ~/davids_game
git clone https://github.com/BruteForceLearner/BRT_FRC_AST

cd ~/davids_game/BRT_FRC_AST
python3 -m venv .venv

source .venv/bin/activate

python -m pip install -U pip
python -m pip install pygame

python main.py


PLAY

cd ~/davids_game/BRT_FRC_AST
source .venv/bin/activate
python main.py
