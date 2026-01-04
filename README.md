# adventure-game# 🎮 Text Adventure Game

An interactive GUI-based dungeon adventure game built with Python and Tkinter. Navigate through a mysterious dungeon, make choices, and find the treasure while avoiding dangers!

## 🎯 Game Overview

You wake up in a dark dungeon with one goal: reach the treasure room. Navigate through different rooms using arrow keys, collect items, encounter merchants and monsters, and make strategic decisions to win the game.

## ✨ Features

- **Interactive GUI** - Built with Tkinter for a smooth user experience
- **Keyboard Controls** - Use Left/Right arrow keys to make choices
- **Dynamic Storytelling** - Multiple paths and outcomes based on your decisions
- **State Management** - Keeps track of your progress through the dungeon
- **Combat System** - Choose to fight or sneak around monsters
- **Item Collection** - Find keys and maps to help your journey
- **Win/Lose Conditions** - Multiple endings based on your choices

## 🎮 How to Play

### Controls
- **Left Arrow** ⬅️ - Choose the left path / Fight monster
- **Right Arrow** ➡️ - Choose the right path / Sneak around monster

### Game Flow
1. Start in a dark dungeon (Room 1)
2. Choose to go left or right
3. Collect items (key, map) and meet NPCs (merchant)
4. Face challenges (locked doors, monsters)
5. Make strategic decisions to survive
6. Find the treasure room to win!

### Tips
- Pay attention to the items you collect - they might be needed later
- Some paths loop back, so explore carefully
- Fighting the monster is risky but leads to victory
- Sneaking around the monster results in game over

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** - GUI framework (built into Python)

## 📁 Project Structure

```
text-adventure-game/
│
├── adventure.py          # Main game script
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies (Tkinter is built-in)
```

## 🚀 Getting Started

### Prerequisites

Python 3.x installed on your system. Tkinter comes pre-installed with Python.

### Installation

1. Clone the repository
```bash
git clone https://github.com/kananjn45/text-adventure-game.git
cd text-adventure-game
```

2. Run the game
```bash
python adventure.py
```

That's it! No additional packages needed.

## 🎯 Game Paths

### Winning Path
1. Room 1 → Go Left → Find key
2. Room 2 → Go Left → Meet merchant, get map
3. Room 3 → Go Right → Encounter monster
4. Choose Left → Fight monster (WIN!)
5. Room 3 → Go Right → Find treasure room (VICTORY!)

### Losing Path
1. Choosing to sneak around the monster (Game Over)

### Alternative Paths
- Going right in Room 1 leads to a locked door (need key)
- Various paths can loop you back to explore more

### Game Window
- Clean tan-colored interface
- Large, readable text display
- Clear choice indicators
- Interactive keyboard controls

## 🔧 Technical Highlights

- **Event-Driven Programming** - Uses Tkinter's event binding system
- **State Management** - Tracks current room and game progress
- **Dynamic UI Updates** - Story and choices update based on player actions
- **Callback Functions** - Separate functions for different game scenarios
- **Game Over Handling** - Prevents further input after game ends

## 🎓 Learning Outcomes

This project demonstrates:
- GUI development with Tkinter
- Event handling and keyboard input
- State management in Python
- Game logic and branching narratives
- User experience design
- Error handling and game flow control

## 🔮 Future Enhancements

- [ ] Add save/load game functionality
- [ ] Implement inventory system
- [ ] Add more rooms and paths
- [ ] Include sound effects
- [ ] Add character stats (health, attack)
- [ ] Create multiple difficulty levels
- [ ] Add visual graphics/images
- [ ] Implement random events

## 👤 Author

**Kanan Jain**
- Portfolio: [kananjn45.github.io/portfolio-website](https://kananjn45.github.io/portfolio-website/)
- LinkedIn: [linkedin.com/in/kanan-jain-762785298](https://www.linkedin.com/in/kanan-jain-762785298/)
- Email: kananjn45@gmail.com

## 🙏 Acknowledgments

- Built as a learning project to explore GUI development with Python
- Inspired by classic text-based adventure games
- Developed as part of 12th school project

---

⭐ Star this repository if you enjoyed playing the game!

---

<div align="center">
  Made with ❤️ and lots of ☕ by Kanan Jain
</div>
