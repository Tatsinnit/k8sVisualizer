# Kubernetes Cluster Visualization

## Overview

This project provides a **Kubernetes Cluster Visualization Tool** built with **Dash**, **Dash-Cytoscape**, and the **Kubernetes Python Client**. The tool dynamically fetches Kubernetes cluster data and visually represents nodes, pods, and services in an interactive graph.

### Key Features:
- **Interactive Visualization:** Graphical representation of Kubernetes nodes, pods, and services.
- **Dynamic Layouts:** Switch between grid, circle, breadth-first, and random layouts.
- **Node Interactivity:** Click nodes to view detailed information.
- **Real-Time Data Fetching:** Uses Kubernetes Python Client for live data retrieval.

## Getting Started

### Prerequisites
- Python 3.8+
- Kubernetes Cluster Access
- kubeconfig configured on your local machine

### Installation

1. Clone the repository: (you are welcome to fork and use your user name etc)
   ```bash
   git clone https://github.com/Tatsinnit/k8sVisualizer.git
   cd k8sVisualizer
   ```
2. Install required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

### Run the Application
```bash
python k8s_visualize.py
```

Open your browser and navigate to: [http://127.0.0.1:8050](http://127.0.0.1:8050)

## Screenshare for idea sake

![](./resources/quickscreencapture1.mov)

## Usage
- **Select Layout:** Use the dropdown to change the graph layout.
- **Inspect Nodes:** Click on a node to view detailed metadata.

## Project Structure
```
.
├── k8s_visualize.py            # Main Dash application
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Technologies Used
- Dash
- Dash-Cytoscape
- Kubernetes Python Client
- Python 3.x

## Contributing
Contributions are welcome! Please submit an issue or pull request.

## License
This project is licensed under the MIT License.


Feel free to contribute, share feedback, report bugs, or request features!

---

Happy Visualizing! 🚀

